import defaultSkills
import fighter, interaction
import armors, items, weapons
from typing import List, Union

class Player(fighter.CHARACTER):
    def __init__(self, name:str, faction:str, gold:int = 0, HP:int =20, MaxHP:int =20, Stamina:int =5, magic:int =0, stamina_regeneration:int =5, race :str = "Human",  Equipment: List[Union[armors.ARMOR, weapons.WEAPON, weapons.RANGE_WEAPON]] = [], Inventory: List[items.ITEM] = [], skills : List[str] = defaultSkills.DEFAULT_SKILLS):
        super().__init__(name,faction,gold,HP,MaxHP,Stamina, magic,  stamina_regeneration, race, Equipment, Inventory, skills)
        self.actionCounter = {skillName : 0 for skillName in skills}

    
    def getInitiative(self):
        return interaction.askFor("Roll 1d100 dice for Initiative, Give result")
        
   
    def addSkill(self, skill:str):
        if skill not in self.skills:
            self.skills.append(skill)
            self.actionCounter[skill] = 0
                    
    def useSkill(self,skill:str):
        self.actionCounter[skill] += 1
        
    def dodge(self,modification=0):
        return interaction.askFor("Roll 1d100 dice for Dodging, Give result")