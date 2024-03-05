
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
            
    def acts(self, fighter : fighter.CHARACTER, context : Union[Dict[Tuple[int,int] : fighter.CHARACTER], fighter.CHARACTER], targets : Union[List[Tuple[int,int]], fighter.CHARACTER]):
        pass
    
    
    


class Movement(Action):
    def __init__(self, action_name: str, StaminaCost: int, UpgradeExpCost: int):
        super().__init__(action_name, StaminaCost, UpgradeExpCost)
    

class Quick_Movement(Movement):
    Level_Parameters = {
        1 : {"StaminaCost" : 3, "UpgradeExpCost" : 10},
        2 : {"StaminaCost" : 3, "UpgradeCost" : 15}
    }
    def __init__(self, level: int):
        super().__init__("Quick_Movement"+"-lv"+str(level), **Quick_Movement.Level_Parameters[level])
    
class Classic_Movement(Movement):
    def __init__(self, action_name: str, StaminaCost: int, UpgradeExpCost: int):
        super().__init__(action_name, StaminaCost, UpgradeExpCost)
        
class Slow_Movement(Movement):
    def __init__(self, action_name: str, StaminaCost: int, UpgradeExpCost: int):
        super().__init__(action_name, StaminaCost, UpgradeExpCost)
        
        
        
        
class Attack(Action):
    def __init__(self, action_name: str, StaminaCost: int, UpgradeExpCost: int):
        super().__init__(action_name, StaminaCost, UpgradeExpCost)

class Brutal_Attack(Attack):
    def __init__(self, action_name: str, StaminaCost: int, UpgradeExpCost: int):
        super().__init__(action_name, StaminaCost, UpgradeExpCost)
        
class Quick_Attack(Attack):
    def __init__(self, action_name: str, StaminaCost: int, UpgradeExpCost: int):
        super().__init__(action_name, StaminaCost, UpgradeExpCost)
    
class Classic_Attack(Attack):
    def __init__(self, action_name: str, StaminaCost: int, UpgradeExpCost: int):
        super().__init__(action_name, StaminaCost, UpgradeExpCost)
       
       
       
        
class Defense(Action):
    def __init__(self, action_name: str, StaminaCost: int, UpgradeExpCost: int):
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
    
    
    

