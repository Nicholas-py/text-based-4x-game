from kill import Kill
from actiontype import ActionType
from action import Action
from person import Person


####
#MASTER LIST OF ALL COMMANDS
####
commands = [Kill]
max_command_word_count = 4

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

def getpossession(tokens):
    return tokens[0],1



def parseargs(tokens, targetargs):
    for i in tokens:
        if i == '':
            tokens.remove(i)
    basetokens = tokens
    for argpattern in targetargs:
        tokens = basetokens.copy()
        outputs = []
        matched = True
        for term in argpattern.split(' '):
            if len(tokens) == 0:
                matched = False
                break
            arg = None
            numused = 1
            match term:
                case 'Person':
                    arg, numused = getperson(tokens)
                case 'Possession':
                    arg, numused = getpossession(tokens)
            if arg:
                outputs.append(arg)
            tokens = tokens[numused:]
        if len(tokens):
            matched = False
        
        if matched:
            return outputs
    raise   ParserError('Arguments supplied did not match any overloads')         

primarys = [i.synonyms[0] for i in commands]
allsupported = getcommandlist(commands)

def parse(userstring) -> Action:
    tokens = userstring.split(' ')
    for i in range(1,max_command_word_count+1):
        commandname = ' '.join(tokens[0:i])
        if commandname in allsupported:
            command = allsupported[commandname]
            
            if isinstance(command, ActionType):
                try:
                    args = parseargs(tokens[i:], command.args)
                    return Action(command, args)
                except ParserError as e:
                    print('Argument Error: ',e)
            else:
                print('Action type unknown. This is weird.')
    else:
        print('Command not found')

if __name__ == '__main__':
    you = Person()
    print('You are:',you)
    print('Enter commands here.')
    while True:
        action = parse(input())
        if action:
            you.doaction(action)