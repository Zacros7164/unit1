
appOpen = True
appDict = {
    "Zac": "770-380-1088",
    "Russ": "404-372-8616",
    "Anita": "404-401-2166:",
    "Misty": "706-988-3328",
}
while(appOpen):
    print "\nElectronic Phonebook App"
    print "\n ====================== \n"
    print "1. Look up an entry"
    print "2. Set an entry"
    print "3. Delete an entry"
    print "4. List all entries"
    print "5. Search for an entry"
    print "6. Quit"
    userInput = raw_input("\n What do you want to do? (1-6) ")
    if userInput == "1":
        option1 = raw_input("\n Who do you want to search for? ").lower().capitalize()
        if option1 in appDict:
            print "\n %s's phone number is %s.\n" % (option1, appDict[option1])
        else:
            print "\nNo %s in the phonebook." % option1
    if userInput == "2":
        option2name = raw_input("\nWhat is the name? ").lower().capitalize()
        option2number = raw_input("\nWhat is the phone number? ")
        appDict[option2name] = option2number
    elif userInput == "3":
        option3 = raw_input("\nWho do you want to delete? ").lower().capitalize()
        try:
            appDict[option3]
        except KeyError:
            print "\nThere is no %s in the phonebook." % option3
            continue
        userApprove = raw_input("\nAre you sure? (y/n) ").lower()
        if userApprove == "y":
            del appDict[option3]
            print "\n%s has been deleted from the phonebook." % option3
        else:
            continue
    elif userInput == "4":
        for key, value in appDict.items():
            print "\nFound entry for %s: %s" % (key, value)
    elif userInput == "5":
        option5 = raw_input("\nWhat number do you want to search for? ")
        for key,value in appDict.iteritems():
            if value == option5:
                print "\nFound %s: %s" % (key, value)
    elif userInput == "6":
        appOpen = False
    else:
        print "\nSorry that option doesn't exist. Please try again."
