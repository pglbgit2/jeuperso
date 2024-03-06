from typing import Dict, List
import ast, re

TERMINAL = 0
MOVEMENT = 0
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

def getPlayerActions(playerName : str, units_name : List[str], valid_actions : List[str], mod=MOD):
    if mod == TERMINAL:
        finished = False
        Actions = []
        while finished == False:
            try:
                Actions = []
                allActionsInserted = False
                leftHandUsed = False
                rightHandUsed = False
                while not allActionsInserted:
                    actionName = input("Action Name")
                    if actionName not in valid_actions:
                        raise Exception("given actionName is not valid")
                    
                    if "Equip" in actionName:
                        objectToEquip = input("Name of Object to equip")
                        Actions.append({"name" : actionName, "target" : playerName, "object" : objectToEquip})
                        continue
                    if "Movement" in actionName:
                        if MOVEMENT == 1:
                            strCoordinates = input("Destination")
                            if not is_valid_tuple_string(strCoordinates):
                                raise Exception('given tuple is not valid')
                            Actions.append({"name" : actionName, "target" : ast.literal_eval(strCoordinates)})
                        else:
                            Actions.append({"name" : actionName, "target" : (-1,-1)})
                        continue        
                    
                    if "Defense" in actionName:
                        Actions.append({"name" : actionName, "target" : playerName})
                        continue
                    if "Attack" in actionName:
                        target = input("Targets Name: target1, target2, ...")
                        if ", " in target:
                            fightersName = target.split(", ")
                        else: fightersName = [target]
                        
                        for fighterName in fightersName:
                            if fighterName not in units_name:
                                raise Exception("given fighter name"+fighterName+" do not exist")                        
                        hand = input("Used Hand to attack")
                        if hand == "left":
                            if leftHandUsed == False:
                                leftHandUsed = True
                                Actions.append({"name" : actionName, "target" : fightersName, "hand" : hand})
                                continue
                            else: raise Exception("Left hand already used")
                        if hand == "right":
                            if rightHandUsed == False:
                                rightHandUsed = True
                finished = True                    
            except Exception as e:
                throwError(e.args[0])
                continue
    return Actions
    