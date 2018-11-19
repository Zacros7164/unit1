bill = int(raw_input("What is the total bill amount? "))
service = raw_input("how was the service? (good, fair or bad) ")
if(service == "good"):
    tip = bill * .20
    total = bill + tip
    print "The total is $" + str(total)
elif(service == "fair"):
    tip = bill * .15
    total = bill + tip
    print "The total is $" + str(total)
elif(service == "bad"):
    tip = bill * .10
    total = bill + tip
    print "The total is $" + str(total)