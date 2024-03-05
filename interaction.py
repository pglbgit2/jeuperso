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
                strActions = input("Expected Format: action1 on fighter1, fighter2 ; action2 on fighter2 ; action3 on (x,y) ...")
                parsedActions = strActions.split(" ; ")
                for strAction in parsedActions:
                    [actionName, target] = strAction.split(" on ")
                    if not strAction.startswith("("):
                        fightersName = target.split(", ")
                        for fighterName in fightersName:
                            if fighterName not in units.keys():
                                print("given fighter name"+fighterName+" do not exist")
                                raise Exception()
                    else:
                        coordonates = strAction()
                    if actionName not in rules.ACTIONS_NAMES.keys():
                        print("given Action Name: "+actionName+" do not exist")
                        raise Exception()
                    
                    
                    
                finished = True                    
            except Exception as e:
                continue
    return Actions
    