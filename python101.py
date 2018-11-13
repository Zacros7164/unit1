# print "Hello, World";

# print """
# It was a dark and stormy night.
#     A murder happened.
# """;

# # comment wth python using a hashtag
# # highlight what you want and use command / to turn highlighted portion into a comment. most text editors will use this shortcut

# # variables
# # - strings, letters, numbers, or any other stuff
# # you can make with a keyboard

# # variables do not make a program faster.
# # they make the program slower.
# # variables make it easier for us to write a program.

# # This is how you declare a variable
# theBestClass = "the 11-18 immersive"
# print theBestClass

# # Data types
# # - Programming languages see different types of varibles differently
# # - string = English stuff.
# # - Number = something with a number or a - or e for standard notation.
# #     - floats = decimal point in the number
# #     - integers = whole number (no decimal point)
# # - Booleans = true or false, on or off, 1 or 0
# # - list = a bunch of things in one variable, most other languages call this an array
# # - Dictionaries = a variable of variables
# # - Objects - super dictionaries 

# # Primitvie Data types = String, Numbers, Booleans (like base elements hydrogen, oxygen, etc)
# # Abstract data types = List, Dictionaries, Objects (things made up of primitive dtata types, like H2O OR NaCl)
# month = "November"
# print type(month)
# date = 13
# print type(date)
# dateAsfloat = 13.0
# print type(dateAsfloat)
# aBool = True 
# print type(aBool)
# aList = []
# print type(aList)
# aDictionary = {}
# print type(aDictionary)

# # concatenate is programming speak for add things together
# first = "Zac"
# last = "Crosby"
# fullName = first + last
# fullName = first + " " + last
# print fullName

# # fourteen = 10 + 4
# # print fourteen

# # cast = change a variable to a new data type
# fourteen = int("10") + 4
# print fourteen

# Math = +, -, /, *, %
# print 2+2
# print 2-2
# print 2/2
# print 2*2
# # % = modulus, Modulus divides the number and gives you the remainder
# print 2%2 
# print 2%3
# print 2**3
# just like concatenation the multiplication symbol can be used to replicate a string multiple times
# a string and a * and a number = give me X strings 
# print "-" * 20

# python does not have a simple incrementer
# num = 1;
# num ++
# num += 1;

# Input 
# python 2 = raw_input
# python 3 = input
# name = raw_input("What is your name? ")
# print type(name)

# Conditionals
# a single = sign, means set the left to whatever is on the right
# 2 = signs, means compare what's on the left to whatever is on the right

print 2 == 2
print 2 == 1
print 2 == "2"
secretNumber = 5;
if(secretNumber == 3):
    print "Secret number is 3";
else:
    print "Secret number is not 3";

game_on = True;
i = 0;
while(game_on):
    i += 1
    if(i == 10):
        game_on = False
    else:
        print "Game on!"
print "Loop exited!"