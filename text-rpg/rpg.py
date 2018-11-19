# This is a procedural approach to a txt based rpg game
# The hero is fighting the goblin
# The hero has the option to:
# 1. Fight
# 2. Dance
# 3. Flee

# Go get the os module from python
import os
# os.system() will take any liux command
# and if python can run it, it will

# get the hero name from the player
hero_name = raw_input("What is thy name, brave adventurer? ")

def fight():
    print "Welcome %s. Thou art brave!" % hero_name
    # declare some variables
    # These variables are in the function scope
    # These variables are only accesible inside of fight()
    hero_health = 10
    hero_power = 5
    goblin_health = 6
    goblin_power = 2
    # run the game as long as BOTH characters have health > 0
    while hero_health > 0 and goblin_health > 0:
        print """
        You have %d health and %d power. 
        The goblin has %d health and %d power.  
        What do you want to do?
        1. fight goblin
        2. do a little dance
        3. flee""" % (hero_health, hero_power, goblin_health, goblin_power)
        # Get the user's choice
        user_input = raw_input("> ")

        if user_input == "1":
            # The hero has decided to attack
            # Subtract goblin's health by hero's power
            goblin_health -= hero_power
            print "You have done %d damage to the goblin" % hero_power
        elif user_input == "2":
            hero_health += 10
            print """
            The goblin stares at you in disbelief of your stupidity. 
            His jaw drops as your wounds heal."""
            print "Your health is now %d." % hero_health
        elif user_input == "3":
            print "Goodbye, %s the cowardly" % hero_name
            break
        else: 
            # user entered something that we didn't offer
            print "You fool, thou hast stumbledith (invalid input)"

        # Now it's the goblin's turn
        # Unless he just died from the hero attack
        if goblin_health > 0:
            hero_health -= goblin_power
            print "The goblin hits you for %d damage." % goblin_power
            if hero_health <= 0:
                print "Thou hast been vanquished."
        raw_input("Hit enter to continue. ")
        os.system("clear")


# ANYTIME YOU HAVE (), IT IS CALLING A FUNCTION
fight()