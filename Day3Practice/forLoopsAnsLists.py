# # A for loop expects a starting point and an ending point
# # the ending point is non inclusive, meaining it will stop
# # when/before it gets there 

# # i = the thing that will change each time through, can be whatever variable name you want

# for i in range(1,10):
#     print i

# # a 3rd argument you can hand is called the "step"
# # by default the step is one

# for i in range(1,10,2):
#     print i

# # ==========LISTS==========
# # lists = Array in any other language
# # a list is a list of variables
# student1 = "Brian" 
# student2 = "Brandon"
# student3 = "Zac"
# student4 = "J.R."

# print student1
# print student2
# print student3
# print student4

# # A list groups "stuff" together and indexes them by number
# # A list index ALWAYS starts at 0
# # a list is made with []
# # when making a list separate each index with a comma
# # students = [
# #     "Brian", "Brandon", "Zac", "J.R."
# # ]
# # both of these options are exactly the same

# students = [
#     "Brian",
#     "Brandon",
#     "Zach",
#     "J.R.",
# ]
# # use this to change specific parts of list index without changing entire list
# students[2] = "Zac"

# # print student[0] -- get the first element in the list
# # print students[4] -- ERROR!
# # print students[-1] -- starts from the end of the list and goes through in reverse order 

# # All lists have a length you can find with len()
# numOfStudents = len(students)
# for i in range(0, numOfStudents):
#     print "Welcome to class, %s" % students[i]

# # make a list called nflTeams 
# teams = [
#     [
#         "Falcons",
#         "Panthers",
#         "Saints",
#         "Bucs",
#     ],
#     "Bills",
#     "Dolphins",
#     "49ers"
# ]

# print teams[0]
# # print list at index 0 
# print teams[0][0]
# # prints falcons

# # A tuple is a list whose elements CANNOT be changed
# # A tuple is made with () instead of []

# creat an empty list
atlanta_teams = []
# to add something to the end of a list 
# you can use the append
atlanta_teams.append("Falcons")
print atlanta_teams
atlanta_teams.append("Braves")
print atlanta_teams
atlanta_teams.append("Hawks")
print atlanta_teams
atlanta_teams.append("Thrashers")
print atlanta_teams

# use pop() to remove the last thing off a list, by default
# LISTNAME.pop() will remove the last element in a list
# LISTNAME.pop(3) will remove the 3th element in a list
atlanta_teams.pop()
print atlanta_teams
atlanta_teams.append("United")
print atlanta_teams

# A sort method for lists!
# .sort() will put them in natural order, alpha for strings, numerical for integers
# atlanta_teams.sort()
# print atlanta_teams

# if you want to sort, but not change the original
# you can use sorted(LISTNAME)
sortedAtlantaTeams = sorted(atlanta_teams)
print atlanta_teams
print sortedAtlantaTeams

# reserveSort is the .reverse(), changes the original list like .sort()
atlanta_teams.reverse()
print atlanta_teams

# if you have an array and you want to turn it into a list ...
# split

reindeer = "Dasher, Dancer, Prancer, Vixon"
# split expects a delimiter, the delimiter is what you want split to look for
# and each time it finds it, it will create a new element
reindeerAsAList = reindeer.split(", ")
print reindeerAsAList

# if you want part of a list, you use [x:y]
# this will create a copy of the array. it will not change 
# the original. it will start copying at the Xth indexand it will stop at the Yth.
# so if we want just Dancer, Prancer ...
dancerPrancer = reindeerAsAList[1:3] #inside the bracket is the index to start at and the index to stop at, NOT INCLUDING the stopped index
print dancerPrancer