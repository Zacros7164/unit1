import random
secretNumber = random.randint(1, 10)
print "I am thinking of a number between 1 and 10."
playerGuess = int(raw_input("What is the number? "))
attempts = 4
while(attempts >= 0):
    if(attempts > 1):
        if(playerGuess < secretNumber):
            print str(playerGuess) + " is too low."
            print "Only " + str(attempts) + " tries left."
            attempts -= 1
            playerGuess = int(raw_input("What is the number? "))
        elif(playerGuess > secretNumber):
            print str(playerGuess) + " is too high."
            print "Only " + str(attempts) + " tries left."
            attempts -= 1
            playerGuess = int(raw_input("What is the number? "))
        elif(playerGuess == secretNumber):
            print "Correct, you win"
            attempts = 0
            replay = raw_input("Would you like to play again? (y or n) ")
            if (replay == "y"):
                secretNumber = random.randint(1, 10)
                print "I am thinking of a number between 1 and 10."
                playerGuess = int(raw_input("What is the number? "))
                attempts = 4
            else:
                print "Bye"
                break
    elif(attempts == 1):
        if(playerGuess < secretNumber):
            print str(playerGuess) + " is too low."
            attempts -= 1
            playerGuess = int(raw_input("Last chance, what is the number? "))
        elif(playerGuess > secretNumber):
            print str(playerGuess) + " is too high."
            attempts -= 1
            playerGuess = int(raw_input("Last chance, what is the number? "))
        elif(playerGuess == secretNumber):
            print "Correct, you win"
            replay = raw_input("Would you like to play again? (y or n) ")
            if (replay == "y"):
                secretNumber = random.randint(1, 10)
                print "I am thinking of a number between 1 and 10."
                playerGuess = int(raw_input("What is the number? "))
                attempts = 4
            else:
                print "Bye"
                break
    else:
        print "Sorry, you lose" 
        replay = raw_input("Would you like to play again? (y or n) ")
        if (replay == "y"):
            secretNumber = random.randint(1, 10)
            print "I am thinking of a number between 1 and 10. "
            playerGuess = int(raw_input("What is the number? "))
            attempts = 4
        else:
            print "Bye"
            break