from random import *
from coords import Coords

fnames = open('fnames.txt','r').read().split('\n')
lnames = open('lnames.txt','r').read().split('\n')
personalities = open('personalities.txt').read().split('\n')
skilladjectives = ['absolutely horrible','horrible','awful','bad','not great','average','decent','good','great','incredible','absolutely incredible']
class Person:
    def __init__(self,
                 gender = choice(['M','F']),
                 country = 'Rome',
                 name = '', 
                 location = Coords(0,0),
                 personality = choice(personalities)+' and ' +choice(personalities),
                 title = ''):
        self.country = country
        self.gender = gender
        if not name:
            name = self.makename()
        self.name = name
        self.location = location
        self.title = title
        #skills
        self.strength = Person.randskill()
        self.oration = Person.randskill()
        self.persuasion = Person.randskill()
        self.strategy = Person.randskill()   
        self.writing = Person.randskill() 
        self.diplomacy = Person.randskill()
        self.personality = personality

    def randskill():
        coinflips = [randint(0,1) for i in range(8)]
        return sum(coinflips)+1

    def makename(self):
        fname = choice(fnames)
        mname = choice(fnames)
        while mname == fname:
            mname = choice(fnames)
        genderindex = int(self.gender == 'F')
        fname = fname.split(' ')[genderindex]
        mname = mname.split(' ')[genderindex]
        lname = choice(lnames)
        return ' '.join([fname.title(),mname.title(),lname.title()])


    def __repr__(self):
        string =  self.name+', of '+self.country+'. '
        string += 'Is '+self.personality+'. '
        string += 'Is '+skilladjectives[self.strength]+' physically, '
        string += skilladjectives[self.persuasion]+' at negotiation, '
        string += skilladjectives[self.diplomacy]+' at diplomacy, '
        string += skilladjectives[self.oration]+' at public speaking, '
        string += skilladjectives[self.strategy]+' at military strategy, and '
        string += skilladjectives[self.writing]+' at writing. '
        return string


print(Person())

