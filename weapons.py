import items, interaction, os, json
from inspect import signature
###### MELEE WEAPON ######
## DEFAULT SWORD ATTRIBUTES ##

SWORD_DAMAGE = 6
SWORD_WEIGHT = 20
SWORD_COST = 40 
SWORD_SPEED = 15
SWORD = {"damage" : SWORD_DAMAGE, "weight" : SWORD_WEIGHT, "cost" : SWORD_COST, "speed" : SWORD_SPEED, "type" : "blade"}

## DEFAULT SHIELD ATTRIBUTES ##

SHIELD_DAMAGE = 3
SHIELD_WEIGHT = 30
SHIELD_COST = 60 
SHIELD_SPEED = 15
SHIELD = {"damage" : SHIELD_DAMAGE, "weight" : SHIELD_WEIGHT, "cost" : SHIELD_COST, "speed" : SHIELD_SPEED, "type" : "impact"}



## DEFAULT KNIFE ATTRIBUTES ##

KNIFE_DAMAGE = 3
KNIFE_WEIGHT = 7
KNIFE_COST = 10
KNIFE_SPEED = 25
KNIFE = {"damage" : KNIFE_DAMAGE, "weight" : KNIFE_WEIGHT, "cost" : KNIFE_COST, "speed" : KNIFE_SPEED, "type" : "pierce"}

 
## DEFAULT LONG_SWORD ATTRIBUTES ##

LONG_SWORD_DAMAGE = 9
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

SPEAR_DAMAGE = 5
SPEAR_WEIGHT = 12
SPEAR_COST = 20
SPEAR_SPEED = 12
SPEAR = {"damage" : SPEAR_DAMAGE,"weight" :  SPEAR_WEIGHT,"cost" : SPEAR_COST, "speed" : SPEAR_SPEED, "type" : "pierce"}


## ENERGY_BLADE ##

ENERGY_BLADE_DAMAGE = 8
ENERGY_BLADE_WEIGHT = 1
ENERGY_BLADE_COST = 0
ENERGY_BLADE_SPEED = 15
ENERGY_BLADE = {"damage" : ENERGY_BLADE_DAMAGE,"weight" :  ENERGY_BLADE_WEIGHT,"cost" : ENERGY_BLADE_COST, "speed" : ENERGY_BLADE_SPEED, "type" : "arcane"}


## CORRUPTED_STAFF ##

CORRUPTED_STAFF_DAMAGE = 6
CORRUPTED_STAFF_WEIGHT = 20
CORRUPTED_STAFF_COST = 100
CORRUPTED_STAFF_SPEED = 12
CORRUPTED_STAFF = {"damage" : CORRUPTED_STAFF_DAMAGE,"weight" :  CORRUPTED_STAFF_WEIGHT,"cost" : CORRUPTED_STAFF_COST, "speed" : CORRUPTED_STAFF_SPEED, "type" : "necrotic"}

## MACE ##

MACE_DAMAGE = 11
MACE_WEIGHT = 40
MACE_COST = 90
MACE_SPEED = 3
MACE = {"damage" : MACE_DAMAGE,"weight" :  MACE_WEIGHT,"cost" : MACE_COST, "speed" : MACE_SPEED, "type" : "impact"}


## WOODEN_STAFF ##

WOODEN_STAFF_DAMAGE = 2
WOODEN_STAFF_WEIGHT = 40
WOODEN_STAFF_COST = 90
WOODEN_STAFF_SPEED = 3
WOODEN_STAFF = {"damage" : WOODEN_STAFF_DAMAGE,"weight" :  WOODEN_STAFF_WEIGHT,"cost" : WOODEN_STAFF_COST, "speed" : WOODEN_STAFF_SPEED, "type" : "impact"}



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

MELEE_WEAPONS = ["KNIFE", "SPEAR", "SWORD", "SPIKED_CLUB", "LONG_SWORD", "MACE", "CORRUPTED_STAFF", "ENERGY_BLADE", "SHIELD", "WOODEN_STAFF"]

THROWABLE = ["KNIFE", "ROCK", "SPEAR"]

RANGE_PROJECTILE = ["ARROW", "ROCK"]

RANGE_WEAPONS = ["BOW", "SLINGSHOT"]

ONE_HAND_WEAPONS = ["SWORD", "KNIFE", "SLINGSHOT", "SPIKED_CLUB", "SHIELD"]

SMALL_WEAPON = ["KNIFE"]

DEFENSIVE_WEAPON = ["SHIELD"]

HEAVY = ["LONG_SWORD", "MACE"]

TWO_HAND_WEAPONS = ["BOW", "LONG_SWORD", "SPEAR"]

INVOCATION = ["ENERGY_BLADE"]

class WEAPON(items.ITEM):
    def __init__(self, name : str, cost : int, damage : int, weight : int, speed : int, type : str):
        super().__init__(name,cost,weight)
        self.damage = damage
        self.speed = speed
        self.damageType = type
        self.canPoison = False
        
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
        
    @staticmethod
    def get_weapon_from_file(weapon_name):
        directory = "weapons"
        target_file = f"{weapon_name}.json"
        for root, dirs, files in os.walk(directory):
            if target_file in files:
                file_path = os.path.join(root, target_file)
                with open(file_path, 'r', encoding='utf-8') as file:
                    weapon = json.load(file)
                    if "categories" in weapon.keys():
                        categories = weapon["categories"]
                        del weapon['categories']
                    class_args = signature(WEAPON).parameters.keys()
                    if all(key in weapon for key in class_args):
                        for category in categories:
                            if category in globals().keys() and type(globals()[category]) is list:
                                Category = globals()[category]
                                if weapon["name"] not in Category:
                                    Category.append(weapon["name"])
                        instance = WEAPON(**weapon)
                        return instance
                    else:
                        print("Keys do not match the class constructor arguments.")
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
        

#print(WEAPON.get_weapon_from_file("sword"))