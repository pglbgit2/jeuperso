import armors, items, weapons, races
from typing import List, Union, Type


FACTIONS = ["Heroes","Bandits","City"]

class FIGHTER:
    def __init__(self, name:str, faction:str, gold:int = 0, HP:int =20, MaxHP:int =20, Stamina:int =5, magic:int =0, stamina_regeneration:int =5, race :str = "Human",  Equipment: List[Union[armors.ARMOR, weapons.WEAPON, weapons.RANGE_WEAPON]] = [], Inventory: List[items.ITEM] = []):
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
        self.weight = 0
        
    def max_weight(self):
        return self.stamina*30
        
    def equip(self, stuff : Union[armors.ARMOR, weapons.WEAPON, weapons.RANGE_WEAPON]):
        if stuff in self.inventory and stuff not in self.equipment:
            self.equipment.append(stuff)
    
    def total_weight(self):
        if self.weight == 0:
            for item in self.inventory:
                self.weight += item.weight
        return self.weight
    
    def get_speed(self):
        return self.max_weight() - self.total_weight()
            
    def put_into_inventory(self, stuff : items.ITEM):
        if self.total_weight() <= self.max_weight() and stuff not in self.inventory:
            self.inventory.append(stuff)
            self.weight += stuff.weight
    
    def lootAll(self, loot: List[items.ITEM]):
        for item in loot:
            self.put_into_inventory(item)
        
        
    @staticmethod
    def instantiate_from_race(race:str, name:str, faction: str):
        if race in races.RACES:
            Race = getattr(races, race)
            return FIGHTER(name = name, faction = faction, **Race)
        
#billy = FIGHTER.instantiate_from_race("HUMAN", "billy", "team1")
