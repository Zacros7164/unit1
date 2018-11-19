import random
class Hero(object):
    def __init__(self,name):
        self.name = name
        self.health = 10
        self.power = random.randint(5,10)

theHero = Hero("Link")
print theHero.power