from typing import Tuple


class Map:
    def __init__(self, filename=None, dimension : Tuple[int,int] = (50,50)):
        if filename == None:
            self.dimension = dimension
        else:
            self.map = None