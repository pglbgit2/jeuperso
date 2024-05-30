
from typing import List, Tuple, Dict, Union
import fighter, armors, weapons, defaultSkills, interaction, random, math, consumable

class Action:
    ACTIONS_DICT : Dict[str,'Action'] = {}
    
    def __init__(self, action_name : str, StaminaCost: int, UpgradeExpCost : int, level : int, dodge_alteration : int):
        if action_name not in Action.ACTIONS_DICT.keys():
            Action.ACTIONS_DICT[action_name] = self
            self.name = action_name
            self.upgrades : List['Action'] = []
            self.staminaCost = StaminaCost
            self.upgradeExpCost = UpgradeExpCost
            self.level = level
            self.dodge_alteration = dodge_alteration
        else: raise Exception("Already Existing Action")
    
    def addUpgrade(self, upgrade: 'Action'):
        if upgrade not in self.upgrades:
            self.upgrades.append(upgrade)
            
    def acts(self, fighter : fighter.CHARACTER, targets : List[fighter.CHARACTER], otherInfos : Dict[str, Union[Tuple[int,int], List[fighter.CHARACTER], Union[armors.ARMOR, weapons.WEAPON, weapons.RANGE_WEAPON], consumable.Consumable]]):
        fighter.dodgePercent += fighter.dodgePercent * self.dodge_alteration
        actionName = self.name
        if "-lv" in actionName:
            actionName = actionName.split("-lv")[0]
        fighter.useSkill(actionName)
        interaction.showInformation("fighter "+fighter.name+" uses "+self.name)

class EnergyUsingAction(Action):
    def __init__(self, action_name : str, ManaCost: int, UpgradeExpCost : int, level:int, dodge_alteration : int):
        super().__init__(action_name, 0, UpgradeExpCost, level, dodge_alteration)
        self.manaCost = ManaCost
    
    def acts(self, fighter : fighter.CHARACTER, targets : List[fighter.CHARACTER], otherInfos : Dict[str, Union[Tuple[int,int], List[fighter.CHARACTER], Union[armors.ARMOR, weapons.WEAPON, weapons.RANGE_WEAPON], consumable.Consumable]]):
        super(EnergyUsingAction, self).acts(fighter,targets,otherInfos)
        fighter.magic -= self.manaCost


class MagicAggression(EnergyUsingAction):
    def __init__(self, action_name : str, ManaCost: int, UpgradeExpCost : int, level:int, dodge_alteration : int, damage : int, damageType : str):
        super().__init__(action_name, ManaCost, UpgradeExpCost, level, dodge_alteration)
        self.damage = damage
        self.damageType = damageType
    
    def acts(self, fighter : fighter.CHARACTER, targets : List[fighter.CHARACTER], otherInfos : Dict[str, Union[Tuple[int,int], List[fighter.CHARACTER], Union[armors.ARMOR, weapons.WEAPON, weapons.RANGE_WEAPON], consumable.Consumable]]):
        super(MagicAggression, self).acts(fighter,targets,otherInfos)
        potential_damage = self.damage
        potential_damage += fighter.damageBonus

        for target in targets:
            bodyPart = target.tryToHit(otherInfos["bodyPart"])

            if target.dodge(bodyPart=bodyPart) != True:
                interaction.showInformation(fighter.name+" attack "+target.name+" with "+str(potential_damage)+" damage")
                target.take_damage(potential_damage, self.damageType)
            else:
                interaction.showInformation(target.name+" dodged attack")
 
class EnergyRay(MagicAggression):
    Level_Parameters = defaultSkills.UPGRADABLE[defaultSkills.ER]
    def __init__(self, level: int):
        super().__init__("EnergyRay"+"-lv"+str(level), level=level, **EnergyRay.Level_Parameters[level])
    

class EnergyOrb(MagicAggression):
    Level_Parameters = defaultSkills.UPGRADABLE[defaultSkills.EO]
    def __init__(self, level: int):
        super().__init__("EnergyOrb"+"-lv"+str(level), level=level, **EnergyOrb.Level_Parameters[level])
        
