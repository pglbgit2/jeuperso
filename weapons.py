import items, interaction

###### MELEE WEAPON ######
## DEFAULT SWORD ATTRIBUTES ##

SWORD_DAMAGE = 9
SWORD_WEIGHT = 20
SWORD_COST = 40 
SWORD_SPEED = 15
SWORD = {"damage" : SWORD_DAMAGE, "weight" : SWORD_WEIGHT, "cost" : SWORD_COST, "speed" : SWORD_SPEED, "type" : "blade"}

## DEFAULT KNIFE ATTRIBUTES ##

KNIFE_DAMAGE = 5
KNIFE_WEIGHT = 7
KNIFE_COST = 10
KNIFE_SPEED = 25
KNIFE = {"damage" : KNIFE_DAMAGE, "weight" : KNIFE_WEIGHT, "cost" : KNIFE_COST, "speed" : KNIFE_SPEED, "type" : "pierce"}

 
## DEFAULT LONG_SWORD ATTRIBUTES ##

LONG_SWORD_DAMAGE = 12
LONG_SWORD_WEIGHT = 35
LONG_SWORD_COST = 70
LONG_SWORD_SPEED = 5
LONG_SWORD = {"damage" : LONG_SWORD_DAMAGE, "weight" : LONG_SWORD_WEIGHT, "cost" : LONG_SWORD_COST, "speed" : LONG_SWORD_SPEED , "type" : "blade"}

## DEFAULT SPIKED_CLUB ATTRIBUTES ##

SPIKED_CLUB_DAMAGE = 7
SPIKED_CLUB_WEIGHT = 14
SPIKED_CLUB_COST = 15
SPIKED_CLUB_SPEED = 18
SPIKED_CLUB = {"damage" : SPIKED_CLUB_DAMAGE, "weight" : SPIKED_CLUB_WEIGHT, "cost" : SPIKED_CLUB_COST, "speed" : SPIKED_CLUB_SPEED, "type" : "impact"}


## SPEAR ##

SPEAR_DAMAGE = 6
SPEAR_WEIGHT = 12
SPEAR_COST = 20
SPEAR_SPEED = 12
SPEAR = {"damage" : SPEAR_DAMAGE,"weight" :  SPEAR_WEIGHT,"cost" : SPEAR_COST, "speed" : SPEAR_SPEED, "type" : "pierce"}

#### END OF MELEE WEAPON #####


## RANGE PROJECTILE ##

## IRON ARROW ##

ARROW_DAMAGE = 5
ARROW_WEIGHT = 0.2
ARROW_COST = 0.3
ARROW_SPEED = 20
ARROW = {"damage" : ARROW_DAMAGE, "weight" : ARROW_WEIGHT,"cost" : ARROW_COST, "type" : "pierce", "speed" : ARROW_SPEED}

## ROCK ##
ROCK_DAMAGE = 3
ROCK_WEIGHT = 0.7
ROCK_COST = 0
ROCK_SPEED = 10
ROCK = {"damage" : ROCK_DAMAGE, "weight" : ROCK_WEIGHT, "cost" : ROCK_COST, "type" : "impact", "speed" : ROCK_SPEED}

######################
## RANGE WEAPONS ##

## BOW ##

BOW_ACCURACY = 0.20
BOW_WEIGHT = 15
BOW_COST = 30
BOW_MUNITION = "ARROW"
BOW =  {"accuracy" : BOW_ACCURACY, "weight" : BOW_WEIGHT, "cost" : BOW_COST, "munition" : BOW_MUNITION}

## SLINGSHOT ##

SLINGSHOT_ACCURACY = 0.10
SLINGSHOT_WEIGHT = 9
SLINGSHOT_COST = 15
SLINGSHOT_MUNITION = "ROCK"
SLINGSHOT =  {"accuracy" : SLINGSHOT_ACCURACY, "weight" : SLINGSHOT_WEIGHT, "cost" : SLINGSHOT_COST, "munition" : SLINGSHOT_MUNITION}



######################


## GROUP DEFINITIONS ##

MELEE_WEAPONS = ["KNIFE", "SPEAR", "SWORD", "SPIKED_CLUB", "LONG_SWORD"]

THROWABLE = ["KNIFE", "ROCK", "SPEAR"]

RANGE_PROJECTILE = ["ARROW", "ROCK"]

RANGE_WEAPONS = ["BOW"]

ONE_HAND_WEAPONS = ["SWORD", "KNIFE"]

TWO_HAND_WEAPONS = ["BOW", "LONG_SWORD", "SPEAR"]

class WEAPON(items.ITEM):
    def __init__(self, name : str, cost : int, damage : int, weight : int, speed : int, type : str):
        super().__init__(name,cost,weight)
        self.damage = damage
        self.speed = speed
        self.damageType = type
        
    def upgrade(self, damage_boost : int):
        self.damage += damage_boost
    
    @staticmethod
    def get_melee_weapon(weapon_name):
     
        if weapon_name in globals().keys() and weapon_name in MELEE_WEAPONS:
            weapon = globals()[weapon_name]
            return WEAPON(name=weapon_name, **weapon)
        else:
            interaction.throwError("No Weapon with such name")
            return None
        
    @staticmethod
    def get_munition_weapon(weapon_name):
     
        if weapon_name in globals().keys() and weapon_name in RANGE_PROJECTILE:
            weapon = globals()[weapon_name]
            return WEAPON(name=weapon_name, **weapon)
        else:
            interaction.throwError("No Weapon with such name")
            return None
    
class RANGE_WEAPON(items.ITEM):
    def __init__(self, name, cost : int, accuracy : int, weight : int, munition : str):      
        super().__init__(name,cost,weight)
        self.accuracy = accuracy
        self.munition = munition
        
    @staticmethod
    def get_range_weapon(weapon_name):
        if weapon_name in globals() and weapon_name in RANGE_WEAPONS:
            range = globals()[weapon_name]
            return RANGE_WEAPON(name=weapon_name, **range)
        else:
            interaction.throwError("No Weapon with such name")
            return None

#print(WEAPON.get_melee_weapon("SWORD"))