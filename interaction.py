from typing import List
import ast, re
import textwrap
from fpdf import FPDF

TERMINAL = 1
MOVEMENT = 0
MOD = TERMINAL
if MOD == TERMINAL:
    import readline
    
def askFor(something:str, mod=MOD):
    if mod == TERMINAL:
        return input(something)
    return ""

def askForInt(something:str, mod=MOD):
    if mod == TERMINAL:
        someInteger = ""
        while someInteger == "" or not someInteger.isdecimal():
            someInteger = input(something)
        return someInteger

def throwError(someError:str, mod=MOD):
    if mod == TERMINAL:
        print(someError)

def showInformation(someInfo : str, mod=MOD):
    if mod == TERMINAL:
        print(someInfo)
        
def is_valid_tuple_string(s:str):
    pattern = r'^\(\s*\d+\s*,\s*\d+\s*\)$'
    return re.match(pattern, s) is not None



def text_to_pdf(text, filename):
    a4_width_mm = 210
    pt_to_mm = 0.35
    fontsize_pt = 10
    fontsize_mm = fontsize_pt * pt_to_mm
    margin_bottom_mm = 10
    character_width_mm = 7 * pt_to_mm
    width_text = a4_width_mm / character_width_mm

    pdf = FPDF(orientation='P', unit='mm', format='A4')
    pdf.set_auto_page_break(True, margin=margin_bottom_mm)
    pdf.add_page()
    pdf.set_font(family='Courier', size=fontsize_pt)
    splitted = text.split('\n')

    for line in splitted:
        lines = textwrap.wrap(line, width_text)

        if len(lines) == 0:
            pdf.ln()

        for wrap in lines:
            pdf.cell(0, fontsize_mm, wrap, ln=1)

    pdf.output(filename, 'F')   


def getStrInList(strList:List[str],subject):
    result = None
    possibilities = ""
    for element in strList:
        possibilities += element+", "
    possibilities = possibilities[:-2]
    while not result in strList:
        print("Please enter "+subject+" in "+possibilities+"\n")
        result = input("> ")
        for element in strList:
            if element.startswith(result):
                print(element, end="")
                val =  input("\n confirm ? (y or n)")
                if val == "y":
                    return element
                else: continue
    return result

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
                    print("Actions input of "+playerName+"\n")
                    actionName = getStrInList(list(valid_actions)+["end"], "Action Name")
                    #actionName = input("Action Name among+"+str(valid_actions)+" or end to stop\n")
                    if actionName == "end":
                        allActionsInserted = True
                        break
                    if actionName not in valid_actions:
                        raise Exception("given actionName is not valid")
                                            
                    if "useConsumable" == actionName:
                        consumable = input("Name of consumable")
                        Actions.append({"name":actionName, "target" : consumable})
                    
                    if "Equip" == actionName:
                        objectToEquip = input("Name of Object to equip\n")
                        hand = input("hand : left or right or none \n")
                        Actions.append({"name" : actionName, "target" : playerName, "object" : objectToEquip, "hand":hand})
                        continue
                    if "Movement" in actionName:
                        if MOVEMENT == 1:
                            strCoordinates = input("Destination\n")
                            if not is_valid_tuple_string(strCoordinates):
                                raise Exception('given tuple is not valid')
                            Actions.append({"name" : actionName, "target" : ast.literal_eval(strCoordinates)})
                        else:
                            Actions.append({"name" : actionName, "target" : (-1,-1)})
                        continue        
                    
                    if "Defense" in actionName:
                        Actions.append({"name" : actionName, "target" : playerName})
                        continue
                    
                    if "Attack" in actionName or "Shot" in actionName or "Melee_Combat" == actionName:
                        print("All potential targets:"+str(units_name)+"\n")
                        target = input("Targets Name\n")
                        if ", " in target:
                            fightersName = target.split(", ")
                        else: fightersName = [target]
                        
                        for fighterName in fightersName:
                            if fighterName not in units_name:
                                raise Exception("given fighter name"+fighterName+" do not exist")   
                        action = {"name" : actionName, "targets" : fightersName}
                        if actionName != "Melee_Combat":         
                            hand = input("Used Hand to attack: left or right\n")
                            if hand == "left":
                                if leftHandUsed == False:
                                    leftHandUsed = True
                                else: raise Exception("Left hand already used")
                            if hand == "right":
                                if rightHandUsed == False:
                                    rightHandUsed = True
                                    if not isinstance(fightersName, List):
                                        fightersName = [fightersName]
                                else: raise Exception("Right hand already used")
                            if hand != "left" and hand != "right":
                                raise Exception("Not correct hand")
                            action["hand"] = hand
                        Actions.append(action)

                finished = True                    
            except Exception as e:
                throwError(e.args[0])
                continue
    return Actions
    