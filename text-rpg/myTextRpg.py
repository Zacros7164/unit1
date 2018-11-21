# Import relevant files and modules
from Hero import Hero
from Vampire import Vampire
from Goblin import Goblin
from Boss import Boss
import asciiArt
import dialogue
import os
# Get player name and instantiate a Hero object, and goblin object
hero_name = raw_input("What is your name? ")
theHero = Hero(hero_name)
theHero.cheer_hero
monster = Goblin()
# hard code monster speed so you can't run away from first fight
monster.speed = 15
# begin game loop
while theHero.is_alive():
    # print opening dialogue and first fight sequence
    print dialogue.openingSequence
    print asciiArt.goblin
    # begin while loop for first fight, necessary to move game along
    while theHero.health > 0 and monster.health > 0:
        print dialogue.battleStats % (theHero.health, theHero.power,monster.name, monster.health, monster.power)
        theHero.battle_choice()
        player_choice = raw_input("> ")
        
        if player_choice == "1": #fight
            monster.take_damage(theHero.power)
            print dialogue.battleStats % (theHero.health, theHero.power,monster.name, monster.health, monster.power)
        
        elif player_choice == "2": #dance
            print dialogue.dance % monster.name
            theHero.take_damage(monster.power)

        elif player_choice == "3": #flee
            if theHero.speed <= monster.speed:
                print dialogue.cantEscape % monster.name
            else:
                print dialogue.runAway % monster.name
                break
        
        if monster.is_alive(): #monster counter attacks
            theHero.take_damage(monster.power)
            print dialogue.monsterAttack % (monster.name, monster.power)
            if not theHero.is_alive(): # hero death message
                print asciiArt.death
                print dialogue.heroDied % monster.name
                break
            
        
        if not monster.is_alive(): # Monster death message
            print dialogue.monsterDied % monster.name
            print dialogue.power_up
            theHero.defeated_enemy(monster.power)
            monster.drop_gold()
        raw_input("Hit enter to continue ")
        os.system("clear")
    print dialogue.firstGoblin % (monster.name, monster.gold)
    theHero.get_wallet(monster.gold)
    # after winning first fight, take the Goblin's gold, get the map for the game and decide where to go
    while theHero.is_alive():
        # print dialogue.firstGoblin % (monster.name, monster.gold)
        # theHero.get_wallet(monster.gold)
        # # move story along with treasure map
        # print dialogue.movementChoice
        # movement_choice = raw_input("> ").lower()
        # if movement_choice == "town":
        #     print dialogue.arrivalTown
        #     movement_choice == "treasure"

        # elif movement_choice == "treasure":
        print dialogue.arrivalTreasure
        
        # else:
        #     print dialogue.invalidChoice

        # while movement_choice == "treasure":
        numMonsters = 0 #set monsters to 0
        if numMonsters < 3: #go through a few battles to power up for the boss fight
            theHero.dice_roll()
            if theHero.dice_roll >= 4: #randomly generate either a goblin or a vampire
                monster = Goblin() #generate goblin
                while theHero.health > 0 and monster.health > 0:
                    print dialogue.battleStats % (theHero.health, theHero.power,monster.name, monster.health, monster.power)
                    theHero.battle_choice()
                    player_choice = raw_input("> ")
                    
                    if player_choice == "1": #fight
                        monster.take_damage(theHero.power)
                        print dialogue.battleStats % (theHero.health, theHero.power,monster.name, monster.health, monster.power)
                    
                    elif player_choice == "2": #dance
                        print dialogue.dance % monster.name
                        theHero.take_damage(monster.power)

                    elif player_choice == "3": #flee
                        if theHero.speed <= monster.speed:
                            print dialogue.cantEscape % monster.name
                        else:
                            print dialogue.runAway % monster.name
                            break
                    else:
                        print dialogue.invalidChoice #entered an invalid choice
                        break
                    
                    if monster.is_alive(): #monster counter attacks
                        theHero.take_damage(monster.power)
                        print dialogue.monsterAttack % (monster.name, monster.power)
                        if not theHero.is_alive(): # hero death message
                            print asciiArt.death
                            print dialogue.heroDied % monster.name
                            break
                    
                    if not monster.is_alive(): # Monster death message
                        print dialogue.monsterDied % monster.name
                        print dialogue.power_up
                        theHero.defeated_enemy(monster.power)
                        monster.drop_gold()
                        numMonsters += 1
                        break
                    raw_input("Hit enter to continue ")
                    os.system("clear")
            else: 
                monster = Vampire() #generate a vampire
                while theHero.health > 0 and monster.health > 0:
                    print dialogue.battleStats % (theHero.health, theHero.power,monster.name, monster.health, monster.power)
                    theHero.battle_choice()
                    player_choice = raw_input("> ")
                    
                    if player_choice == "1": #fight
                        monster.take_damage(theHero.power)
                        print dialogue.battleStats % (theHero.health, theHero.power,monster.name, monster.health, monster.power)
                    
                    elif player_choice == "2": #dance
                        print dialogue.dance % monster.name
                        theHero.take_damage(monster.power)

                    elif player_choice == "3": #flee
                        if theHero.speed <= monster.speed:
                            print dialogue.cantEscape % monster.name
                        else:
                            print dialogue.runAway % monster.name
                            break
                    else:
                        print dialogue.invalidChoice #entered an invalid choice 
                        break
                    
                    if monster.is_alive(): #monster counter attacks
                        theHero.take_damage(monster.power)
                        print dialogue.monsterAttack % (monster.name, monster.power)
                        if not theHero.is_alive(): # hero death message
                            print asciiArt.death
                            print dialogue.heroDied % monster.name
                            break
                    
                    if not monster.is_alive(): # Monster death message
                        print dialogue.monsterDied % monster.name
                        print dialogue.power_up
                        theHero.defeated_enemy(monster.power)
                        monster.drop_gold()
                        numMonsters += 1
                        break
                    raw_input("Hit enter to continue ")
                    os.system("clear")
        else: 
            monster = Boss() #generate a boss
            print dialogue.encounterBoss
            while theHero.health > 0 and monster.health > 0:
                    print dialogue.battleStats % (theHero.health, theHero.power,monster.name, monster.health, monster.power)
                    theHero.battle_choice()
                    player_choice = raw_input("> ")
                    
                    if player_choice == "1": #fight
                        monster.take_damage(theHero.power)
                        print dialogue.battleStats % (theHero.health, theHero.power,monster.name, monster.health, monster.power)
                    
                    elif player_choice == "2": #dance
                        print dialogue.dance % monster.name
                        theHero.take_damage(monster.power)

                    elif player_choice == "3": #flee
                        if theHero.speed <= monster.speed:
                            print dialogue.cantEscape % monster.name
                        else:
                            print dialogue.runAway % monster.name
                            break
                    else:
                        print dialogue.invalidChoice
                        break
                    
                    if monster.is_alive(): #monster counter attacks
                        theHero.take_damage(monster.power)
                        print dialogue.monsterAttack % (monster.name, monster.power)
                        if not theHero.is_alive(): # hero death message
                            print asciiArt.death
                            print dialogue.heroDied % monster.name
                            break
                    
                    if not monster.is_alive(): # monster death message
                        print dialogue.monsterDied % monster.name
                        print dialogue.power_up
                        theHero.defeated_enemy(monster.power)
                        monster.drop_gold()
                        movement_choice = ""
                    raw_input("Hit enter to continue ")
                    os.system("clear")            

    replay = raw_input("Do you want to play again? (y/n) ")
    if replay == "n":
        break
    else:
        theHero = Hero(hero_name)
        monster = Goblin()
        monster.speed = 15
        continue