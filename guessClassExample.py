# Set a secret number as 5. 
secrectNumber = 5
# Init the bool gameOn to True
gameOn = True
# Run a loop until gameOn = False
while(gameOn):
    # get the users input and store it in userGuess
    userGuess = int(raw_input("guess a number between 1 and 10"))
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
        print "Guess again... "
        