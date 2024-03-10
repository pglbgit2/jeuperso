
### RACES ###


## HUMANS ##
HUMAN  = {
    "HP" : 20,
    "MaxHP" : 20,
    "Stamina" : 5,
    "magic" : 0,
    "stamina_regeneration"  : 5, 
    "race"  :  "Human",
    "dodge" : 0.15
}


### CHARACTER CLASSES ###

THIEF = {
    "HP" : 22,
    "MaxHP" : 22,
    "Stamina" : 5,
    "magic" : 0,
    "gold" : 5,
    "stamina_regeneration" : 5,
    "dodge" : 0.20,
    "Inventory" : {"weapons" : [["KNIFE",True]], "armors" : [], "items" : []} # Tuple is [Object, toEquip]
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
    "Inventory" : {"weapons" : [["SLINGSHOT",True], ["ROCK", False,20], ["SPIKED_CLUB",True]], "armors" : [], "items" : []}
}

ARCHER = {
    "HP" : 22,
    "MaxHP" : 22,
    "magic" : 0,
    "gold" : 5,
    "stamina_regeneration" : 5,
    "dodge" : 0.25,
    "Inventory" : {"weapons" : [["BOW",True], ["ARROW",False,20],["KNIFE",True]], "armors" : [], "items" : []}
}


### ALL RACES & CLASSES LISTED BELOW ###

RACES = ["HUMAN", "THIEF", "CITY_GARD", "FOOTPAD", "ARCHER"]