class FireBreath(MagicAggression):
    Level_Parameters = defaultSkills.UPGRADABLE[defaultSkills.FB]
    def __init__(self, level: int):
        super().__init__("FireBreath"+"-lv"+str(level), level=level, **FireBreath.Level_Parameters[level])
        
class FireBall(MagicAggression):
    Level_Parameters = defaultSkills.UPGRADABLE[defaultSkills.FBa]
    def __init__(self, level: int):
        super().__init__("FireBall"+"-lv"+str(level), level=level, **FireBall.Level_Parameters[level])

class FireStorm(MagicAggression):
    Level_Parameters = defaultSkills.UPGRADABLE[defaultSkills.FS]
    def __init__(self, level: int):
        super().__init__("FireStorm"+"-lv"+str(level), level=level, **FireStorm.Level_Parameters[level])
        

    
class Invocation(EnergyUsingAction):
    def __init__(self, action_name: str, ManaCost: int, UpgradeExpCost: int, dodge_alteration :int, level : int, invocation:str):
        super().__init__(action_name, ManaCost, UpgradeExpCost,level, dodge_alteration)
        self.invoke = invocation
        
    def acts(self, fighter : fighter.CHARACTER, targets : List[fighter.CHARACTER], otherInfos : Dict[str, Union[Tuple[int,int], List[fighter.CHARACTER], Union[armors.ARMOR, weapons.WEAPON, weapons.RANGE_WEAPON], consumable.Consumable]]):
        interaction.showInformation(fighter.name+" invoke "+self.invoke)
        if self.invoke in weapons.INVOCATION:
            if self.invoke in weapons.MELEE_WEAPONS:
                item = weapons.WEAPON.get_melee_weapon(self.invoke)
            fighter.inventory.append(item)
            if fighter.leftTool == None:
                fighter.leftTool = item
            elif fighter.rightTool == None:
                fighter.rightTool = item
                
                
class Energy_Blade(Invocation):
    def __init__(self):
        super().__init__("Energy_Blade", ManaCost=5, UpgradeExpCost=0, level=1, dodge_alteration=0,invocation="ENERGY_BLADE")
    

class Magic_Armor(EnergyUsingAction):
    def __init__(self, action_name: str, ManaCost: int, UpgradeExpCost: int, protection : int, dodge_alteration :int, level : int):
        super().__init__(action_name, ManaCost, UpgradeExpCost, level, dodge_alteration)
        self.protection = protection
    
    def acts(self, fighter : fighter.CHARACTER, targets : List[fighter.CHARACTER], otherInfos : Dict[str, Union[Tuple[int,int], List[fighter.CHARACTER], Union[armors.ARMOR, weapons.WEAPON, weapons.RANGE_WEAPON], consumable.Consumable]]):
        super(Magic_Armor,self).acts(fighter,targets,otherInfos)
        protection = math.ceil((self.protection)/(1+len(targets)))
        fighter.defensePoints += protection
        interaction.showInformation(fighter.name+" protect itself using Magic Armor for "+str(protection))
        
        for target in targets:
            target.defensePoints += protection
            interaction.showInformation(fighter.name+" protect "+target.name+" for "+str(protection))
            
            

class Minor_Shield(Magic_Armor):
    Level_Parameters = defaultSkills.UPGRADABLE[defaultSkills.MS]
    def __init__(self, level: int):
        super().__init__("Minor_Shield"+"-lv"+str(level), level=level, **Minor_Shield.Level_Parameters[level])
    
class Protection_Field(Magic_Armor):
    Level_Parameters = defaultSkills.UPGRADABLE[defaultSkills.PF]
    def __init__(self, level: int):
        super().__init__("Protection_Field"+"-lv"+str(level), level=level, **Protection_Field.Level_Parameters[level])
        
        
        
        
        
        
