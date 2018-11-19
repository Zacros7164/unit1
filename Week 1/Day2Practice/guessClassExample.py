# import any needed modules
import random

# generate a random number using hte random module which is a part of python
secrectNumber = random.randint(1, 10)
print secrectNumber
# Set a secret number as 5. 
# secrectNumber = 5
# Init the bool gameOn to True
gameOn = True
# Run a loop until gameOn = False
while(gameOn):
    # get the users input and store it in userGuess
    userGuess = int(raw_input("guess a number between 1 and 10"))
    # userGuessAsInt = int(userGuess)
    # if the userGuess = the secrectNumber, then ...
    # change gameOn = False
    # single = means assignment, == means compare
    if(userGuess == secrectNumber):
        # the user guessed the right number (or we wouldn't run
        # this code) or change gameOn to False, so we can
        # quit the loop
        gameOn = False
        # Congrtulate the user for being awesome
        print "Great Job! Game over."
    # if the user did not gues the right number, tell them
    # to guess again
    else:
        # if the user is too high, tell them
        if(userGuess > secrectNumber):
            # print "Your guess is too high."
            print str(userGuess) + " is too high."

        # if the user guess isn't too high and isn't right it must be too low
        else: 
            # option 1. print userGuess + " is too low"
            # option 2. print str(userGuess) + " is too low."
            # interpolation = mixing strings and variables
            # in Python you can interpolate with a % sign (use % with data type e.g. %i, %s, )
            print "%i is too low" % userGuessAsInt 

        
        print "Guess again... "
