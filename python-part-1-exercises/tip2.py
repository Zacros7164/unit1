bill = int(raw_input("What is the total bill amount? "))
service = raw_input("how was the service? (good, fair or bad) ")
split = int(raw_input("Split how many ways? "))
if(service == "good"):
    tip = bill * .20
    total = bill + tip
    share = total / split
    print "The total is $" + str(total)
    print "Each person owes " + str(share)

elif(service == "fair"):
    tip = bill * .15
    total = bill + tip
    share = total / split
    print "The total is $" + str(total)
    print "Each person owes " + str(share)

elif(service == "bad"):
    tip = bill * .10
    total = bill + tip
    share = total / split
    print "The total is $" + str(total)
    print "Each person owes " + str(share)