class Energy_Damage_Boost(EnergyUsingAction):
    def __init__(self, action_name: str, ManaCost: int, UpgradeExpCost: int, damageBoost : int, dodge_alteration :int, level : int):
        super().__init__(action_name, ManaCost, UpgradeExpCost, level, dodge_alteration)
        self.damageBoost = damageBoost
    
    def acts(self, fighter : fighter.CHARACTER, targets : List[fighter.CHARACTER], otherInfos : Dict[str, Union[Tuple[int,int], List[fighter.CHARACTER], Union[armors.ARMOR, weapons.WEAPON, weapons.RANGE_WEAPON], consumable.Consumable]]):
        super(Energy_Damage_Boost,self).acts(fighter,None,otherInfos)
        fighter.damageBonus += self.damageBoost
        interaction.showInformation(fighter.name+" boost its damage using energy by "+str(self.damageBoost))
        

class Minor_Aggressive_Flux(Energy_Damage_Boost):
    Level_Parameters = defaultSkills.UPGRADABLE[defaultSkills.MAF]
    def __init__(self, level: int):
        super().__init__("Minor_Aggressive_Flux"+"-lv"+str(level), level=level, **Minor_Aggressive_Flux.Level_Parameters[level])
    
class Wrath_Torrent(Energy_Damage_Boost):
    Level_Parameters = defaultSkills.UPGRADABLE[defaultSkills.WT]
    def __init__(self, level: int):
        super().__init__("Wrath_Torrent"+"-lv"+str(level), level=level, **Wrath_Torrent.Level_Parameters[level])
        







class useConsumable(Action):
    def __init__(self):
        super().__init__("useConsumable",1,0,1,0)

    def acts(self, fighter : fighter.CHARACTER, targets : List[fighter.CHARACTER], otherInfos : Dict[str, Union[Tuple[int,int], List[fighter.CHARACTER], Union[armors.ARMOR, weapons.WEAPON, weapons.RANGE_WEAPON], consumable.Consumable]]):
        fighter.useConsumable(otherInfos["Equipment"])


class Equip(Action): 
    def __init__(self):
        super().__init__("Equip", 1, 0, 1, 0)
    
    def acts(self, fighter : fighter.CHARACTER, targets : List[fighter.CHARACTER], otherInfos : Dict[str, Union[Tuple[int,int], List[fighter.CHARACTER], Union[armors.ARMOR, weapons.WEAPON, weapons.RANGE_WEAPON], consumable.Consumable]]):
        fighter.equip(otherInfos["item"],otherInfos["bodyPart"])
    

class Movement(Action):
    def __init__(self, action_name: str, StaminaCost: int, UpgradeExpCost: int, speed : int, dodge_alteration :int, level : int):
        super().__init__(action_name, StaminaCost, UpgradeExpCost, level, dodge_alteration)
        self.speed = speed
    
    def acts(self, fighter : fighter.CHARACTER, targets : List[fighter.CHARACTER], otherInfos : Dict[str, Union[Tuple[int,int], List[fighter.CHARACTER], Union[armors.ARMOR, weapons.WEAPON, weapons.RANGE_WEAPON], consumable.Consumable]]):
        interaction.showInformation(fighter.name+" move")
        super(Movement, self).acts(fighter,targets,otherInfos)
        pass # move fighter at target emplacement if possible

class Quick_Movement(Movement):
    Level_Parameters = defaultSkills.UPGRADABLE[defaultSkills.QM]
    def __init__(self, level: int):
        super().__init__("Quick_Movement"+"-lv"+str(level), level=level, **Quick_Movement.Level_Parameters[level])
    
class Classic_Movement(Movement):
    Level_Parameters = defaultSkills.UPGRADABLE[defaultSkills.CM]
    def __init__(self, level: int):
        super().__init__("Classic_Movement"+"-lv"+str(level), level=level, **Classic_Movement.Level_Parameters[level])
        
