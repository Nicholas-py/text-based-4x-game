from famliyrelation import FamilyRelation

class Relation:
    def __init__(self,p1,p2):
        self.p1 = p1
        self.p2 = p2
        if FamilyRelation.applies(p1,p2):
            self.familyrelation = FamilyRelation(p1,p2)
        else:
            self.familyrelation = None
        
    def __repr__(self):
        return ''