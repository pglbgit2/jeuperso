import interaction


GEMSTONE_WEIGHT = 3
GEMSTONE_COST = 80
GEMSTONE =  {"weight" : GEMSTONE_WEIGHT, "cost" : GEMSTONE_COST}

class ITEM:
    def __init__(self, name: str, _cost : int, _weight : int):
        self.cost = _cost
        self.weight = _weight
        self.name = name
    
    @staticmethod
    def get_item(item_name):
        if item_name in globals():
            item = globals()[item_name]
            return ITEM(**item)
        else:
            interaction.throwError("No item with such name")
            return None