class Slow_Movement(Movement):
    Level_Parameters = defaultSkills.UPGRADABLE[defaultSkills.SM]
    def __init__(self, level: int):
        super().__init__("Slow_Movement"+"-lv"+str(level), level=level, **Slow_Movement.Level_Parameters[level])



def parry(target : fighter.CHARACTER, fighter : fighter.CHARACTER):
    if random.random() < 0.3:
        (hand, bodyPart, doQuickAttack) = target.getParryInfos()
        if not doQuickAttack:
            Action.ACTIONS_DICT["Classic_Attack"+target.getStrLevelOfSkill("Classic_Attack")].acts(target,[fighter], {"hand":hand,"bodyPart" : bodyPart, "name" : "Classic_Attack"})
        else:
            Action.ACTIONS_DICT["Quick_Attack"+target.getStrLevelOfSkill("Quick_Attack")].acts(target,[fighter], {"hand":hand,"bodyPart" : bodyPart, "name" : "Quick_Attack"})

        
class Melee_Combat(Action):
    def __init__(self):
        super().__init__("Melee_Combat", 3, 0, 1, 0)
    
    def acts(self, fighter : fighter.CHARACTER, targets : List[fighter.CHARACTER], otherInfos : Dict[str, Union[Tuple[int,int], List[fighter.CHARACTER], Union[armors.ARMOR, weapons.WEAPON, weapons.RANGE_WEAPON], consumable.Consumable]]):
        potential_damage = fighter.default_damage+fighter.damageBonus
        damage_type = fighter.default_damage_type
        
        for target in targets:
            bodyPart = target.tryToHit(otherInfos["bodyPart"])
            canParry = False
            modifier = 0
            if (target.leftTool != None and target.leftTool.name in weapons.DEFENSIVE_WEAPON ) or (target.rightTool != None and target.rightTool.name in weapons.DEFENSIVE_WEAPON):
                canParry = True
                if bodyPart == "torso":
                    modifier += 0.2
            if not target.dodge(bodyPart=bodyPart, modification=modifier):
                    interaction.showInformation(fighter.name+" attack "+target.name+" with "+str(potential_damage)+" damage")
                    target.take_damage(potential_damage, damage_type, bodyPart)
            else:
                interaction.showInformation(target.name+" dodged attack")
                if canParry :
                    parry(target, fighter)
                    
                
class Attack(Action):
    def __init__(self, action_name: str, StaminaCost: int, UpgradeExpCost: int, damageFactor : int, level : int, dodge_alteration : int):
        super().__init__(action_name, StaminaCost, UpgradeExpCost, level, dodge_alteration)
        self.factor = damageFactor
        
    def acts(self, fighter : fighter.CHARACTER, targets : List[fighter.CHARACTER], otherInfos : Dict[str, Union[Tuple[int,int], List[fighter.CHARACTER], Union[armors.ARMOR, weapons.WEAPON, weapons.RANGE_WEAPON], consumable.Consumable]]):
        super(Attack,self).acts(fighter, targets, otherInfos)
        potential_damage = 0
        if otherInfos["hand"] == "left" :
            if fighter.leftTool == None:
                Action.ACTIONS_DICT["Melee_Combat"].acts(fighter,targets,otherInfos)
                return
            potential_damage += fighter.leftTool.damage
            damage_type = fighter.leftTool.damageType
            aWeapon = fighter.leftTool
        else : 
            if fighter.rightTool == None:
                Action.ACTIONS_DICT["Melee_Combat"].acts(fighter,targets,otherInfos)
                return
            potential_damage += fighter.rightTool.damage
            damage_type = fighter.rightTool.damageType
            aWeapon = fighter.rightTool
        potential_damage = potential_damage * self.factor
        potential_damage += fighter.damageBonus
        for target in targets:
            bodyPart = target.tryToHit(otherInfos["bodyPart"])
            noFail = False
            modifier = 0
            if self.name.startswith("Quick_Attack"):
                if aWeapon.name in weapons.SMALL_WEAPON:
                    noFail = True
                else:
                    modifier = -0.4
            canParry = False
            if (target.leftTool != None and target.leftTool.name in weapons.DEFENSIVE_WEAPON ) or (target.rightTool != None and target.rightTool.name in weapons.DEFENSIVE_WEAPON):
                canParry = True
                if bodyPart == "torso":
                    modifier += 0.2
            if noFail or not target.dodge(bodyPart=bodyPart, modification=modifier):
                interaction.showInformation(fighter.name+" attack "+target.name+" with "+str(potential_damage)+" damage")
                target.take_damage(potential_damage, damage_type, bodyPart)
            else:
                interaction.showInformation(target.name+" dodged attack")
                if canParry :
                    parry(target, fighter)
        
