import items, interaction, math, copy, races, os,json
from typing import Dict
from inspect import signature


## DEFAULT CHAIN_MAIL ATTRIBUTES ##

CHAIN_MAIL_DURABILITY = 50
CHAIN_MAIL_WEIGHT = 40
CHAIN_MAIL_COST = 70
CHAIN_MAIL_ABSORPTION = {
    "blade" : 0.6,
    "pierce" : 0.6,
    "impact" : 0.4
}
CHAIN_MAIL = {"weight" : CHAIN_MAIL_WEIGHT, "durability" : CHAIN_MAIL_DURABILITY, "cost" : CHAIN_MAIL_COST, "absorption" : CHAIN_MAIL_ABSORPTION}


## DEFAULT LEATHER_LEATHER_HELMET ATTRIBUTES ##

LEATHER_HELMET_DURABILITY = 27
LEATHER_HELMET_WEIGHT = 15
LEATHER_HELMET_COST = 30
LEATHER_HELMET_ABSORPTION = {
    "blade" : 0.3,
    "pierce" : 0.3,
    "impact" : 0.3,
    "cold" : 0.1
}
LEATHER_HELMET = {"weight" : LEATHER_HELMET_WEIGHT, "durability" : LEATHER_HELMET_DURABILITY, "cost" : LEATHER_HELMET_COST, "absorption" : LEATHER_HELMET_ABSORPTION}


## DEFAULT IRON_HELMET ATTRIBUTES ##

IRON_HELMET_DURABILITY = 35
IRON_HELMET_WEIGHT = 27
IRON_HELMET_COST = 45
IRON_HELMET_ABSORPTION = {
    "blade" : 0.5,
    "pierce" : 0.6,
    "impact" : 0.4
}
IRON_HELMET = {"weight" : IRON_HELMET_WEIGHT, "durability" : IRON_HELMET_DURABILITY, "cost" : IRON_HELMET_COST, "absorption" : IRON_HELMET_ABSORPTION}


## DEFAULT STEEL_HELMET ATTRIBUTES ##

STEEL_HELMET_DURABILITY = 45
STEEL_HELMET_WEIGHT = 39
STEEL_HELMET_COST = 70
STEEL_HELMET_ABSORPTION = {
    "blade" : 0.8,
    "pierce" : 0.9,
    "impact" : 0.6,
}
STEEL_HELMET = {"weight" : STEEL_HELMET_WEIGHT, "durability" : STEEL_HELMET_DURABILITY, "cost" : STEEL_HELMET_COST, "absorption" : STEEL_HELMET_ABSORPTION}



## DEFAULT LEATHER_LP ATTRIBUTES ##

LEATHER_LP_DURABILITY = 22
LEATHER_LP_WEIGHT = 20
LEATHER_LP_COST = 30
LEATHER_LP_ABSORPTION = {
    "blade" : 0.3,
    "pierce" : 0.3,
    "impact" : 0.3,
    "cold" : 0.1
}
LEATHER_LP = {"weight" : LEATHER_LP_WEIGHT, "durability" : LEATHER_LP_DURABILITY, "cost" : LEATHER_LP_COST, "absorption" : LEATHER_LP_ABSORPTION}


## DEFAULT IRON_LP ATTRIBUTES ##

IRON_LP_DURABILITY = 33
IRON_LP_WEIGHT = 24
IRON_LP_COST = 45
IRON_LP_ABSORPTION = {
    "blade" : 0.5,
    "pierce" : 0.6,
    "impact" : 0.4
}
IRON_LP = {"weight" : IRON_LP_WEIGHT, "durability" : IRON_LP_DURABILITY, "cost" : IRON_LP_COST, "absorption" : IRON_LP_ABSORPTION}

## DEFAULT STEEL_LP ATTRIBUTES ##

STEEL_LP_DURABILITY = 47
STEEL_LP_WEIGHT = 37
STEEL_LP_COST = 60
STEEL_LP_ABSORPTION = {
    "blade" : 0.8,
    "pierce" : 0.8,
    "impact" : 0.6
}
STEEL_LP = {"weight" : STEEL_LP_WEIGHT, "durability" : STEEL_LP_DURABILITY, "cost" : STEEL_LP_COST, "absorption" : STEEL_LP_ABSORPTION}



