import defaultSkills, fighter, interaction, armors, items, weapons, ast, races, copy
from typing import List, Union, Dict

class Player(fighter.CHARACTER):
    def __init__(self, name:str, faction:str, gold:int = 0, HP:int =20, MaxHP:int =20, Stamina:int =5, magic:int =0, stamina_regeneration:int =5, race :str = "Human",  Equipment: List[Union[armors.ARMOR, weapons.WEAPON, weapons.RANGE_WEAPON]] = [], Inventory: List[items.ITEM] = [], skills : List[str] = defaultSkills.DEFAULT_SKILLS, dodge : float = 0.15, skillsLevel : Union[Dict[str,int], str] = {}, shotBonus : float = 0, counter : Union[Dict[str,int],str]= {}, raceResistance : Dict[str,float] = races.DEFAULT_RESISTANCE):
        super().__init__(name,faction,gold,HP,MaxHP,Stamina, magic,  stamina_regeneration, race, Equipment, Inventory, skills,dodge, skillsLevel,shotBonus, raceResistance)
        self.actionCounter = {skillName : 0 for skillName in skills}
        if isinstance(counter,str):
            counter = ast.literal_eval(counter)
        self.actionCounter.update(counter)
    
    def getInitiative(self):
        result = "nope"
        while not result.isdigit():
            result = interaction.askFor(self.name+", roll 1d100 dice for Initiative, Give result")
        return int(result)
   
    def addSkill(self, skill:str):
        if super(fighter.CHARACTER,self).addSkill(skill):
            self.actionCounter[skill] = 0
                    
    def useSkill(self,skill:str):
        self.actionCounter[skill] += 1
        
    def dodge(self,modification=0):
        result = "nope"
        while not result.isdigit():
            result = interaction.askFor(self.name+", roll 1d100 dice for Dodging, Give result")
        print(self.dodgePercent)
        return int(result)/100 <= (self.dodgePercent + modification)
    
    def setUpActions(self, fightersByName : Dict[str, fighter.CHARACTER], teamEstimatedPower : Dict[str,int], fightersByFaction : Dict[str,List[fighter.CHARACTER]]):
        self.actions = interaction.getPlayerActions(self.name, fightersByName.keys(), self.skills)
        return self.actions      
    
    def getDictInfos(self):
        dictInfo = super().getDictInfos()
        dictInfo["counter"] = str(self.actionCounter)
        return dictInfo       
    
    @staticmethod
    def instantiate_from_dict(classAttributes : Dict, name : str, faction : str, race: str):
        if faction in fighter.FACTIONS:
            if race in races.RACES:
                Player.instantiateInventoryEquipment(classAttributes)
                Race = getattr(races, race)
                return Player(name = name, faction = faction, race=race, raceResistance=Race["raceResistance"], **classAttributes)
            else: 
                interaction.throwError("Race do not exist, create it and add it to race array")
        else: 
            interaction.throwError("faction do not exist")
            return None
        
        
    @staticmethod
    def instantiate_from_class(characterClass:str, name:str, faction: str, race:str):
        if characterClass in races.CLASSES:
            classAttributes = copy.copy(getattr(races, characterClass))
            return Player.instantiate_from_dict(classAttributes, name, faction, race)
        else : 
            interaction.throwError("Class do not exist, create it and add it to class array")
            return None
    

    @staticmethod
    def retrieveFighter(filename : str):
        path = "./characters/"+filename
        try:
            with open(path, "r") as file:
                NameLine = file.readline()[:-1]
                factionLine = file.readline()[:-1]
                raceLine = file.readline()[:-1]
                dictLine = file.readline()[:-1]
                if dictLine != None:
                    fighterDictStr = ast.literal_eval(dictLine)
                    file.close()
                    if isinstance(fighterDictStr, Dict):
                        return Player.instantiate_from_dict(name=NameLine, faction=factionLine, classAttributes=fighterDictStr, race=raceLine)
                    else:
                        return None
                else:
                    file.close()
                    return None
        except Exception as e:
            print(e.args)
            interaction.throwError("file "+filename+" do not exist or has not correct format")
        
# billy = Player.instantiate_from_class("CITY_GARD", "billy", "Heroes", "HUMAN")
# billy.actionCounter["Classic_Movement"] = 1
# billy.saveFighter("billy.sav")
# billy2 = Player.retrieveFighter("billy.sav")
# print(billy2.inventory)
# print(billy2.actionCounter)