class Brutal_Attack(Attack):
    Level_Parameters = defaultSkills.UPGRADABLE[defaultSkills.BA]
    def __init__(self, level : int):
        super().__init__("Brutal_Attack"+"-lv"+str(level),level=level, **Brutal_Attack.Level_Parameters[level])
        self.level = level
class Quick_Attack(Attack):
    Level_Parameters = defaultSkills.UPGRADABLE[defaultSkills.QA]
    def __init__(self, level : int):
        super().__init__("Quick_Attack"+"-lv"+str(level),level=level, **Quick_Attack.Level_Parameters[level])
        self.level = level
class Classic_Attack(Attack):
    Level_Parameters = defaultSkills.UPGRADABLE[defaultSkills.CA]
    def __init__(self, level : int):
        super().__init__("Classic_Attack"+"-lv"+str(level),level=level, **Classic_Attack.Level_Parameters[level])
        self.level = level
        
class Shot(Action):
    
    def __init__(self, action_name: str, StaminaCost: int, UpgradeExpCost: int, level : int, accuracy : int, dodge_alteration : int):
        super().__init__(action_name, StaminaCost, UpgradeExpCost, level, dodge_alteration)
        self.accuracy = accuracy
       
    def acts(self, fighter : fighter.CHARACTER, targets : List[fighter.CHARACTER], otherInfos : Dict[str, Union[Tuple[int,int], List[fighter.CHARACTER], Union[armors.ARMOR, weapons.WEAPON, weapons.RANGE_WEAPON], consumable.Consumable]]):
        super(Shot,self).acts(fighter,None,otherInfos)
        if otherInfos["hand"] == "left":
            weapon = fighter.leftTool
            if weapon == None:
                return
        else:
            weapon = fighter.rightTool
            if weapon == None:
                return
        assert (weapon != None and weapon.name in weapons.RANGE_WEAPONS) or weapon.name in weapons.THROWABLE
        
        if weapon.name in weapons.RANGE_WEAPONS:
            for target in targets:
                munition : weapons.WEAPON = fighter.removeItemFromInventoryByName(getattr(weapons,weapon.name,None)["munition"])
                potential_damage = 0
                if munition != None:
                    potential_damage += munition.damage
                    damage_type = munition.damageType
                    if fighter.shot(self.accuracy+weapon.accuracy):
                        interaction.showInformation(fighter.name+" attack "+target.name+" with "+str(potential_damage)+" damage")
                        bodyPart = target.tryToHit(otherInfos["bodyPart"])
                        target.take_damage(potential_damage, damage_type, bodyPart)
                    else:
                        interaction.showInformation(target.name+" dodged attack")
                else:
                    interaction.showInformation("no munition left")
        
        elif weapon.name in weapons.THROWABLE:
            fighter.removeItemFromInventoryByName(weapon.name)
            assert len(targets) == 1
            potential_damage = weapon.damage
            damage_type = weapon.damage
            if fighter.shot(self.accuracy):
                interaction.showInformation(fighter.name+" attack "+targets[0].name+" with "+str(potential_damage)+" damage")
                bodyPart = target.tryToHit(otherInfos["bodyPart"])
                targets[0].take_damage(potential_damage, damage_type, bodyPart)
            else:
                interaction.showInformation(targets[0].name+" dodged attack")
            #targets[0].inventory.append(weapon)
            return weapon

