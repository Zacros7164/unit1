import random


class Vampire(object):
    def __init__(self):
        randomPower = random.randint(4,7)
        randomHealth = random.randint(10,15)
        randomGold = random.randint(4,8)
        randomSpeed = random.randint(6,9)
        self.name = "vampire"
        self.health = randomHealth
        self.power = randomPower
        self.gold = randomGold
        self.speed = randomSpeed
    def take_damage(self, amount_of_damage):
        self.health -= amount_of_damage
    def is_alive(self):
        return self.health > 0
    def drop_gold(self):
        dice_roll = random.randint(1,6)
        if dice_roll == 5:
            self.gold = self.gold/2
            return self.gold
        if dice_roll == 4:
            self.gold = self.gold/3
            return self.gold
        if dice_roll <= 3:
            self.gold = self.gold/4
            return self.gold
        else:
            return self.gold

# vampire = Vampire()
# print vampire.gold
# vampire.drop_gold()
# print vampire.gold