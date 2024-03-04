import fighter, rules, player
from typing import Dict

TERMINAL = 0

MOD = TERMINAL

def askFor(something:str, mod=MOD):
    if mod == TERMINAL:
        return input(something)
    return ""

def throwError(someError:str, mod=MOD):
    if mod == TERMINAL:
        print(someError)
        
def getPlayerActions(player : player.Player, units : Dict[str:fighter.CHARACTER], mod=MOD):
    if mod == TERMINAL:
        finished = False
        Actions = []
        while finished == False:
            try:
                Actions = []
                strActions = input("Expected Format: action1 on fighter1 ; action2 on fighter2 ; ...")
                parsedActions = strActions.split(" ; ")
                for strAction in parsedActions:
                    [actionName, fighterName] = strAction.split(" on ")
                    if actionName not in rules.ACTIONS_NAMES.keys():
                        print("given Action Name: "+actionName+" do not exist")
                        raise Exception()
                    if fighterName not in units.keys():
                        print("given fighter name"+fighterName+" do not exist")
                        raise Exception()
                    Actions.append(rules.Action(rules.ACTIONS_NAMES[actionName], player, units[fighterName]))
                    
                
            except Exception as e:
                continue
    return Actions
    