
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
    "default_damage" : 3,
    "default_damage_type" : "impact",

}

## GIANT_SPIDER ##
GIANT_SPIDER = {
    "HP" : 50,
    "MaxHP" : 50,
    "Stamina" : 10,
    "magic" : 0,
    "stamina_regeneration"  : 10, 
    "race"  :  "GIANT_SPIDER",
    "dodge" : 0.15,
    "raceResistance" : {"blade" : 0.3, "pierce" : 0.3, "impact" : -0.2},
    "default_damage" : 18,
    "default_damage_type" : "pierce",
    "bodyBaseResistance" : {"head" : 10, "torso" : 45, "legs": 30}
}

## BAT ##
BAT = {
    "HP" : 10,
    "MaxHP" : 10,
    "Stamina" : 5,
    "magic" : 0,
    "stamina_regeneration"  : 5, 
    "race"  :  "BAT",
    "dodge" : 0.50,
    "raceResistance" : {},
    "default_damage" : 4,
    "default_damage_type" : "pierce",
    "bodyBaseResistance" : {"head" : 0, "torso" : 0, "legs": 0}
}

## SNAKE ##
SNAKE = {
    "HP" : 12,
    "MaxHP" : 12,
    "Stamina" : 5,
    "magic" : 0,
    "stamina_regeneration"  : 5, 
    "race"  :  "SNAKE",
    "dodge" : 0.20,
    "raceResistance" : {},
    "default_damage" : 4,
    "default_damage_type" : "pierce",
    "bodyBaseResistance" : {"head" : 0, "torso" : 0, "legs": 0}
}

## SRAVAL ##
SRAVAL = {
    "HP" : 30,
    "MaxHP" : 30,
    "Stamina" : 9,
    "magic" : 3,
    "stamina_regeneration"  : 8, 
    "race"  :  "SRAVAL",
    "dodge" : 0.25,
    "raceResistance" : {"blade" : 0.3, "pierce" : 0.3, "impact" : 0.3, "fire" : -0.5},
    "default_damage" : 8,
    "default_damage_type" : "impact",
    "bodyBaseResistance" : 5
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
    "raceResistance" : {"blade":0.2, "impact" : 0.2, "fire" : -0.1},
    "default_damage" : 4,
    "default_damage_type" : "impact",
}

### TROLL
TROLL  = {
    "HP" : 110,
    "MaxHP" : 110,
    "Stamina" : 10,
    "magic" : 0,
    "stamina_regeneration"  : 7, 
    "race"  :  "TROLL",
    "dodge" : 0.05,
    "raceResistance" : {"blade":0.4, "impact" : 0.3, "fire" : 0.3, "arcane":-0.3},
    "default_damage" : 8,
    "default_damage_type" : "impact",
    "skillsLevel" : {"Brutal_Attack" : 4},
    "bodyBaseResistance" : {"head" : 0, "torso" : 70, "legs": 0}
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
    "raceResistance" : {},
    "default_damage" : 1,
    "default_damage_type" : "impact",
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
    "raceResistance" : {"blade" : 0.4, "pierce" : 0.4, "impact" : -0.3, "arcane" : -0.5},
    "default_damage" : 2,
    "default_damage_type" : "necrotic",
}

### CHARACTER CLASSES ###

DEFAULT_CLASS = {}

THIEF = {
    "Stamina" : 5,
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
    "magic" : 0,
    "gold" : 5,
    "stamina_regeneration" : 5,
    "dodge" : 0.25,
    "Inventory" : {"weapons" : [["SLINGSHOT",True], ["ROCK", False,20], ["SPIKED_CLUB",True]], "armors" : [["PADDED_ARMOR",True]], "items" : []}
}

ARCHER = {
    "magic" : 0,
    "gold" : 5,
    "stamina_regeneration" : 5,
    "dodge" : 0.15,
    "Inventory" : {"weapons" : [["BOW",True], ["ARROW",False,20],["KNIFE",True]], "armors" : [], "items" : []}
}

WARRIOR = {
    "gold" : 5,
    "stamina_regeneration" : 6,
    "dodge" : 0.15,
    "Inventory" : {"weapons" : [["random",True,["SPIKED_CLUB", "SWORD"]]], "armors" : [], "items" : []}
}

BRUTE = {
    "Inventory" : {"weapons" : [["random",True,["WOODEN_STAFF", "SPIKED_CLUB"]]], "armors" : [], "items" : []}
}

APPRENTICE = {
    "HP" : 20,
    "MaxHP" : 20,
    "magic" : 15,
    "gold" : 10,
    "stamina_regeneration" : 4,
    "dodge" : 0.10,
    "Inventory" : {"weapons" : [], "armors" : [], "items" : []},
    "skills" : ["Minor_Shield", "Minor_Aggressive_Flux", "Energy_Blade", "EnergyRay", "Solid_Skin"]
}

MAGE = {
    "HP" : 20,
    "MaxHP" : 20,
    "magic" : 15,
    "gold" : 10,
    "stamina_regeneration" : 4,
    "dodge" : 0.10,
    "Inventory" : {"weapons" : [], "armors" : [], "items" : []},
    "skills" : ["Minor_Shield", "Protection_Field", "Minor_Aggressive_Flux", "Wrath_Torrent", "Energy_Blade", "EnergyRay", "EnergyOrb", "Unshakable_Fortress", "Solid_Skin"]
}


### ALL RACES & CLASSES LISTED BELOW ###


POISONER = ["SNAKE"]
RACES = ["HUMAN","ORC","GOBLIN", "UNDEAD", "GIANT_SPIDER", "SRAVAL", "SNAKE", "BAT", "TROLL"]
CLASSES = ["THIEF", "CITY_GARD", "FOOTPAD", "ARCHER", "WARRIOR", "DEFAULT_CLASS", "MAGE","APPRENTICE", "BRUTE"]
INVENTORY_CLASSES = ["BRUTE"]
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
