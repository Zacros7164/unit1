class Character(object):
    def __init__(self,name,health,power):
        self.name = name
        self.health = health
        self.power = power
    
    def take_damage(self, amount_of_damage):
        self.health -= amount_of_damage
    
    def is_alive(self):
        return self.health > 0