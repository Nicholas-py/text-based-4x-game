from math import inf

def prepmap(name):
    file = open('maps/europemap'+name+'.txt')
    return file.read().split('\n')


symbols = '-+zw@'
basemap = prepmap('')
elevmap = prepmap('elev')
precmaps = [prepmap('prec'+str(i)) for i in range(1,13)]
tempmaps = [prepmap('temp'+str(i)) for i in range(1,13)]

def tileinmap(coords):
    row = basemap[coords.y]
    item = row[coords.x]
    return item != ' '


def gettileelev(coords):
    row = elevmap[coords.y]
    item = row[coords.x]
    if item == ' ':
        return -inf
    val = symbols.index(item)
    return val

def gettileprec(coords, month):
    row = precmaps[month-1][coords.y]
    item = row[coords.x]
    if item == ' ':
        return -inf
    val = symbols.index(item)
    return val

def gettiletemp(coords, month):
    row = tempmaps[month-1][coords.y]
    item = row[coords.x]
    if item == ' ':
        return -inf
    val = symbols.index(item)
    return val
