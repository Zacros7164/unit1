import random
# this is a subclass of Character
# so import Character
from Character import Character


class Vampire(Character):
    def __init__(self):
        super(Vampire,self)__init__("Vampire", 15, 4)
        self.gold = randomGold
        self.speed = randomSpeed
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