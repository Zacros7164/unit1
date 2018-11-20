import os
# from [NAME OF FILE] import [CLASS]
from Hero import Hero
from Goblin import Goblin
hero_name = raw_input("What is your name? ")
# Thre is only one Frodo
theHero = Hero(hero_name)
theHero.cheer_hero()
# There are many many goblins
goblin = Goblin()

while (theHero.is_alive()): 
    # There are many many goblins
    goblin = Goblin()
    while theHero.is_alive() and goblin.is_alive():

        print """
        You have %d health and %d power. 
        The goblin has %d health and %d power.  
        What do you want to do?
        1. fight goblin
        2. do a little dance
        3. flee""" % (theHero.health, theHero.power, goblin.health, goblin.power)
        # Get the user's choice
        user_input = raw_input("> ")

        if user_input == "1":
            # The hero has decided to attack
            # Subtract goblin's health by hero's power
            goblin.take_damage(theHero.power)
            print "You have done %d damage to the goblin" % theHero.power
        elif user_input == "2":
            theHero.health += 10
            print """
            The goblin stares at you in disbelief of your stupidity. 
            His jaw drops as your wounds heal."""
            print "Your health is now %d." % theHero.health
        elif user_input == "3":
            print "Goodbye, %s the cowardly" % theHero.name
            break
        else: 
            # user entered something that we didn't offer
            print "You fool, thou hast stumbledith (invalid input)"
        # Now it's the goblin's turn
        # Unless he just died from the hero attack
        if goblin.is_alive():
            theHero.take_damage(goblin.power)
            print "The goblin hits you for %d damage." % goblin.power
            if not theHero.is_alive():
                print "Thou hast been vanquished."
        if not goblin.is_alive():
            print "You have vanquished the goblin."
        raw_input("Hit enter to continue. ")
        os.system("clear")