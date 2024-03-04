import fighter, rules
from typing import List

class Battle:
    def __init__(self, units : List[fighter.CHARACTER]):
        self.units = units
        
        
    def turn(self):
        for unit in rules.getTurnPriority(self.units):
            pass