import os
# from [NAME OF FILE] import [CLASS]
from Hero import Hero
from Goblin import Goblin
from Vampire import Vampire
from random import randint
hero_name = raw_input("What is your name? ")
# Thre is only one Frodo
theHero = Hero(hero_name)
theHero.cheer_hero()
# There are many many goblins
# goblin = Goblin()

while (theHero.is_alive()): 

    # get random monster
    randMonster = randint(1,2)
    if randMonster == 1:
        monster = Goblin()
    else:
        monster = Vampire()
    print "You have encountered a terrifying %s." % monster.name
    while theHero.is_alive() and monster.is_alive():

        print """
        You have %d health and %d power. 
        The %s has %d health and %d power.  
        What do you want to do?
        1. fight %s
        2. do a little dance
        3. flee""" % (theHero.health, theHero.power,monster.name, monster.health, monster.power, monster.name)
        # Get the user's choice
        user_input = raw_input("> ")

        if user_input == "1":
            # The hero has decided to attack
            # Subtract monster's health by hero's power
            monster.take_damage(theHero.power)
            print "You have done %d damage to the monster" % theHero.power
        elif user_input == "2":
            theHero.health += 10
            print """
            The monster stares at you in disbelief of your stupidity. 
            His jaw drops as your wounds heal."""
            print "Your health is now %d." % theHero.health
        elif user_input == "3":
            print "Goodbye, %s the cowardly" % theHero.name
            break
        else: 
            # user entered something that we didn't offer
            print "You fool, thou hast stumbledith (invalid input)"
        # Now it's the monster's turn
        # Unless he just died from the hero attack
        if monster.is_alive():
            theHero.take_damage(monster.power)
            print "The monster hits you for %d damage." % monster.power
            if not theHero.is_alive():
                print "Thou hast been vanquished."
        if not monster.is_alive():
            print "You have vanquished the monster."
        raw_input("Hit enter to continue. ")
        os.system("clear")
    fight_again_message = "Fight another fiend, brave %s? " % theHero.name
    fight_again = raw_input(fight_again_message)
    if fight_again == "n":
        break
    else:
        continue