import armors, items, weapons, races
from typing import List, Union


FACTIONS = []

class FIGHTER:
    def __init__(self, name:str, faction:str, gold:int = 0, HP:int =20, MaxHP:int =20, Stamina:int =5, magic:int =0, stamina_regeneration:int =5, race :str = "Human",  Equipment: List[Union[armors.ARMOR, weapons.WEAPON]]= [], Inventory: List[items.ITEM] = []):
        self.HP = HP
        self.MaxHP = MaxHP
        self.stamina = Stamina
        self.magic = magic
        self.stamina_regeneration = stamina_regeneration
        self.equipment = Equipment
        self.inventory = Inventory
        self.race = race
        self.name = name
        self.money = gold
        self.faction = faction
        
    def equip(self, stuff : Union[armors.ARMOR, weapons.WEAPON]):
        self.equipment.append(stuff)
        
    def get_item(self, stuff : items.ITEM):
        self.equipment.append(stuff)
        
    @staticmethod
    def instantiate_from_race(race:str, name:str, faction: str):
        if race in races.RACES:
            Race = getattr(races, race)
            return FIGHTER(name = name, faction= faction, **Race)
        
#billy = FIGHTER.instantiate_from_race("HUMAN", "billy", "team1")
