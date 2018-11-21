import random


class Boss(object):
    def __init__(self):
        randomPower = random.randint(10,15)
        randomHealth = random.randint(25, 45)
        randomGold = random.randint(50,100)
        randomSpeed = random.randint(8,15)
        self.name = "Demon"
        self.health = randomHealth
        self.power = randomPower
        self.gold = randomGold
        self.speed = randomSpeed
    def take_damage(self, amount_of_damage):
        self.health -= amount_of_damage
    def is_alive(self):
        return self.health > 0
    def drop_gold(self):
        return self.gold
    def take_critical_hit(self, hero_power):
        if probability == 6:
            self.health -= (hero_power * 2)

# vampire = Vampire()
# print vampire.gold
# vampire.drop_gold()
# print vampire.gold