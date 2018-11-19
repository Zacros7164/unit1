import os
import random
user_name = raw_input("What is your name: ")
gameOn = True
hero = {
    "name" : user_name,
    "weapon damage" : 0,
    "base damage" : 5,
    "armor" : 15,
    "health" : 10,
}
hero_health = hero["armor"] + hero["health"]
hero_damage = hero["weapon damage"] + hero["base damage"]
goblin = {
    "armor": random.randint(1,5),
    "health": random.randint(5,10),
    "weapon damage": random.randint(1,7),
    "base damage": random.randint(2,4),
    "inventory": 2
}
goblin_health = goblin["health"] + goblin["armor"]
goblin_damage = goblin["weapon damage"] + goblin["base damage"]

def goblin_fight(x):
    goblin_health = goblin["health"] + goblin["armor"]
    goblin_damage = goblin["weapon damage"] + goblin["base damage"]
    hero_health = hero["armor"] + hero["health"]
    hero_damage = hero["weapon damage"] + hero["base damage"]
    while goblin_health > 0 and hero_health > 0:
        if user_choice == "1":
            goblin_health -= hero_damage
            print "You hit the goblin, he now has %d health left." % goblin_health
            if goblin_health > 0:
                print "The goblin screams in rage, and hits you back.\n you now have %d health left." % hero_health
                hero_health -= goblin_damage
        elif user_choice == "2":
            print "You dont speak goblin and he doesn't speak human, stupid.\nHe hits you."
            hero_health -= goblin_damage
            print "You now have %d health left." % hero_health
        elif user_choice == "3":
            print "You ran away."
            break
        else:
            print "The goblin doesn't wait for you to make the first move and hits you."
            hero_health -= goblin_damage
            print "You now have %d health left." % hero_health



while gameOn:
    print """
    You wake up in a forest, covered in rags. 
    Looking around you see a goblin approaching you.
    What do you want to do?
    1. Fight
    2. Talk
    3. Run """
    user_choice = raw_input("> ")
    goblin_fight(user_choice)
    print """
    You have killed the goblin, what would you like to do now?
    1. Rummage through the goblin's pockets
    2. Move away from the stench of the dead goblin """
    user_choice = raw_input("> ")
    if user_choice == "1":
        message = """
        You search the goblin's pockets. He has a weapon that does %d damage. 
        He has armor that adds %d health points. 
        And he has a crumpled piece of paper. """
        print message % (goblin["weapon damage"], goblin["goblin armor"])
        print """
        what would you like to do?
        1. Check the goblin's armor against your own
        2. Take armor
        3. Take weapon
        4. Take all"""
        user_choice = raw_input("> ")
        while goblin["inventory"] > 0
            if user_choice == "1":
                print """
                Your armor has %d points
                The goblin's armor has %d points
                Your weapon has %d points
                The goblin's weapon has %d points""" % (hero["armor"], goblin["armor"], hero["weapon damage"], goblin["weapon damage"])
                break
            elif user_choice == "2":
                