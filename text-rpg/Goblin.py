import random


class Goblin(object):
    def __init__(self):
        randomPower = random.randint(2,5)
        randomHealth = random.randint(6,9)
        self.name = "Goblin"
        self.health = randomHealth
        self.power = randomPower
    def take_damage(self, amount_of_damage):
        self.health -= amount_of_damage
    def is_alive(self):
        return self.health > 0
