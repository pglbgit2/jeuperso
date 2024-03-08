import items, interaction, math
from typing import Dict


## DEFAULT CHAIN_MAIL ATTRIBUTES ##

CHAIN_MAIL_DURABILITY = 50
CHAIN_MAIL_WEIGHT = 30
CHAIN_MAIL_COST = 40
CHAIN_MAIL_ABSORPTION = {
    "blade" : 0.1,
    "pierce" : 0.1,
    "impact" : 0.05,
    "fire" : 0,
    "cold" : 0,
    "arcane" : 0
}
CHAIN_MAIL = {"weight" : CHAIN_MAIL_WEIGHT, "durability" : CHAIN_MAIL_DURABILITY, "cost" : CHAIN_MAIL_COST, "absorption" : CHAIN_MAIL_ABSORPTION}


## DEFAULT LEATHER_LEATHER_HELMET ATTRIBUTES ##

LEATHER_HELMET_DURABILITY = 27
LEATHER_HELMET_WEIGHT = 15
LEATHER_HELMET_COST = 30
LEATHER_HELMET_ABSORPTION = {
    "blade" : 0.05,
    "pierce" : 0.05,
    "impact" : 0.05,
    "fire" : 0,
    "cold" : 0,
    "arcane" : 0
}
LEATHER_HELMET = {"weight" : LEATHER_HELMET_WEIGHT, "durability" : LEATHER_HELMET_DURABILITY, "cost" : LEATHER_HELMET_COST, "absorption" : LEATHER_HELMET_ABSORPTION}


## DEFAULT LEATHER_LP ATTRIBUTES ##

LEATHER_LP_DURABILITY = 22
LEATHER_LP_WEIGHT = 20
LEATHER_LP_COST = 30
LEATHER_LP_ABSORPTION = {
    "blade" : 0.05,
    "pierce" : 0.05,
    "impact" : 0.05,
    "fire" : 0,
    "cold" : 0,
    "arcane" : 0
}
LEATHER_LP = {"weight" : LEATHER_LP_WEIGHT, "durability" : LEATHER_LP_DURABILITY, "cost" : LEATHER_LP_COST, "absorption" : LEATHER_LP_ABSORPTION}



# ARMOR TYPES #

BODY = ["CHAIN_MAIL"]

HEAD = ["LEATHER_HELMET"]

#LP stands for LEG PROTECTOR
LEGS = ["LEATHER_LP"]


class ARMOR(items.ITEM):
    def __init__(self,name:str, cost : int, weight : int, durability : int, absorption : Dict[str,int]):
        super().__init__(name,cost,weight)
        self.maxDur = durability
        self.absorption = absorption
        self.durability = durability
        
    @staticmethod
    def get_armor(armor_name):
        if armor_name in globals():
            armor = globals()[armor_name]
            return ARMOR(name=armor_name,**armor)
        else:
            interaction.throwError("No armor with such name")
            return None
        
    def damage_absorption(self, damage:int, damage_type : str):
        absorbed = math.ceil(self.absorption[damage_type]*damage)
        if absorbed > damage:
            absorbed = damage
        if absorbed > self.durability:
            absorbed = self.durability
        self.durability -= absorbed
        interaction.showInformation(self.name+" has absorbed "+str(absorbed)+" remaining durability:"+str(self.durability))
        return damage - absorbed
        
    
    def repair(self, reparation):
        self.durability += reparation
        if self.durability > self.maxDur:
            self.durability = self.maxDur
            
            