import random
class Hero(object):
    def __init__(self,name):
        randomHealth = random.randint(8,10)
        randomPower = random.randint(4,7) 
        self.name = name
        self.health = randomHealth
        self.power = randomPower

    def cheer_hero(self):
        print "Welcome, brave %s" % (self.name)
    
    def take_damage(self, amount_of_damage):
        self.health -= amount_of_damage
    def is_alive(self):
        return self.health > 0