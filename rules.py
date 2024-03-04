from typing import List
import fighter


ACTION_BY_SPEED = 0
ACTION_BY_INITIATIVE = 1



QM = 0 # Quick Movement 
CM = 1 # Classic Movement
SM = 2 # Slow Movement
BA = 3 # Brutal Attack
QA = 4 # Quick Attack
CA = 5 # Classic Attack
LD = 6 # Light Defense
SD = 7 # Stoical Defense
CD = 8 # Classic Defense

ACTIONS = {QM : "Quick Movement", CM : "Classic Movement", SM : "Slow Movement", BA : "Brutal Attack", QA : "Quick Attack", CA : "Classic Attack", LD : "Light Defense", SD : "Stoical Defense", CD : "Classic Defense"}

def getTurnPriority(units : List[fighter.CHARACTER], mod=ACTION_BY_SPEED):
    if mod == ACTION_BY_SPEED:
        return sorted(units, key=lambda x : x.get_speed(), reverse=True)
    
    if mod == ACTION_BY_INITIATIVE:
        return sorted(units, key= lambda x: x.getInitiative(), reverse=True)
    
    return []