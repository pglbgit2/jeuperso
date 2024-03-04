import fighter, interaction


class Player(fighter.CHARACTER):
    def __init__(self, name:str, faction:str, gold:int = 0, HP:int =20, MaxHP:int =20, Stamina:int =5, magic:int =0, stamina_regeneration:int =5, race :str = "Human",  Equipment: List[Union[armors.ARMOR, weapons.WEAPON, weapons.RANGE_WEAPON]] = [], Inventory: List[items.ITEM] = [], skills : dict = {}):
        super().__init__(name,faction,gold,HP,MaxHP,Stamina, magic,  stamina_regeneration, race, Equipment, Inventory, skills)
    
    
    def getInitiative(self):
        interaction.askFor("Roll 1d100 dice for Initiative, Give result")