class Precise_Shot(Shot):
    Level_Parameters = defaultSkills.UPGRADABLE[defaultSkills.PS]
    def __init__(self, level : int):
        super().__init__("Precise_Shot"+"-lv"+str(level),level=level, **Precise_Shot.Level_Parameters[level])
        self.level = level
        

class Quick_Shot(Shot):
    Level_Parameters = defaultSkills.UPGRADABLE[defaultSkills.QS]
    def __init__(self, level : int):
        super().__init__("Quick_Shot"+"-lv"+str(level),level=level, **Quick_Shot.Level_Parameters[level])
        self.level = level

class Classic_Shot(Shot):
    Level_Parameters = defaultSkills.UPGRADABLE[defaultSkills.CS]
    def __init__(self, level : int):
        super().__init__("Classic_Shot"+"-lv"+str(level),level=level, **Classic_Shot.Level_Parameters[level])
        self.level = level


        
class Defense(Action):
    def __init__(self, action_name: str, StaminaCost: int, UpgradeExpCost: int, defensePoints : int, level:int, dodge_alteration : int):
        super().__init__(action_name, StaminaCost, UpgradeExpCost, level, dodge_alteration)        
        self.defensePoints = defensePoints
        
    def acts(self, fighter : fighter.CHARACTER, targets : List[fighter.CHARACTER], otherInfos : Dict[str, Union[Tuple[int,int], List[fighter.CHARACTER], Union[armors.ARMOR, weapons.WEAPON, weapons.RANGE_WEAPON], consumable.Consumable]]):
        super(Defense,self).acts(fighter,None,None)
        if self.defensePoints > 0:
            fighter.defensePoints += self.defensePoints
        if self.defensePoints < 0:
            fighter.DamageDivisor = -self.defensePoints
        if self.defensePoints > 0:
            interaction.showInformation("fighter "+fighter.name+" protect itself with "+str(self.defensePoints)+" temporary armor, total temporary armor:"+str(fighter.defensePoints))
        else:
            interaction.showInformation("fighter "+fighter.name+" protect itself by dividing damage by "+str(-self.defensePoints))

class Light_Defense(Defense):
    Level_Parameters = defaultSkills.UPGRADABLE[defaultSkills.LD]
    def __init__(self, level : int):
        super().__init__("Light_Defense"+"-lv"+str(level),level=level, **Light_Defense.Level_Parameters[level])
    
class Stoical_Defense(Defense): # for stoical_Defense, damage is divided by the absolute value of defensePoints in fighter.py but it is the only action authorized for unit
    Level_Parameters = defaultSkills.UPGRADABLE[defaultSkills.SD]
    def __init__(self, level : int):
        super().__init__("Stoical_Defense"+"-lv"+str(level),level=level, **Stoical_Defense.Level_Parameters[level])
   
        
class Classic_Defense(Defense):
    Level_Parameters = defaultSkills.UPGRADABLE[defaultSkills.CD]
    def __init__(self, level : int):
        super().__init__("Classic_Defense"+"-lv"+str(level),level=level, **Classic_Defense.Level_Parameters[level])
    


def setupActions():
    import sys, inspect
    for name, obj in inspect.getmembers(sys.modules[__name__]):
        if inspect.isclass(obj):
            if obj not in ABSTRACT:
                #print(obj)
                if hasattr(obj, 'Level_Parameters'):
                    ClassLevel = []
                    i = 0
                    for level in obj.Level_Parameters.keys():
                        ClassLevel.append(obj(level))
                        if i>0:
                            ClassLevel[i-1].upgrades.append(ClassLevel[i])
                        i+=1
                else:
                    obj()

ABSTRACT = [Action, Attack, Defense, Movement, Shot, EnergyUsingAction, Magic_Armor, Energy_Damage_Boost, Invocation, MagicAggression]

                
if __name__ == '__main__':
    setupActions()
    #print(Action.ACTIONS_DICT)