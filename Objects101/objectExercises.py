class Person(object):
                #These are called parameters
    def __init__(self, name, email, phone): # this is a constructor
        self.name = name
        self.email = email
        self.phone = phone
        self.friends= []
        self.greeting = 0
    def greet(self, other_person):
        print 'Hello %s, I am %s!' % (other_person.name, self.name)
        self.greeting += 1
    
    def print_contact_info(self):
        print "%s's email: %s, %s's phone number: %s" % (self.name,self.email, self.name, self.phone)
    
    def add_friend(self, person):
        self.friends.append(person)
    
    def num_friends(self):
        print len(self.friends)

    def greeting_count(self):
        print self.greeting
    
    def __repr__(self):
        return '%s %s %s' % (self.name, self.email, self.phone) 
    
# # Write code to

# Instantiate an instance object of Person with name of 'Sonny', email of 'sonny@hotmail.com', and phone of '483-485-4948', store it in the variable sonny.
sonny = Person('Sonny', 'sonny@hotmail.com', '483-485-4948')
                #These are called arguments
# Instantiate another person with the name of 'Jordan', email of 'jordan@aol.com', and phone of '495-586-3456', store it in the variable 'jordan'.
jordan = Person('Jordan', 'jordan@aol.com', '495-586-3456')
# Have sonny greet jordan using the greet method.
sonny.greet(jordan)
# Have jordan greet sonny using the greet method.
jordan.greet(sonny)
# Write a print statement to print the contact info (email and phone) of Sonny.
print sonny.email, sonny.phone
# Write another print statement to print the contact info of Jordan.
print jordan.email, jordan.phone

class Vehicle(object):
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
    def print_info(self):
        print self.year, self.make, self.model

# myCar = Vehicle("Ford", 'F150', 2014)
# myCar.print_info()

# sonny.print_contact_info()
# sonny.friends.append(jordan)
# print len(sonny.friends)
# sonny.num_friends()
# sonny.add_friend(jordan)
# sonny.num_friends()
# sonny.greeting_count()
# sonny.greet(jordan)
# sonny.greeting_count()
print sonny
print jordan

# Primitive Data types: integer, float, string, boolean

# 3 Abstract Data types

# dictionary: diction['key']
# diction = {
#     "key": "value"
# }

# list: aList[0]
# aList = [
#     "value",
#     "joe",
#     "222"
# ]

# object = sonny.name
# we define with the class keyword
# and then we instantiate an object by calling the class
# classes have constructor functions(__init__), its run on creation
# and sets self variables
# objects use . notation (sonny.name)

# the really big differences between classes and dictionaries:
# 1. classes have a schema
# 2. classes have methods built in