## DEFAULT PADDED_ARMOR ATTRIBUTES ##

PADDED_ARMOR_DURABILITY = 35
PADDED_ARMOR_WEIGHT = 28
PADDED_ARMOR_COST = 40
PADDED_ARMOR_ABSORPTION = {
    "blade" : 0.3,
    "pierce" : 0.3,
    "impact" : 0.3,
    "cold" : 0.1
}
PADDED_ARMOR = {"weight" : PADDED_ARMOR_WEIGHT, "durability" : PADDED_ARMOR_DURABILITY, "cost" : PADDED_ARMOR_COST, "absorption" : PADDED_ARMOR_ABSORPTION}


## DEFAULT SCALE_ARMOR ATTRIBUTES ##

SCALE_ARMOR_DURABILITY = 45
SCALE_ARMOR_WEIGHT = 35
SCALE_ARMOR_COST = 50
SCALE_ARMOR_ABSORPTION = {
    "blade" : 0.50,
    "pierce" : 0.40,
    "impact" : 0.40,
    "fire" : 0.30,
}
SCALE_ARMOR = {"weight" : SCALE_ARMOR_WEIGHT, "durability" : SCALE_ARMOR_DURABILITY, "cost" : SCALE_ARMOR_COST, "absorption" : SCALE_ARMOR_ABSORPTION}


## DEFAULT PLATE_ARMOR ATTRIBUTES ##

PLATE_ARMOR_DURABILITY = 60
PLATE_ARMOR_WEIGHT = 50
PLATE_ARMOR_COST = 90
PLATE_ARMOR_ABSORPTION = {
    "blade" : 1,
    "pierce" : 1,
    "impact" : 0.9
}
PLATE_ARMOR = {"weight" : PLATE_ARMOR_WEIGHT, "durability" : PLATE_ARMOR_DURABILITY, "cost" : PLATE_ARMOR_COST, "absorption" : PLATE_ARMOR_ABSORPTION}




DEFAULT_ABSORPTION = races.DEFAULT_RESISTANCE

# ARMOR TYPES #

BODY = ["CHAIN_MAIL","PLATE_ARMOR","SCALE_ARMOR","PADDED_ARMOR"]

HEAD = ["LEATHER_HELMET","IRON_HELMET","STEEL_HELMET"]

#LP stands for LEG PROTECTOR
LEGS = ["LEATHER_LP","IRON_LP","STEEL_LP"]
ARMORS = BODY+HEAD+LEGS

class ARMOR(items.ITEM):
    def __init__(self,name:str, cost : int, weight : int, durability : int, absorption : Dict[str,int], maxDurability=-1):
        super().__init__(name,cost,weight)
        if maxDurability == -1:
            self.maxDur = durability
        else:
            self.maxDur = maxDurability
        self.absorption = copy.copy(DEFAULT_ABSORPTION)
        self.absorption.update(absorption)
        self.durability = durability
    
    @staticmethod
    def get_armor_from_file(armor_name):
        directory = "armors"
        target_file = f"{armor_name}.json"
        for root, dirs, files in os.walk(directory):
            if target_file in files:
                file_path = os.path.join(root, target_file)
                with open(file_path, 'r', encoding='utf-8') as file:
                    armor = json.load(file)
                    if "categories" in armor.keys():
                        categories = armor["categories"]
                        del armor['categories']
                    class_args = signature(ARMOR).parameters.keys()
                    if all(key in armor for key in class_args):
                        for category in categories:
                            if category in globals().keys() and type(globals()[category]) is list:
                                Category = globals()[category]
                                if armor["name"] not in Category:
                                    Category.append(armor["name"])
                        instance = ARMOR(**armor)
                        return instance
                    else:
                        print("Keys do not match the class constructor arguments.")
                        return None
    
    
    
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
            
#print(ARMOR.get_armor_from_file("CHAIN_MAIL").durability)