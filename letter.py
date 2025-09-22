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
            
        string = "You are a letter writer bot. You will only reply with the contents of a letter., including the greeting and signature. \n" 
        string += "Please draft a short letter from "+self.sender.name+'. '
        if self.replyto:
            string += 'The letter is a reply to the following letter:\n'
            string += str(self.replyto)
            string += '\nFor your reply, '
        string += "The letter is addressed to "+self.recipient.name+', '+relation.getstr(self.sender)+'. '
        string += relation.getcloseness()+'. '
        string += "The letter's style is somewhat "+self.sender.personality+' and the writing is '+str(self.sender.writing)+'. '
        string += self.sender.pronoun1.title()+' ' + relation.getliking(self.sender)+' ' + relation.getstr(self.sender)
        string += ', who '+self.sender.pronoun1+' is sending the letter to. '
        if len(self.codecontents)==1:
            string += "The letter contains "+self.codecontents[0]
        else:
            self.codecontents[-1] = 'and '+ self.codecontents[-1]
            string += "The letter contains "+', '.join(self.codecontents)
        string += '. Do not include anything other than the contents of the letter from '+self.sender.firstname()+'.'
        print('\nPROMPT\n',string)
        return string

    def __repr__(self):
        if not self.contents:
            self.contents = syncresponse(self.aiprompt())
        return self.contents
if __name__ == '__main__':
    peep = Person()
    child = peep.havechildwith(Person())
    print('parent:',peep.name)
    print('child:',child.name)
    child.getrelationto(peep).changecloseness(int(input('How close are they? ')))
    child.getrelationto(peep).changelikingfrom(peep, int(input('How much does the parent like the child? ')))
    child.getrelationto(peep).changelikingfrom(child, int(input('How much does the child like the parent? ')))
    l = (Letter(sender=peep,recipient=child))
    l2 = (Letter(sender=child, recipient=peep,replyto=l))
    print(l2)
    input()

    for i in range(1000):
        l = (Letter(sender=peep,recipient=child,replyto=l2))
        l2 = (Letter(sender=child, recipient=peep,replyto=l))
        print(l2)
        input()