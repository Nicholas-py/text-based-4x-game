from llm import asyncresponse, syncresponse
import asyncio
from coords import Coords
from random import random
from math import inf
from tile import gettile, Tile
coords = Coords(input('Enter your coordinates: '))
month = 6
tile = (gettile(coords))

#Will be used with "the landscape is ____"
elevadjs = ['flat','flat','rolling','hilly','mountainous']

#Will be used with "the tempurature is _____"
tempadjs = ['freezing','chilly','temperate','hot','boiling']

#Chance of raining, and raining heavily if so
rainchances = [1/10,1/4,1/2,2/3,3/4]
heavyrainchances = [1/5,1/3,1/3,1/2,2/3]
rainadjs = ['sunny out','lightly raining','heavily raining']

prompt = 'Please describe the scenery of where I am. '

elev = tile.elev

temp = tile.temps[month]

rainavg = tile.precs[month]
#If no data (in ocean), use average ocean rain quantities
if rainavg == -inf:
    rainavg = 2
rainlevel = 0
if random() < rainchances[rainavg]:
    rainlevel += 1
    if random() < heavyrainchances[rainavg]:
        rainlevel += 1


if tile.ocean:
    location = 'the North Sea'
    prompt += f'''I'm on a boat in {location}, with no land anywhere in sight. '''
else:
    prompt += f'''The landscape is {elevadjs[elev]}, the tempurature is {tempadjs[temp]}. '''
    
prompt += f"It's {rainadjs[rainlevel]}. "

prompt += 'Describe of this scenery in 3-5 sentences. Describe it like you\'re writing the descriptive text for a video game'
async def main():
    print(syncresponse(prompt))

asyncio.run(main())