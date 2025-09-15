from llm import syncresponse
from person import Person
#temporary, until brought into own class
skilladjectives = ['absolutely horrible','horrible','awful','bad','not great','average','decent','good','great','incredible','absolutely incredible']
class Letter:
    def __init__(self, sender=Person(),recipient=Person(),date=0, codecontents=["nothing of substance"]):
        self.sender = sender
        self.codecontents = codecontents
        self.contents = ""
        self.date = date
        self.recipient = recipient

    def aiprompt(self):
        string = "Please draft a short letter from "+self.sender.name+'. '
        string += "The letter is addressed to "+self.recipient.name+', '+self.sender.getrelation(self.recipient)+'. '
        string += "Its style is "+self.sender.personality+' and the writing is '+skilladjectives[self.sender.writing]+'. '
        if len(self.codecontents)==1:
            string += "The letter contains "+self.codecontents[0]
        else:
            self.codecontents[-1] += 'and '
            string += "The letter contains "+', '.join(self.codecontents)
        string += '. '
        print('\nPROMPT\n',string)
        return string

    def __repr__(self):
        if not self.contents:
            self.contents = syncresponse(self.aiprompt())
        return self.contents

peep = Person()
print(Letter(sender=peep,recipient=Person()))