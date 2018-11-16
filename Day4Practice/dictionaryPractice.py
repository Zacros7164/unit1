# Given the following dictionary, representing a mapping from names to phone numbers:

phonebook_dict = {
  'Alice': '703-493-1834',
  'Bob': '857-384-1234',
  'Elizabeth': '484-584-2923'
}
# Write code to do the following:

# Print Elizabeth's phone number.
print 

# Add a entry to the dictionary: Kareem's number is 938-489-1234.
# Delete Alice's phone entry.
# Change Bob's phone number to '968-345-2345'.
# Print all the phone entries.
# In this exercise, are you using dynamic keys or fixed keys?

# Exercise 2: Nested Dictionaries
# ramit = {
#   'name': 'Ramit',
#   'email': 'ramit@gmail.com',
#   'interests': ['movies', 'tennis'],
#   'friends': [
#     {
#       'name': 'Jasmine',
#       'email': 'jasmine@yahoo.com',
#       'interests': ['photography', 'tennis']
#     },
#     {
#       'name': 'Jan',
#       'email': 'jan@hotmail.com',
#       'interests': ['movies', 'tv']
#     }
#   ]
# }
# Write a python expression that gets the email address of Ramit.
# Write a python expression that gets the first of Ramit's interests.
# Write a python expression that gets the email address of Jasmine.
# Write a python expression that gets the second of Jan's two interests.
# In this exercise, are you using dynamic keys or fixed keys?

# Letter Summary
# Write a letter_histogram function that takes a word as its input, and returns a dictionary containing the tally of how many times each letter in the alphabet was used in the word. For example:

# >>> letter_histogram('banana')
# {'a': 3, 'b': 1, 'n': 2}
# In this exercise, are you using dynamic keys or fixed keys?

# Word Summary
# Write a word_histogram function that takes a paragraph of text as its input, and returns a dictionary containing the tally of how many times each letter in the alphabet was used in the text. For example:

# >>> word_histogram('To be or not to be')
# {'to': 2, 'be': 2, 'or': 1, 'not': 1}
# In this exercise, are you using dynamic keys or fixed keys?

# Bonus Challenge
# Given a histogram tally (one returned from either letter_histogram or word_summary), print the top 3 words or letters.

# Super Bonus Challenge
# Given a list (example below), create a function that takes the list and returns a dictionary that has a key "one," "two," "three," and so on. Assign the value for each key to be a list of however many times a value shows up in the list. 

# list1 = [1,45,65,4,45,"Jim",1,"Jim",3,4,1,1,True,3,45,4,1,"The Beetles",9]

# The output shoudl be:

# final_dictionary = {
#     'one': ["The Beetles",9,True,65]
#     'two': ["Jim",3]
#     'three': [45,4]
#     'five': [1]
# }
# Ultra Bonus Challenge
# Do the super bonus with multiple lists.