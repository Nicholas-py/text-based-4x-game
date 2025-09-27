from llm import syncresponse
from person import Person
from relation import Relation

#temporary, until brought into own class
skilladjectives = ['absolutely horrible','horrible','awful','bad','not great','average','decent','good','great','incredible','absolutely incredible']
class Letter:
    def __init__(self, sender=Person(),recipient=Person(),date=0, codecontents=["nothing of substance"], replyto = None):
        self.sender = sender
        self.codecontents = codecontents
        self.contents = ""
        self.date = date
        self.recipient = recipient
        self.replyto = replyto

    def aiprompt(self):
        relation = Relation.get(self.sender,self.recipient)
            
        string = "You are a letter writer bot. You will only reply with the contents of a letter, including the greeting and signature. \n" 
        string += "Please draft a short letter from "+self.sender.name+'. '
        #if self.replyto:
         #   string += 'The letter is a reply to the following letter:\n'
          #  string += str(self.replyto)
           # string += '\nFor your reply, '
        string += "The letter is addressed to "+self.recipient.name+', '+relation.getstr(self.sender)+'. '
        string += "The letter is "+self.sender.personality+' and the writing is '+str(self.sender.writing)+'. '
        string += relation.getcloseness()+', and '
        string += self.sender.pronoun1+' ' + relation.getliking(self.sender)+' ' + relation.getstr(self.sender)
        string += ', who '+self.sender.pronoun1+' is sending the letter to. '
        if len(self.codecontents)==1:
            string += "The letter contains "+self.codecontents[0]
        else:
            self.codecontents[-1] = 'and '+ self.codecontents[-1]
            string += "The letter contains "+', '.join(self.codecontents)
        string += '. Do not include anything other than the contents of the letter'
        string += 'from '+self.sender.firstname()+' to '+self.sender.pronoun2 +' '+ relation.getstr(self.sender,False)
        print('\nPROMPT\n',string)
        return string

    def __repr__(self):
        if not self.contents:
            self.contents = syncresponse(self.aiprompt())
        return self.contents
if __name__ == '__main__':
    peep = Person()
    peep2 = Person()
    peep2.marry(peep)
    print('p1:',peep.name)
    print('p2:',peep2.name)
    peep2.getrelationto(peep).changecloseness(int(input('How close are they? ')))
    peep2.getrelationto(peep).changelikingfrom(peep, int(input('How much does the parent like the child? ')))
    peep2.getrelationto(peep).changelikingfrom(peep2, int(input('How much does the child like the parent? ')))
    l = (Letter(sender=peep,recipient=peep2))
    print(l)
    input()
    l2 = (Letter(sender=peep2, recipient=peep,replyto=l))
    print(l2)
    input()

    for i in range(1000):
        l = (Letter(sender=peep,recipient=peep2,replyto=l2))
        print(l)
        input()
        l2 = (Letter(sender=peep2, recipient=peep,replyto=l))
        print(l2)
        input()