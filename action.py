
from typing import List, Tuple, Dict, Union
import fighter, armors, weapons, defaultSkills, interaction, random, math

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
            
    def acts(self, fighter : fighter.CHARACTER, targets : Union[Tuple[int,int], List[fighter.CHARACTER], Union[armors.ARMOR, weapons.WEAPON, weapons.RANGE_WEAPON]], hand="left"):
        fighter.dodgePercent += fighter.dodgePercent * self.dodge_alteration
        actionName = self.name
        if "-lv" in actionName:
            actionName = actionName.split("-lv")[0]
        fighter.useSkill(actionName)
        interaction.showInformation("fighter "+fighter.name+" uses "+self.name)


class Equip(Action): 
    def __init__(self):
        super().__init__("Equip", 1, 0, 1, 0)
    
    def acts(self, fighter : fighter.CHARACTER, targets : Union[armors.ARMOR, weapons.WEAPON, weapons.RANGE_WEAPON], hand="left"):
        fighter.equip(targets,hand)
    
    

class Movement(Action):
    def __init__(self, action_name: str, StaminaCost: int, UpgradeExpCost: int, speed : int, dodge_alteration :int, level : int):
        super().__init__(action_name, StaminaCost, UpgradeExpCost, level, dodge_alteration)
        self.speed = speed
    
    def acts(self, fighter : fighter.CHARACTER, targets : Tuple[int,int], hand="left"):
        interaction.showInformation(fighter.name+" move to "+str(targets))
        super(Movement, self).acts(fighter,targets)
        pass # move fighter at target emplacement if possible

class Quick_Movement(Movement):
    Level_Parameters = defaultSkills.DEFAULT_SKILLS[defaultSkills.QM]
    def __init__(self, level: int):
        super().__init__("Quick_Movement"+"-lv"+str(level), level=level, **Quick_Movement.Level_Parameters[level])
    
class Classic_Movement(Movement):
    Level_Parameters = defaultSkills.DEFAULT_SKILLS[defaultSkills.CM]
    def __init__(self, level: int):
        super().__init__("Classic_Movement"+"-lv"+str(level), level=level, **Classic_Movement.Level_Parameters[level])
        
class Slow_Movement(Movement):
    Level_Parameters = defaultSkills.DEFAULT_SKILLS[defaultSkills.SM]
    def __init__(self, level: int):
        super().__init__("Slow_Movement"+"-lv"+str(level), level=level, **Slow_Movement.Level_Parameters[level])

        
        
        
class Attack(Action):
    def __init__(self, action_name: str, StaminaCost: int, UpgradeExpCost: int, damageFactor : int, level : int, dodge_alteration : int):
        super().__init__(action_name, StaminaCost, UpgradeExpCost, level, dodge_alteration)
        self.factor = damageFactor
        
    def acts(self, fighter : fighter.CHARACTER, targets : List[fighter.CHARACTER], hand="left"):
        super(Attack,self).acts(fighter, targets)
        potential_damage = 0
        if hand == "left" :
            potential_damage += fighter.leftTool.damage
            damage_type = fighter.leftTool.damageType
        else : 
            potential_damage += fighter.rightTool.damage
            damage_type = fighter.rightTool.damageType
        potential_damage = potential_damage * self.factor
        
        for target in targets:
            if self.name.startswith("Quick_Attack") or target.dodge() != True:
                interaction.showInformation(fighter.name+" attack "+target.name+" with "+str(potential_damage)+" damage")
                target.take_damage(potential_damage, damage_type)
            else:
                interaction.showInformation(target.name+" dodged attack")
        
class Brutal_Attack(Attack):
    Level_Parameters = defaultSkills.DEFAULT_SKILLS[defaultSkills.BA]
    def __init__(self, level : int):
        super().__init__("Brutal_Attack"+"-lv"+str(level),level=level, **Brutal_Attack.Level_Parameters[level])
        self.level = level
class Quick_Attack(Attack):
    Level_Parameters = defaultSkills.DEFAULT_SKILLS[defaultSkills.QA]
    def __init__(self, level : int):
        super().__init__("Quick_Attack"+"-lv"+str(level),level=level, **Quick_Attack.Level_Parameters[level])
        self.level = level
