
from typing import List, Tuple, Dict, Union
import fighter, player


class Action:
    ACTIONS_DICT = {}
    
    def __init__(self, action_name : str, StaminaCost: int, UpgradeExpCost : int):
        if action_name not in Action.ACTIONS_DICT.keys():
            Action.ACTIONS_DICT[action_name] = self
            self.name = action_name
            self.upgrades : List['Action'] = []
            self.staminaCost = StaminaCost
            self.upgradeExpCost = UpgradeExpCost
        else: raise Exception("Already Existing Action")
    
    def addUpgrade(self, upgrade: 'Action'):
        if upgrade not in self.upgrades:
            self.upgrades.append(upgrade)
            
    def acts(self, fighter : fighter.CHARACTER, targets : Union[Tuple[int,int], List[fighter.CHARACTER]], hand="left"):
        pass
    
    
    


class Movement(Action):
    def __init__(self, action_name: str, StaminaCost: int, UpgradeExpCost: int, speed : int, dodge_alteration :int):
        super().__init__(action_name, StaminaCost, UpgradeExpCost)
        self.speed = speed
        self.dodge_alter = dodge_alteration
    
    def acts(self, fighter : fighter.CHARACTER, targets : Tuple[int,int], hand="left"):
        pass # move fighter at target emplacement if possible

class Quick_Movement(Movement):
    Level_Parameters = {
        1 : {"StaminaCost" : 3, "UpgradeExpCost" : 10, "speed" : 5, "dodge_alteration" : -0.15},
        2 : {"StaminaCost" : 3, "UpgradeCost" : 25, "speed" : 8, "dodge_alteration" : -0.20}
    }
    def __init__(self, level: int):
        super().__init__("Quick_Movement"+"-lv"+str(level), **Quick_Movement.Level_Parameters[level])
        self.level = level
    
class Classic_Movement(Movement):
    Level_Parameters = {
        1 : {"StaminaCost" : 2, "UpgradeExpCost" : 10, "speed" : 3, "dodge_alteration" : 0},
        2 : {"StaminaCost" : 2, "UpgradeCost" : 20, "speed" : 4, "dodge_alteration" : 0}
    }
    def __init__(self, level: int):
        super().__init__("Classic_Movement"+"-lv"+str(level), **Classic_Movement.Level_Parameters[level])
        self.level = level
        
class Slow_Movement(Movement):
    Level_Parameters = {
        1 : {"StaminaCost" : 1, "UpgradeExpCost" : 10, "speed" : 1, "dodge_alteration" : 0.15},
        2 : {"StaminaCost" : 1, "UpgradeCost" : 20, "speed" : 1, "dodge_alteration" : 0.20}
    }
    def __init__(self, level: int):
        super().__init__("Slow_Movement"+"-lv"+str(level), **Slow_Movement.Level_Parameters[level])
        
        
        
        
class Attack(Action):
    def __init__(self, action_name: str, StaminaCost: int, UpgradeExpCost: int, damageFactor : int):
        super().__init__(action_name, StaminaCost, UpgradeExpCost)
        self.factor = damageFactor
        
    def acts(self, fighter : fighter.CHARACTER, targets : List[fighter.CHARACTER], hand="left"):
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
        2 : {"StaminaCost" : 4, "UpgradeCost" : 20, "dodge_alteration" : -1,"damageFactor" : 2.5}
    }
    def __init__(self, level : int):
        super().__init__("Brutal_Attack"+"-lv"+str(level), **Brutal_Attack.Level_Parameters[level])
        
class Quick_Attack(Attack):
    Level_Parameters = {
        1 : {"StaminaCost" : 3, "UpgradeExpCost" : 10,  "dodge_alteration" : 0,"damageFactor" : 0.5},
        2 : {"StaminaCost" : 3, "UpgradeCost" : 20, "dodge_alteration" : 0,"damageFactor" : 0.5}
    }
    def __init__(self, level : int):
        super().__init__("Quick_Attack"+"-lv"+str(level), **Quick_Attack.Level_Parameters[level])
        
class Classic_Attack(Attack):
    Level_Parameters = {
        1 : {"StaminaCost" : 2, "UpgradeExpCost" : 10,  "dodge_alteration" : 0,"damageFactor" : 1},
        2 : {"StaminaCost" : 2, "UpgradeCost" : 20, "dodge_alteration" : 0,"damageFactor" : 1}
    }
    def __init__(self, level : int):
        super().__init__("Classic_Attack"+"-lv"+str(level), **Classic_Attack.Level_Parameters[level])
       
       
       
        
class Defense(Action):
    def __init__(self, action_name: str, StaminaCost: int, UpgradeExpCost: int, defensePoints : int):
        super().__init__(action_name, StaminaCost, UpgradeExpCost)        
        

class Light_Defense(Defense):
    def __init__(self, action_name: str, StaminaCost: int, UpgradeExpCost: int):
        super().__init__(action_name, StaminaCost, UpgradeExpCost)
        
class Stoical_Defense(Defense):
    def __init__(self, action_name: str, StaminaCost: int, UpgradeExpCost: int):
        super().__init__(action_name, StaminaCost, UpgradeExpCost)
        
class Classic_Defense(Defense):
    def __init__(self, action_name: str, StaminaCost: int, UpgradeExpCost: int):
        super().__init__(action_name, StaminaCost, UpgradeExpCost)
    
    
    

