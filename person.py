from random import *
from coords import Coords
from skill import Skill
from relation import Relation

fnames = open('fnames.txt','r').read().split('\n')
lnames = open('lnames.txt','r').read().split('\n')
personalities = open('personalities.txt').read().split('\n')
class Person:
    lastindex = 0
    def __init__(self,
                 gender = '',
                 country = 'Rome',
                 name = None, 
                 location = Coords(0,0),
                 personality = None,
                 title = '',
                 parents = [None, None]):
        self.country = country
        if not gender:
            gender = choice(['M','F'])
        self.gender = gender
        self.parents = parents
        self.children = []
        if not name:
            name = self.makename(parents[0])
        self.name = name
        if not personality:
            personality = self.makepersonality(choice(self.parents))
        self.personality = personality

        self.location = location
        self.title = title
        self.diplomacy,self.oration,self.persuasion, self.strategy, self.strength, self.writing = self.makeskills()
        self.index = Person.lastindex
        Person.lastindex += 1

    def getrelation(self,other):
        if self.index == other.index:
            return 'the same person'
        elif other in self.parents:
            return ''
        else:
            return 'a complete stranger'

    def havechildwith(self, otherparent):
        child = Person(parents=[self,otherparent],country=self.country)
        self.children.append(child)
        otherparent.children.append(child)
        return child

    def makeskills(self):
        if self.parents[0] == None and self.parents[1] == None:
            return (Skill(),Skill(),Skill(),Skill(),Skill(),Skill())
        else:
            p1skills = self.parents[0].packskills()
            if not self.parents[1]:
                newskills = (Skill.randnear(i) for i in p1skills)
                return newskills
            else:
                p2skills = self.parents[1].packskills()
                newskills = (Skill.randnear2(p1skills[i],p2skills[i]) for i in range(len(p1skills)))
                return newskills
            
    def packskills(self):
        return (self.diplomacy,self.oration,self.persuasion, self.strategy, self.strength, self.writing)

    def makename(self,parent=None):
        if self.country == 'Rome':      
            fname = choice(fnames)
            if (not parent):
                mname = choice(fnames)
                while mname == fname:
                    mname = choice(fnames)
            else:
                pmname = parent.name.split(' ')[1].lower()
                for i in fnames:
                    if pmname in i:
                        pmname = i
                mname = pmname
            genderindex = int(self.gender == 'F')
            fname = fname.split(' ')[genderindex]
            mname = mname.split(' ')[genderindex]
            if not parent:
                lname = choice(lnames)
            else:
                lname = parent.name.split(' ')[2]
            return ' '.join([fname.title(),mname.title(),lname.title()])
        else:
            raise NotImplemented("Country not known")

    def makepersonality(self,parent=None):
        if parent == None:
            p1,p2 = choice(personalities),choice(personalities)
        else:
            p1 = choice(parent.personality.split(' and '))
            p2 = choice(personalities)
        while p2 == p1:
            p2 = choice(personalities)
        return p1 +' and '+ p2


    def __repr__(self):
        string =  self.title + self.name+', of '+self.country+'. '
        string += 'Is '+self.personality+'. '
        string += 'Is '+str(self.strength)+' physically, '
        string += str(self.persuasion)+' at negotiation, '
        string += str(self.diplomacy)+' at diplomacy, '
        string += str(self.oration)+' at public speaking, '
        string += str(self.strategy)+' at military strategy, and '
        string += str(self.writing)+' at writing. '
        return string

gp1, gp2 = Person(), Person()
print(gp1.name, '+',gp2.name,'=')
parent1,parent2,parent3 = (gp1.havechildwith(gp2),gp1.havechildwith(gp2),gp1.havechildwith(gp2))
print(parent1.name)
print('and')
print(parent2.name)
print('had a child:')
child = (parent1.havechildwith(Person()))
child2 = (parent2.havechildwith(Person()))
print(child.name)
x,y = parent3, child
a = (Relation(x, y))
print(x.name,': ',y.name,a.getrelationname(child))
print(child)

