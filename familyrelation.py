from collections import deque
import random
random.seed(1)
class FamilyRelation:
    maxsearch = 3
    def __init__(self, p1, p2):
        
        if not FamilyRelation.applies(p1,p2):
            raise Exception("Not a family relationship")


        self.p1 = p1
        self.p2 = p2
        self.commonancestor,self.inlaw, self.adopted = FamilyRelation.getCommonAncestor(p1,p2)
        self.p1gens, self.p2gens = self.getGensToAncestor(self.p1), self.getGensToAncestor(self.p2)
        
    def applies(p1,p2):
        return FamilyRelation.getCommonAncestor(p1,p2) is not None

    def getGensToAncestor(self, person):
        queue = deque([(person,0,False)])
        while len(queue) > 0:
            nextperson, depth,inlawchecked = queue.popleft()
            if nextperson is None:
                continue
            #print(nextperson.name,nextperson.index, depth, inlawchecked ,queue)
            depth += 1
            if depth+int(self.inlaw) <= FamilyRelation.maxsearch:
                if nextperson == self.commonancestor:
                    return depth-1
                else:
                    for i in nextperson.parents + nextperson.adoptedparents:
                        queue.append((i,depth,False))
                    if not inlawchecked and self.inlaw:
                        queue.append((nextperson.spouse,depth-1,True))
        

    def getCommonAncestor(p1,p2):
        indicess = [{p1.index:(False,False)},{p2.index:(False,False)}]
        queue = deque([(p1,0,0,False,False),(p2,0,1,False,False)])
        while len(queue) > 0:
            nextperson, depth,treeof, inlaw, adopted = queue.popleft()
            #print(nextperson.name,nextperson.index, treeof, depth, inlaw ,adopted,indicess[treeof])
            depth += 1
            if depth + int(inlaw) <= FamilyRelation.maxsearch:
                if nextperson.index in indicess[1-treeof]:
                    inlaw2, adopted2 = indicess[1-treeof][nextperson.index]
                    return nextperson, inlaw or inlaw2, adopted or adopted2
                
                if nextperson.index not in indicess[treeof]:
                    indicess[treeof][nextperson.index] = (inlaw, adopted)

                if nextperson.spouse is not None and not inlaw:
                    queue.append((nextperson.spouse,depth-1,treeof,True, adopted))
                for i in nextperson.parents:
                    if i is not None:
                        queue.append((i,depth,treeof, inlaw, adopted))
                for i in nextperson.adoptedparents:
                    if i is not None:
                        queue.append((i,depth,treeof, inlaw, True))

        return None
    
    #relation from p1 to p2, reversed is from p2 to p1
    def getrelationname(self,to_person=None,include_hisher=True):
        grid = [[['the same person']*2,       ['father','mother'], ['grandfather','grandmother'],['great-grandfather','great-grandmother']],
        [['son','daughter'],          ['brother','sister'],['uncle','aunt'],['great-uncle','great-aunt']],
        [['grandson','granddaughter'],['nephew','niece'],  ['cousin','cousin'], ['first cousin once removed']*2],
        [['great-grandson','great-granddaughter'],['grandnephew','grandniece'],['first cousin once removed']*2,['second cousin']*2]]
        if to_person == self.p1 or to_person is None:
            p1,p2,p1gens,p2gens = self.p2,self.p1,self.p2gens,self.p1gens
        elif to_person == self.p2:
            p1,p2,p1gens,p2gens = self.p1,self.p2,self.p1gens,self.p2gens
        else:
            raise Exception("person not member of relation")
        hir = {'M':'his ','F':'her '}[p1.gender]

        val = ''
        if self.adopted:
            val += 'adopted '

        if self.inlaw:
            if p1gens == 0 and p2gens == 0:
                val +=  ['husband','wife'][{'M':0,'F':1}[p2.gender]]
            else:
                val +=  grid[p2gens][p2gens][{'M':0,'F':1}[p2.gender]]+'-in-law'
            if include_hisher:
                val = hir + val
            return val
        
        else:
            val += grid[p2gens][p1gens][{'M':0,'F':1}[p2.gender]]
            if (p1gens!= 0 or p2gens != 0) and include_hisher:
                val = hir + val
            return val

    def __repr__(self):
        return self.getrelationname()

from person import Person
gp1, gp2, gp3, gp4 = Person(), Person(), Person(), Person()
gp1.marry(gp2); gp3.marry(gp4)
print(gp1.name, '+',gp2.name,'     ',gp3.name,'+',gp4.name)
parent1,parent2,parent3 = (gp1.havechildwith(gp2),gp1.havechildwith(gp2),gp3.havechildwith(gp4))
parent1.marry(parent3)
print(parent1.name,'  ',parent2.name,'         ',parent3.name,)
childadopt = parent1.adopt(Person(), parent3)
print(childadopt.name)
print()
print(parent1.name,'+', parent3.name,'=')
child = (parent1.havechildwith(parent3))
child2 = (parent1.havechildwith(parent3))
sil = Person()
child.marry(sil)
print(child.name,'and',child2.name)
print(child.name,'married',sil.name)
child.adopt(gp1, sil)
x,y =   sil,gp1
print('\ntesting relation of',x.name,y.name)
a = (FamilyRelation(x, y))
print('p1gens',a.p1gens,'p2gens',a.p2gens)
print(x.name,'is',y.name+'\'s',a.getrelationname(x,include_hisher=False))
#should be adopted father

dad=Person()
son = dad.havechildwith(Person())
wife = Person()
granddaughter = wife.havechildwith(Person())
son.marry(wife)
dad.marry(granddaughter)
print('dad married his son\'s daughter')
print('dad and son\'s wife =',FamilyRelation(dad,wife))



human = Person(gender='F',name='Human Aurelia aosis')
other = Person(gender='M', name='Name Lucius apjs')
human.marry(other)
print(human,other)
for i in range(1):
    child = other.havechildwith(human)
    wifey = child.marry(Person())
    for i in range(1):
        c2 = wifey.havechildwith(child)
        wifey2 = c2.marry(Person())
        for i in range(1):
            c3 = wifey2.havechildwith(c2)
    print(c2,c2.index)