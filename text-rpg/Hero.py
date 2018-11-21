import random
class Hero(object):
    def __init__(self,name):
        randomHealth = random.randint(8,10)
        randomPower = random.randint(4,7) 
        self.name = name
        self.health = randomHealth
        self.power = randomPower
        self.shield = False
        self.wallet = 0
        self.pocket = []
        self.speed = 10

    def cheer_hero(self):
        print "Welcome, brave %s" % (self.name)
    
    def take_damage(self, amount_of_damage):
        if self.shield:
            amount_of_damage -= self.power
            if amount_of_damage > 0:
                self.health -= amount_of_damage
        else:
            self.health -= amount_of_damage
    def is_alive(self):
        return self.health > 0
    def defeated_enemy(self, monster_power):
        self.power += (monster_power/2)
        self.health += (self.health/2)
    def get_wallet(self, monster_gold):
        self.wallet += monster_gold
        print "You now have %d gold in your wallet" % self.wallet
    def buy_items(self, prices, items):
        if self.wallet >= prices:
            self.pocket.append(items)
    def equip_shield(self):
        self.speed -= 2
        self.sheild = True
    def battle_choice(self):
        print """
        What would you like to do?
        1. Fight
        2. Talk
        3. Run Away"""
    def dice_roll(self):
        probability = random.randint(1,6)
        return probability
    def critical_hit(self):
        probability = random.randint(1,6)
        if probability == 6:
            print """
            You have scored a critical hit, and have done %d damage.""" % (self.power*2)
    
