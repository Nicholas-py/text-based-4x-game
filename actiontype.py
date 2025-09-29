from uniques import Unique

class ActionType (Unique):

    #When creating a subclass, remember to include synonyms (a list of the names you can use for a command) and format
    #Args should be a list of strings, each one an arg

    def __init__(self, synonyms,args, oncall):
        self.synonyms = synonyms
        self.args = args
        self.oncall = oncall
    



