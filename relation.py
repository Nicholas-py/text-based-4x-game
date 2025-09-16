from collections import deque
class Relation:
    maxsearch = 3
    def __init__(self, p1, p2):
        
        self.p1 = p1
        self.p2 = p2
        self.commonancestor = self.getCommonAncestor()
        if self.commonancestor:
            self.p1gens, self.p2gens = self.getGensToAncestor(self.p1), self.getGensToAncestor(self.p2)
    
    def getGensToAncestor(self, person):
        queue = deque([(person,0)])
        while len(queue) > 0:
            nextperson, depth = queue.popleft()
            depth += 1
            if depth <= Relation.maxsearch:
                if nextperson == self.commonancestor:
                    return depth-1
                else:
                    queue.append((nextperson.parents[0],depth))
                    queue.append((nextperson.parents[1],depth))

    def getCommonAncestor(self):
        indices = {}
        queue = deque([(self.p1,0),(self.p2,0)])
        while len(queue) > 0:
            nextperson, depth = queue.popleft()
            depth += 1
            if depth <= Relation.maxsearch:
                if nextperson.index in indices:
                    return nextperson
                indices[nextperson.index] = nextperson
                for i in nextperson.parents:
                    if i is not None:
                        queue.append((i,depth))
        return None
    
    #relation from p1 to p2, reversed is from p2 to p1
    def getrelationname(self,from_person=None):
        if not self.commonancestor:
            return 'a complete stranger'
        if from_person == self.p1 or from_person is None:
            p1,p2,p1gens,p2gens = self.p1,self.p2,self.p1gens,self.p2gens
        elif from_person == self.p2:
            p1,p2,p1gens,p2gens = self.p2,self.p1,self.p2gens,self.p1gens

        hir = {'M':'his ','F':'her '}[p1.gender]
        grid = [[['the same person']*2,       ['father','mother'], ['grandfather','grandmother'],['great-grandfather','great-grandmother']],
                [['son','daughter'],          ['brother','sister'],['uncle','aunt'],['great-uncle','great-aunt']],
                [['grandson','granddaughter'],['nephew','niece'],  ['cousin','cousin'], ['first cousin once removed']*2],
    [['great-grandson','great-granddaughter'],['grandnephew','grandniece'],['first cousin once removed']*2,['second cousin']*2]]
        val = grid[p2gens][p1gens][{'M':0,'F':1}[p2.gender]]
        if p1gens!= 0 or p2gens != 0:
            val = hir + val
        return val

    def __repr__(self):
        return self.getrelationname()
