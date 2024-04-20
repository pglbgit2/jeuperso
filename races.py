
### RACES ###


## HUMANS ##
HUMAN  = {
    "HP" : 20,
    "MaxHP" : 20,
    "Stamina" : 5,
    "magic" : 0,
    "stamina_regeneration"  : 5, 
    "race"  :  "HUMAN",
    "dodge" : 0.15,
    "raceResistance" : {},
    "default_damage" : 2
}


GIANT_SPIDER = {
    "HP" : 50,
    "MaxHP" : 50,
    "Stamina" : 10,
    "magic" : 0,
    "stamina_regeneration"  : 10, 
    "race"  :  "HUMAN",
    "dodge" : 0.20,
    "raceResistance" : {"blade" : 0.2, "pierce" : 0.2, "impact" : -0.2,},
    "default_damage" : 12,
    "default_damage_type" : "pierce",
    "tempDefByTurn" : 5
}


## ORCS ##
ORC  = {
    "HP" : 22,
    "MaxHP" : 22,
    "Stamina" : 7,
    "magic" : 0,
    "stamina_regeneration"  : 7, 
    "race"  :  "ORC",
    "dodge" : 0.10,
    "raceResistance" : {"blade":0.1}
}

## GOBLINS ##
GOBLIN  = {
    "HP" : 15,
    "MaxHP" : 15,
    "Stamina" : 5,
    "magic" : 0,
    "stamina_regeneration" : 5, 
    "race"  :  "GOBLIN",
    "dodge" : 0.25,
    "raceResistance" : {}
}

## UNDEAD ##
UNDEAD  = {
    "HP" : 20,
    "MaxHP" : 20,
    "Stamina" : 5,
    "magic" : 0,
    "stamina_regeneration" : 5, 
    "race"  :  "UNDEAD",
    "dodge" : 0.10,
    "raceResistance" : {"blade" : 0.3, "pierce" : 0.4, "impact" : -0.2, "arcane" : -0.5}
}

### CHARACTER CLASSES ###

DEFAULT_CLASS = {}

THIEF = {
    "HP" : 22,
    "MaxHP" : 22,
    "Stamina" : 5,
    "magic" : 0,
    "gold" : 5,
    "stamina_regeneration" : 5,
    "dodge" : 0.20,
    "Inventory" : {"weapons" : [["KNIFE",True]], "armors" : [["PADDED_ARMOR",True]], "items" : []} # Tuple is [Object, toEquip]
}

CITY_GARD = {
    "HP" : 24,
    "MaxHP" : 24,
    "magic" : 0,
    "gold" : 5,
    "stamina_regeneration" : 5,
    "dodge" : 0.15,
    "Inventory" : {"weapons" : [["SWORD",True]], "armors" : [["CHAIN_MAIL",True]], "items" : []}
}

FOOTPAD = {
    "HP" : 22,
    "MaxHP" : 22,
    "magic" : 0,
    "gold" : 5,
    "stamina_regeneration" : 5,
    "dodge" : 0.25,
    "Inventory" : {"weapons" : [["SLINGSHOT",True], ["ROCK", False,20], ["SPIKED_CLUB",True]], "armors" : [["PADDED_ARMOR",True]], "items" : []}
}

ARCHER = {
    "HP" : 22,
    "MaxHP" : 22,
    "magic" : 0,
    "gold" : 5,
    "stamina_regeneration" : 5,
    "dodge" : 0.15,
    "Inventory" : {"weapons" : [["BOW",True], ["ARROW",False,20],["KNIFE",True]], "armors" : [], "items" : []}
}

WARRIOR = {
    "HP" : 25,
    "MaxHP" : 25,
    "magic" : 0,
    "gold" : 5,
    "stamina_regeneration" : 6,
    "dodge" : 0.15,
    "Inventory" : {"weapons" : [["random",True,["SPIKED_CLUB", "SWORD"]]], "armors" : [], "items" : []}
}


MAGE = {
    "HP" : 20,
    "MaxHP" : 20,
    "magic" : 10,
    "gold" : 10,
    "stamina_regeneration" : 4,
    "dodge" : 0.10,
    "Inventory" : {"weapons" : [], "armors" : [], "items" : []},
    "skills" : ["Minor_Shield", "Protection_Field", "Minor_Aggressive_Flux", "Wrath_Torrent", "Energy_Blade"]
}

### ALL RACES & CLASSES LISTED BELOW ###



RACES = ["HUMAN","ORC","GOBLIN", "UNDEAD", "GIANT_SPIDER"]
CLASSES = ["THIEF", "CITY_GARD", "FOOTPAD", "ARCHER", "WARRIOR", "DEFAULT_CLASS", "MAGE"]

DEFAULT_RESISTANCE = {
    "impact" : 0,
    "pierce" : 0,
    "blade" : 0,
    "fire" : 0,
    "cold" : 0,
    "arcane" : 0,
    "necrotic" : 0,
    "lightning" : 0
}