class Classic_Attack(Attack):
    Level_Parameters = defaultSkills.DEFAULT_SKILLS[defaultSkills.CA]
    def __init__(self, level : int):
        super().__init__("Classic_Attack"+"-lv"+str(level),level=level, **Classic_Attack.Level_Parameters[level])
        self.level = level
        
class Shot(Action):
    
    def __init__(self, action_name: str, StaminaCost: int, UpgradeExpCost: int, level : int, accuracy : int, dodge_alteration : int):
        super().__init__(action_name, StaminaCost, UpgradeExpCost, level, dodge_alteration)
        self.accuracy = accuracy
       
    def acts(self, fighter : fighter.CHARACTER, targets : List[fighter.CHARACTER], hand="left"):
        super(Shot,self).acts(fighter,None)
        if hand == "left":
            weapon = fighter.leftTool
        else:
            weapon = fighter.rightTool
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
                        target.take_damage(potential_damage, damage_type)
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
                targets[0].take_damage(potential_damage, damage_type)
            else:
                interaction.showInformation(targets[0].name+" dodged attack")
            targets[0].inventory.append(weapon)
        

class Precise_Shot(Shot):
    Level_Parameters = defaultSkills.DEFAULT_SKILLS[defaultSkills.PS]
    def __init__(self, level : int):
        super().__init__("Precise_Shot"+"-lv"+str(level),level=level, **Precise_Shot.Level_Parameters[level])
        self.level = level
        

class Quick_Shot(Shot):
    Level_Parameters = defaultSkills.DEFAULT_SKILLS[defaultSkills.QS]
    def __init__(self, level : int):
        super().__init__("Quick_Shot"+"-lv"+str(level),level=level, **Quick_Shot.Level_Parameters[level])
        self.level = level

class Classic_Shot(Shot):
    Level_Parameters = defaultSkills.DEFAULT_SKILLS[defaultSkills.CS]
    def __init__(self, level : int):
        super().__init__("Classic_Shot"+"-lv"+str(level),level=level, **Classic_Shot.Level_Parameters[level])
        self.level = level


        
class Defense(Action):
    def __init__(self, action_name: str, StaminaCost: int, UpgradeExpCost: int, defensePoints : int, level:int, dodge_alteration : int):
        super().__init__(action_name, StaminaCost, UpgradeExpCost, level, dodge_alteration)        
        self.defensePoints = defensePoints
        
    def acts(self, fighter : fighter.CHARACTER, hand="left"):
        super(Defense,self).acts(fighter,None)
        fighter.defensePoints += self.defensePoints
        if self.defensePoints > 0:
            interaction.showInformation("fighter "+fighter.name+" protect itself with "+str(self.defensePoints)+" temporary armor, total temporary armor:"+str(fighter.defensePoints))
        else:
            interaction.showInformation("fighter "+fighter.name+" protect itself by dividing damage by "+str(-self.defensePoints))

class Light_Defense(Defense):
    Level_Parameters = defaultSkills.DEFAULT_SKILLS[defaultSkills.LD]
    def __init__(self, level : int):
        super().__init__("Light_Defense"+"-lv"+str(level),level=level, **Light_Defense.Level_Parameters[level])
    
class Stoical_Defense(Defense): # for stoical_Defense, damage is divided by the absolute value of defensePoints in fighter.py but it is the only action authorized for unit
    Level_Parameters = defaultSkills.DEFAULT_SKILLS[defaultSkills.SD]
    def __init__(self, level : int):
        super().__init__("Stoical_Defense"+"-lv"+str(level),level=level, **Stoical_Defense.Level_Parameters[level])
   
        
class Classic_Defense(Defense):
    Level_Parameters = defaultSkills.DEFAULT_SKILLS[defaultSkills.CD]
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

ABSTRACT = [Action, Attack, Defense, Movement, Shot]

                
if __name__ == '__main__':
    setupActions()
    #print(Action.ACTIONS_DICT)