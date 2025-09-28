from kill import Kill
from actiontype import ActionType
from action import Action
from person import Person


####
#MASTER LIST OF ALL COMMANDS
####
commands = [Kill]

class ParserError(Exception):
    pass


def getcommandlist(commands):
    toreturn = {}
    for command in commands:
        for syn in command.synonyms:
            toreturn[syn] = command
    return toreturn

def getperson(tokens):
    return Person(name=' '.join(tokens[0:3])),3

def parseargs(tokens, targetargs):
    outputs = []
    for i in targetargs:
        if len(tokens) == 0:
            raise ParserError("Not enough arguments given")
        match i:
            case 'Person':
                person, numused = getperson(tokens)
                outputs.append(person)
                tokens = tokens[numused:]
            

primarys = [i.synonyms[0] for i in commands]
allsupported = getcommandlist(commands)

def parse(userstring) -> Action:
    tokens = userstring.split(' ')
    if tokens[0] in allsupported:
        command = allsupported[tokens[0]]
        
        if isinstance(command, ActionType):
            try:
                args = parseargs(tokens[1:], command.args)
                return Action(command, args)
            except ParserError as e:
                print('Argument Error: ',e)
        else:
            print('Action type unknown. This is weird.')
    else:
        print('Command not found')

if __name__ == '__main__':
    print(allsupported)
    you = Person()
    print('You are:',you)
    print('Enter commands here.')
    while True:
        action = parse(input())
        if action:
            you.doaction(action)