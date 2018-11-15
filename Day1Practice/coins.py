coins = 0
print "You have " + str(coins) + " coins."
extra = int(raw_input("Do you want another? (y or n) ")
if(extra == "y"):
    coins += 1
    print "You have " + str(coins) + " coins."
    extra = int(raw_input("Do you want another? (y or n) ")
else:
    print "Bye"
    break