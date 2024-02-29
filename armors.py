import items



## DEFAULT CHAIN_MAIL ATTRIBUTES ##

CHAIN_MAIL_DURABILITY = 50
CHAIN_MAIL_WEIGHT = 30
CHAIN_MAIL_COST = 40
CHAIN_MAIL_ABSORPTION = 5
CHAIN_MAIL = (CHAIN_MAIL_WEIGHT, CHAIN_MAIL_DURABILITY, CHAIN_MAIL_COST, CHAIN_MAIL_ABSORPTION)


## DEFAULT LEATHER_LEATHER_HELMET ATTRIBUTES ##

LEATHER_HELMET_DURABILITY = 27
LEATHER_HELMET_WEIGHT = 15
LEATHER_HELMET_COST = 30
LEATHER_HELMET_ABSORPTION = 1
LEATHER_HELMET = (LEATHER_HELMET_WEIGHT, LEATHER_HELMET_DURABILITY, LEATHER_HELMET_COST, LEATHER_HELMET_ABSORPTION)


## DEFAULT LEATHER_LP ATTRIBUTES ##

LEATHER_LP_DURABILITY = 22
LEATHER_LP_WEIGHT = 20
LEATHER_LP_COST = 30
LEATHER_LP_ABSORPTION = 2
LEATHER_LP = (LEATHER_LP_WEIGHT, LEATHER_LP_DURABILITY, LEATHER_LP_COST, LEATHER_LP_ABSORPTION)



# ARMOR TYPES #

BODY = ["CHAIN_MAIL"]

HEAD = ["LEATHER_HELMET"]

#LP stands for LEG PROTECTOR
LEGS = ["LEATHER_LP"]


class ARMOR(items.ITEM):
    def __init__(self, _cost : int, _weight : int, _max_durability : int, _max_absorption : int):
        super().__init__(_cost,_weight)
        self.maxDur = _max_durability
        self.maxAbs = _max_absorption
        self.durability = _max_durability
        
    @staticmethod
    def get_armor(armor_name):
        if armor_name in globals():
            (ARMOR_WEIGHT, ARMOR_DURABILITY, ARMOR_COST, ARMOR_ABSORPTION) = globals()[armor_name]
            return ARMOR(ARMOR_COST, ARMOR_WEIGHT, ARMOR_DURABILITY, ARMOR_ABSORPTION)
        else:
            print("No armor with such name")
            return None
        
    def damage_absorption(self, damage:int):
        toTake = max(damage - self.maxAbs,0)
        if self.durability > toTake:
            self.durability -= toTake
            damage -= toTake
        else: 
            damage -= self.durability
            self.durability = 0
    
    def repair(self, reparation):
        self.durability += reparation
        if self.durability > self.maxDur:
            self.durability = self.maxDur
            
            