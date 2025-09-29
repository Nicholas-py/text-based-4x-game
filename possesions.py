from coords import Coords
from weapons import Weapon

class Possession:
    def __init__(self, 
                 itemtype,
                 location = Coords(0,0),
                 owner = None,
                 condition = 5,
                 ):
        self.itemtype = itemtype
        self.location = location
        self.owner = owner
        self.onowner = False
        self.condition = condition

        if Weapon.isit(self):
            self.weapon = Weapon(self.itemtype)

    def __repr__(self):
        string =  'a '+self.itemtype
        if self.condition != 5:
            string += 'in '+['awful','bad','mediocre','good'][self.condition]+' condition'
        return string
        