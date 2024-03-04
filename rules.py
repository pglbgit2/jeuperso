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

ACTIONS_NAMES = {"Quick Movement" : QM,"Classic Movement" :  CM,"Slow Movement" :  SM,"Brutal Attack" :  BA,"Quick Attack" :  QA,"Classic Attack" :  CA,"Light Defense" :  LD,"Stoical Defense" :  SD,"Classic Defense" :  CD} 


class Action:
    def __init__(self, action_num : int, actor: fighter.CHARACTER, target: fighter.CHARACTER):
        assert action_num in ACTIONS_NAMES.keys()
        self.action_num = action_num
        self.actor = actor
        self.target = target


def getTurnPriority(units: List[fighter.CHARACTER], mod=ACTION_BY_SPEED):
    if mod == ACTION_BY_SPEED:
        return sorted(units, key=lambda x: x.get_speed(), reverse=True)
    
    if mod == ACTION_BY_INITIATIVE:
        return sorted(units, key= lambda x: x.getInitiative(), reverse=True)
    
    return []

def executeAction(actions: List[Action]):
    pass