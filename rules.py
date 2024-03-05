from typing import List
import fighter


PRIORITY_BY_SPEED = 0
PRIORITY_BY_INITIATIVE = 1
PRIORITY = PRIORITY_BY_SPEED



def getTurnPriority(units: List[fighter.CHARACTER], mod=PRIORITY):
    if mod == PRIORITY_BY_SPEED:
        return sorted(units, key=lambda x: x.get_speed(), reverse=True)
    
    if mod == PRIORITY_BY_INITIATIVE:
        return sorted(units, key= lambda x: x.getInitiative(), reverse=True)
    
    return []

