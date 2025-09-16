from random import randint
class Skill:
    def __init__(self, value=''):
        if value == '':
            self.value = Skill.randskill()
        else:
            self.value = value

    def randskill():
        coinflips = [randint(0,1) for i in range(8)]
        return sum(coinflips)+1

    def randnear(skill):
        coinflips = sum([randint(0,1) for i in range(4)])
        return Skill(skill.value+coinflips-2)

    def randnear2(skill1, skill2):
        minv = min(skill1.value,skill2.value)
        maxv = max(skill1.value,skill2.value)
        val = randint(minv-1, maxv+1)
        return Skill(val)

    def __repr__(self):
        skilladjectives = ['absolutely horrible','horrible','awful','bad','not great','average','decent','good','great','incredible','absolutely incredible']
        return skilladjectives[self.value]

