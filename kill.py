from actiontype import ActionType
from weapons import Weapon
import random
from llm import syncresponse

def getweapon(person):
    weaponstrength = 0
    weapon = 'bare hands'
    for i in person.possessions:
        if i.weapon and i.strength > weaponstrength:
            weaponstrength = i.strength
            weapon = i
    return weapon

def kill(caller, args)->str:
    target = args[0]
    
    if len(args) > 1:
        weapon = args[1]
    elif len(caller.possessions):
        weapon = getweapon(caller)
    else:
        weapon = 'bare hands'
    
    strength = Weapon(weapon).strength
    attackstrength = int(caller.strength)/4+strength
    
    defenseweapon = getweapon(target)
    strength = Weapon(defenseweapon).strength
    defensestrength = int(target.strength)/4 + strength
    
    luck = random.randint(0,6)-3.5
    if attackstrength + luck > defensestrength:
        target.dead = True
        event = 'kill'
    elif attackstrength + luck < defensestrength - 4:
        caller.dead = True
        event = 'backkill'
    else:
        event = 'fail'

    prompt = 'Please provide a brief description of the following event to completion, to be used as narration in a novel. \
Avoid adding details not provided to you, and describe it in past tense\n'

    killdesc = {'kill':'is killing','backkill':'is trying to kill','fail':'is trying to kill'}[event]
    prompt += f'{repr(caller)} {killdesc} {repr(target)}'

    if weapon != 'bare hands':
        prompt += f' with a {weapon}'
    else:
        prompt += ' with '+caller.pronoun3+' bare hands'
    prompt += '. '

    if defenseweapon != 'bare hands':
        prompt += f'{repr(target)} fought back with a {defenseweapon}'
        if event == 'kill':
            prompt += ' but is unsuccessful.'
        elif event == 'fail':
            prompt += ' and manages to avoid death.'
        elif event == 'backkill':
            prompt += f' and kills {repr(caller)}'        
    else:
        if event == 'backkill':
            prompt += f'{repr(target)} fought back and is killing {repr(caller)}'
        if event == 'fail':
            prompt += f'{repr(target)} manages to escape'
    print(prompt+'\n\n')
    return prompt


Kill = ActionType([
    "kill", 
    "murder", 
    "slay",
    "butcher", 
    "massacre", 
    "assassinate", 
    "strangle", 
    "suffocate", 
    "stab", 
    "bludgeon", 
    "garrote", 
    "impale", 
    "decapitate", 
    "behead", 
    "strangle to death", 
    "beat to death", 
    "slaughter", 
    "smite"
    ],
    ['Person',
     'Person with Possession',
     'Person with a Possession',
     'Person with an Possession'], 
    kill
)

