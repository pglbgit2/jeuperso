
from typing import List, Tuple, Dict, Union
import fighter, armors, weapons

class Action:
    ACTIONS_DICT = {}
    
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
            
    def acts(self, fighter : fighter.CHARACTER, targets : Union[Tuple[int,int], List[fighter.CHARACTER]], hand="left"):
        fighter.dodgePercent += fighter.dodgePercent * self.dodge_alteration
    
    
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
        super(Movement, self).acts(fighter,targets)
        pass # move fighter at target emplacement if possible

class Quick_Movement(Movement):
    Level_Parameters = {
        1 : {"StaminaCost" : 3, "UpgradeExpCost" : 10, "speed" : 5, "dodge_alteration" : -0.15},
        2 : {"StaminaCost" : 3, "UpgradeExpCost" : 25, "speed" : 8, "dodge_alteration" : -0.20}
    }
    def __init__(self, level: int):
        super().__init__("Quick_Movement"+"-lv"+str(level), level=level, **Quick_Movement.Level_Parameters[level])
    
class Classic_Movement(Movement):
    Level_Parameters = {
        1 : {"StaminaCost" : 2, "UpgradeExpCost" : 10, "speed" : 3, "dodge_alteration" : 0},
        2 : {"StaminaCost" : 2, "UpgradeExpCost" : 20, "speed" : 4, "dodge_alteration" : 0}
    }
    def __init__(self, level: int):
        super().__init__("Classic_Movement"+"-lv"+str(level), level=level, **Classic_Movement.Level_Parameters[level])
        
class Slow_Movement(Movement):
    Level_Parameters = {
        1 : {"StaminaCost" : 1, "UpgradeExpCost" : 10, "speed" : 1, "dodge_alteration" : 0.15},
        2 : {"StaminaCost" : 1, "UpgradeExpCost" : 20, "speed" : 1, "dodge_alteration" : 0.20}
    }
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
            potential_damage += fighter.leftTool 
        else : potential_damage += fighter.rightTool
        potential_damage = potential_damage * self.factor
        
        for target in targets:
            if self.name.startswith("Quick_Attack") or target.dodge() != True:
                target.take_damage(potential_damage)
        fighter.useSkill(self.name)
        
class Brutal_Attack(Attack):
    Level_Parameters = {
        1 : {"StaminaCost" : 4, "UpgradeExpCost" : 10,  "dodge_alteration" : -1,"damageFactor" : 2.25},
        2 : {"StaminaCost" : 4, "UpgradeExpCost" : 20, "dodge_alteration" : -1,"damageFactor" : 2.5}
    }
    def __init__(self, level : int):
        super().__init__("Brutal_Attack"+"-lv"+str(level),level=level, **Brutal_Attack.Level_Parameters[level])
        self.level = level
class Quick_Attack(Attack):
    Level_Parameters = {
        1 : {"StaminaCost" : 3, "UpgradeExpCost" : 10,  "dodge_alteration" : 0,"damageFactor" : 0.5},
        2 : {"StaminaCost" : 3, "UpgradeExpCost" : 20, "dodge_alteration" : 0,"damageFactor" : 0.5}
    }
    def __init__(self, level : int):
        super().__init__("Quick_Attack"+"-lv"+str(level),level=level, **Quick_Attack.Level_Parameters[level])
        self.level = level
class Classic_Attack(Attack):
    Level_Parameters = {
        1 : {"StaminaCost" : 2, "UpgradeExpCost" : 10,  "dodge_alteration" : 0,"damageFactor" : 1},
        2 : {"StaminaCost" : 2, "UpgradeExpCost" : 20, "dodge_alteration" : 0,"damageFactor" : 1}
    }
    def __init__(self, level : int):
        super().__init__("Classic_Attack"+"-lv"+str(level),level=level, **Classic_Attack.Level_Parameters[level])
        self.level = level
       
       
        
class Defense(Action):
    def __init__(self, action_name: str, StaminaCost: int, UpgradeExpCost: int, defensePoints : int, level:int, dodge_alteration : int):
        super().__init__(action_name, StaminaCost, UpgradeExpCost, level, dodge_alteration)        
        self.defensePoints = defensePoints
        
    def acts(self, fighter : fighter.CHARACTER, targets : List[fighter.CHARACTER], hand="left"):
        super(Defense,self).acts(fighter,targets)
        assert len(targets) == 1 and targets[0] == fighter
        fighter.defensePoints += self.defensePoints 

class Light_Defense(Defense):
    Level_Parameters = {
        1 : {"StaminaCost" : 3, "UpgradeExpCost" : 10,  "dodge_alteration" : 0,"defensePoints" : 1},
        2 : {"StaminaCost" : 3, "UpgradeExpCost" : 20, "dodge_alteration" : 0,"defensePoints" : 1}
    }
    def __init__(self, level : int):
        super().__init__("Light_Defense"+"-lv"+str(level),level=level, **Light_Defense.Level_Parameters[level])
    
class Stoical_Defense(Defense): # for stoical_Defense, damage is divided by the absolute value of defensePoints in fighter.py but it is the only action authorized for unit
    Level_Parameters = {
        1 : {"StaminaCost" : 3, "UpgradeExpCost" : 10,  "dodge_alteration" : -1,"defensePoints" : -3},
        2 : {"StaminaCost" : 3, "UpgradeExpCost" : 20, "dodge_alteration" : -1,"defensePoints" : -5}
    }
    def __init__(self, level : int):
        super().__init__("Stoical_Defense"+"-lv"+str(level),level=level, **Stoical_Defense.Level_Parameters[level])
   
        
class Classic_Defense(Defense):
    Level_Parameters = {
        1 : {"StaminaCost" : 3, "UpgradeExpCost" : 10,  "dodge_alteration" : 0,"defensePoints" : 4},
        2 : {"StaminaCost" : 3, "UpgradeExpCost" : 20, "dodge_alteration" : 0,"defensePoints" : 5}
    }
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

ABSTRACT = [Action, Attack, Defense, Movement]

                
if __name__ == '__main__':
    setupActions()
    #print(Action.ACTIONS_DICT)