import armors, items, weapons
from typing import List, Union



class FIGHTER:
    def __init__(self, _name, gold = 0, _HP:int =20, _MaxHP:int =20, _Stamina:int =5, _magic:int =0, _stamina_regeneration:int =5, _race :str = "Human",  _Equipment: List[items.ITEM] = [], _Inventory: List[items.ITEM] = []):
        self.HP = _HP
        self.MaxHP = _MaxHP
        self.stamina = _Stamina
        self.magic = _magic
        self.stamina_regeneration = _stamina_regeneration
        self.equipment = _Equipment
        self.inventory = _Inventory
        self.race = _race
        self.name = _name
        self.money = gold
        
    def equip(self, stuff : Union[armors.ARMOR, weapons.WEAPON]):
        self.equipment.append(stuff)
        
    def get_item(self, stuff : items.ITEM):
        self.equipment.append(stuff)