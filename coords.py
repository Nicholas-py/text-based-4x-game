class Coords:
    def __init__(self,x,y=None):
        if y == None:
            if (isinstance(x,str)):
                
                data = x.replace('(','').replace(')','').replace(' ','').split(',')
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

    def fromlatlong(lat,long):
        y = -6.32*lat+417.7
        x = 4.25*long+53.2
        return Coords(x,y)

    def __repr__(self):
        return f'({self.x}, {self.y})'
if __name__ == '__main__':
    base = open('maps/europemap.txt').read().split('\n')
    while True:
        try:
            inp = input('Latitude longtitude? ').split(' ')
            lat, long = float(inp[0]),float(inp[1])
            coords = (Coords.fromlatlong(lat,long))
            print(coords)
            l = list(base[coords.y])
            l[coords.x] = '*'
            base[coords.y] = ''.join(l)
            print('worked! next')
        except Exception as e:
            print('exiting')
            break
    file = open('maps/europemapcities.txt','w+')
    file.write('\n'.join(base))
    file.close()
