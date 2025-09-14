from coords import Coords
from maptiles import *
class Tile:
    def __init__(self, coords):
        self.coords = coords
        self.ocean = not tileinmap(self.coords)
        if not self.ocean:
            self.elev = gettileelev(self.coords)
            self.temps = [gettiletemp(self.coords,i) for i in range(1,13)]
            self.precs = [gettileprec(self.coords,i) for i in range(1,13)]
        else:
            self.elev = -1000
            self.temps = [2 for i in range(12)]
            self.precs = [2 for i in range(12)]

    def __repr__(self):
        return(['Land','Ocean'][self.ocean]+' tile at '+str(self.coords)+'.')

def gettile(coords):
    return Tile(coords)