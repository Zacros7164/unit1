import os
from Hero import Hero
hero_name = raw_input("What is your name? ")
theHero = Hero(hero_name, 8)
theHero.cheer_hero()


while(1):
   
    print """
    You have %d health and %d power. 
    The goblin has %d health and %d power.  
    What do you want to do?
    1. fight goblin
    2. do a little dance
    3. flee""" % (theHero.health, theHero.power, goblin_health, goblin_power)
    # Get the user's choice
    user_input = raw_input("> ")

    if user_input == "1":
        # The hero has decided to attack
        # Subtract goblin's health by hero's power
        goblin_health -= theHero.power
        print "You have done %d damage to the goblin" % theHero.power
    elif user_input == "2":
        theHero.health += 10
        print """
        The goblin stares at you in disbelief of your stupidity. 
        His jaw drops as your wounds heal."""
        print "Your health is now %d." % theHero.health
    elif user_input == "3":
        print "Goodbye, %s the cowardly" % hero_name
        break
    else: 
        # user entered something that we didn't offer
        print "You fool, thou hast stumbledith (invalid input)"
    # Now it's the goblin's turn
    # Unless he just died from the hero attack
    if goblin_health > 0:
        theHero.health -= goblin_power
        print "The goblin hits you for %d damage." % goblin_power
        if theHero.health <= 0:
            print "Thou hast been vanquished."
    raw_input("Hit enter to continue. ")
    os.system("clear")