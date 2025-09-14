class Coords:
    def __init__(self,x,y=None):
        if y == None:
            if (isinstance(x,str)):
                
                data = x.replace('(','').replace(')','').split(',')
                self.x = data[0]
                self.y = data[1]
            else:               
                self.y = x[1]
                self.x = x[0]
        else:
            self.x = x
            self.y = y
        self.x = int(self.x)
        self.y = int(self.y)
        assert self.x >= 0
        assert self.y >= 0

    def __repr__(self):
        return f'({self.x}, {self.y})'
