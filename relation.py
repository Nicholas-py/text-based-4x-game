from familyrelation import FamilyRelation

class Relation:

    reldict = {}

    def get(p1,p2):
        if Relation.hash(p1,p2) not in Relation.reldict:
            Relation.reldict[Relation.hash(p1,p2)] = Relation(p1,p2)
        return Relation.reldict[Relation.hash(p1,p2)]

    def __init__(self,p1,p2):
        self.p1 = p1
        self.p2 = p2
        self.closeness = 0 #0 to 5
        self.p1liking = 0 # -5 to 5
        self.p2liking = 0 # -5 to 5
        self.statusfromp1 = ''
        self.statusfromp2 = ''

        if FamilyRelation.applies(p1,p2):
            self.familyrelation = FamilyRelation(p1,p2)
            self.statusfromp1 = self.familyrelation.getrelationname(p2,False)
            self.statusfromp2 = self.familyrelation.getrelationname(p1,False)
        else:
            self.familyrelation = None
    
    def changecloseness(self,amount=1):
        self.closeness += amount
        self.clampvals()
    
    def changelikingfrom(self,person, amount=1):
        if person == self.p1:
            self.p2liking += amount
        elif person == self.p2:
            self.p1liking += amount
        else:
            raise Exception(person.name + " not a member of relation")
        self.clampvals()

    def clampvals(self):
        if self.p1liking < -5:
            self.p1liking = -5
        if self.p1liking > 5:
            self.closeness = 5

        if self.p2liking > 5:
            self.closeness = 5
        if self.p2liking < -5:
            self.liking = -5

        if self.closeness > 5:
            self.closeness = 5
        if self.closeness < 0:
            self.closeness = 0


    def hash(p1,p2):
        return str(min(p1.index,p2.index)) + ':'+str(max(p1.index,p2.index))

    def getcloseness(self):
        lst = [
            'They do not know each other',
            'They barely know each other',
            'They know each other fairly well',
            'They are familiar with each other',
            'They are extremely familiar with each other',
            'They know each other as well as possible'
        ]
        return lst[int(self.closeness)]
    
    #For use in - he/she ____ him/her
    def getliking(self,fromperson):
        lst = [
            'eternally hates',
            'hates',
            'strongly dislikes',
            'dislikes',
            'is not a fan of',
            'is neutral about',
            'somewhat likes',
            'likes',
            'is fond of',
            'is very fond of',
            'dearly loves'
        ]
        if fromperson == self.p1:
            return lst[self.p2liking+5]
        elif fromperson == self.p2:
            return lst[self.p1liking+5]

    def getstr(self, fromperson):
        if fromperson == self.p1:
            if self.statusfromp1 == '' and self.closeness == 0:
                return 'a stranger'
            else:
                return self.p1.pronoun2 +' '+ self.statusfromp1
        elif fromperson == self.p2:
            if self.statusfromp2 == '' and self.closeness == 0:
                return 'a stranger'
            else:
                return self.p2.pronoun2 +' '+ self.statusfromp2
        else:
            raise Exception('Not part of relationship')

