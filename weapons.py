

#Weapon:strength/5
weapons = {
    "gladius":5,
    "spatha":5,
    "pugio":3,
    "pilum":3,
    "hasta":4,
    "contus":4,
    "scutum":2,
    "javelin":3,
    "spear":4,
    "longbow":4,
    "shortbow":3,
    "sling":3,
    "throwing stones":1,
    "battleaxe":5,
    "mace":4,
    "polearm":5,
    "staff":1,
    "dagger":2,
    "cane":1,
    "sword":4,
    "axe":3,
    "knife":2

}


class Weapon:
    def isit(item):
        return item.itemtype in weapons

    def __init__(self, itemtype):
        self.itemtype = itemtype
        if itemtype in weapons:
            self.strength = weapons[itemtype]
        else:
            self.strength = 0