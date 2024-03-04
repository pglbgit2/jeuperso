import fighter, rules, interaction, player
from typing import List

class Battle:
    def __init__(self, units : List[fighter.CHARACTER]):
        self.units = units
        self.unitsByName = {x.name : x for x in units}
    
    def getNPCActions(self, units):
        pass
    
    def turn(self):
        for unit in self.units:
            if isinstance(unit, player.Player):
                unit.actions = interaction.getPlayerActions(self.unitsByName)
            else : unit.actions = self.getNPCActions(self.units)
        
        for unit in rules.getTurnPriority(self.units):
            pass
            