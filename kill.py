from actiontype import ActionType


def kill(caller, target):
    pass


Kill = ActionType(["kill","murder", "slay", "execute", "dispatch",
    "eliminate", "terminate", "exterminate", "extinguish", "annihilate",
    "butcher", "massacre", "decimate", "obliterate", "eradicate",
    "assassinate", "silence", "ice", "waste", "off",
    "liquidate", "strangle", "suffocate", "poison", "stab",
    "shoot", "bludgeon", "stone", "hang", "drown",
    "garrote", "burn", "smother", "lynch", "crucify",
    "impale", "decapitate", "behead", "electrocute", "guillotine",
    "slaughter", "sacrifice", "immolate"],
    ['Person'], kill
)

