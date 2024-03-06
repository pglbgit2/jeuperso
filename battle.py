import fighter, rules, action, player, interaction
from typing import List, Dict, Union, Tuple

class Battle:
    def __init__(self, fighters : List[fighter.CHARACTER]):
        if action.Action.ACTIONS_DICT == {}:
            action.setupActions()
        self.fighters = fighters
        self.fightersNames : List[str] = []
        self.factionsWarriors : Dict[List[str]] = {}
        for fighter in fighters:
            self.fightersNames.append(fighter.name)
            if fighter.faction not in self.factionsWarriors.keys():
                self.factionsWarriors[fighter.faction] = []   
            self.factionsWarriors[fighter.faction].append(fighter.name)
    
    def beginTurn(self):
        map(lambda x: x.newTurn(),self.fighters)    
        
    
    def checkValidity(self, fighter : fighter.CHARACTER, actions : List[Dict[str:Union[str,Tuple[int,int]]]], alliesName : List[str]):
        for someAction in actions:
            if "Stoical_Defense" == someAction and len(actions) > 1:
                interaction.throwError("Can not use Stoical_defense and other action in same turn")
                return False
            if "Attack" in someAction["name"] and any(someAction["target"] == allyName for allyName in alliesName):
                interaction.throwError("Can not attack ally")
                return False
            if someAction["name"] not in action.Action.ACTIONS_DICT.keys():
                interaction.throwError("Using an action "+someAction["name"]+" that does not exist")
                return False
            if someAction["name"] == "Equip":
                if not any(someAction["object"] == stuff for stuff in fighter.inventory):
                    interaction.throwError("Using an item that player do not possess")
                    return False
        return True
                
        

    
    def prepareActions(self):
        for fighter in self.fighters:
            actionValidated = False
            while not actionValidated : 
                actions = fighter.setUpActions(self.fightersNames)
                for someAction in actions:
                    someAction+=fighter.getStrLevelOfSkill(someAction["name"])
                actionValidated = not isinstance(fighter, player.Player) or self.checkValidity(fighter, actions, self.factionsWarriors[fighter.faction])
            fighter.actions = actions
    
    
    def executeActions(self):
        for fighter in rules.getTurnPriority(self.fighters):
            pass
    
    def turn(self):
        self.beginTurn()
        self.prepareActions()
        self.executeActions()