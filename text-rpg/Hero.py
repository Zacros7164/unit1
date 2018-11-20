class Hero(object):
    def __init__(self,name, power = 5):
        self.name = name
        self.health = 10
        self.power = power

    def cheer_hero(self):
        print "Welcome, brave %s" % (self.name)