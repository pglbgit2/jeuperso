from typing import Dict, List
import ast, re

TERMINAL = 0

MOD = TERMINAL

def askFor(something:str, mod=MOD):
    if mod == TERMINAL:
        return input(something)
    return ""

def throwError(someError:str, mod=MOD):
    if mod == TERMINAL:
        print(someError)
        
def is_valid_tuple_string(s:str):
    pattern = r'^\(\s*\d+\s*,\s*\d+\s*\)$'
    return re.match(pattern, s) is not None

def getPlayerActions(units_name : List[str], valid_actions : List[str], mod=MOD):
    if mod == TERMINAL:
        finished = False
        Actions = []
        while finished == False:
            try:
                Actions = []
                strActions = input("Expected Format: action1 on fighter1, fighter2 ; action2 on fighter2 ; action3 on (x,y) ; ...")
                parsedActions = strActions.split(" ; ")
                for strAction in parsedActions:
                    [actionName, target] = strAction.split(" on ")
                    if actionName not in valid_actions:
                        raise Exception("given actionName is not valid")
                    if not target.startswith("("):
                        fightersName = target.split(", ")
                        for fighterName in fightersName:
                            if fighterName not in units_name:
                                raise Exception("given fighter name"+fighterName+" do not exist")
                        Actions.append({"name" : actionName, "target" : fightersName})
                    else:
                        if not is_valid_tuple_string(target):
                            raise Exception('given tuple is not valid')
                        Actions.append({"name" : actionName, "target" : ast.literal_eval(target)})
                finished = True                    
            except Exception as e:
                continue
    return Actions
    