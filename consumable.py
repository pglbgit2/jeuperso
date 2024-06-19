import items, interaction
from typing import Dict, Union, Tuple



HEALTH_POTION_WEIGHT = 4
HEALTH_POTION_COST = 20
HEALTH_POTION = {"weight" : HEALTH_POTION_WEIGHT, "cost" : HEALTH_POTION_COST, "effect":{"Health":(5,12)}}


ANTIDOTE_WEIGHT = 4
ANTIDOTE_COST = 8
ANTIDOTE = {"weight" : ANTIDOTE_WEIGHT, "cost" : ANTIDOTE_COST, "effect":{"Treat":1}}

POISON_WEIGHT = 4
POISON_COST = 10
POISON = {"weight" : POISON_WEIGHT, "cost" : POISON_COST, "effect":{"Poison":1}}


class Consumable(items.ITEM):
    def __init__(self, name:str, cost:int, weight:int, effect:Dict[str,Union[int,str,Tuple[int]]]):
        super().__init__(name,cost,weight)
        self.effect = effect
        
    def canHeal(self):
        return "Health" in self.effect.keys() and self.effect["Health"][1] > 0
    
    @staticmethod
    def get_consumable(item_name):
        if item_name in globals():
            item = globals()[item_name]
            return Consumable(name=item_name, **item)
        else:
            interaction.throwError("No item with such name")
            return None
        
CONSUMABLE = ["HEALTH_POTION", "POISON", "ANTIDOTE"]