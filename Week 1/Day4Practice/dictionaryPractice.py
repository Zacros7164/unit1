# Given the following dictionary, representing a mapping from names to phone numbers:

# phonebook_dict = {
#   'Alice': '703-493-1834',
#   'Bob': '857-384-1234',
#   'Elizabeth': '484-584-2923'
# }
# Write code to do the following:

# Print Elizabeth's phone number.
# phoneNumber = phonebook_dict['Elizabeth']
# print "Elizabeth's phone number is %s" % phoneNumber

# Add a entry to the dictionary: Kareem's number is 938-489-1234.
# phonebook_dict['Kareem'] = '938-489-1234'
# # print phonebook_dict['Kareem']
# # Delete Alice's phone entry.
# del phonebook_dict['Alice']
# print phonebook_dict
# Change Bob's phone number to '968-345-2345'.
# phonebook_dict['Bob'] = '968-345-2345'
# print phonebook_dict

# Print all the phone entries.
# print phonebook_dict
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
# print ramit['email']

# Write a python expression that gets the first of Ramit's interests.
# print ramit['interests']

# Write a python expression that gets the email address of Jasmine.
# print ramit['friends'][0]['email']

# Write a python expression that gets the second of Jan's two interests.
# print ramit['friends'][1]['interests'][1]

# In this exercise, are you using dynamic keys or fixed keys?
# fixed?


# Letter Summary

# Write a letter_histogram function that takes a word as its input, and returns a dictionary containing the tally of how many times each letter in the alphabet was used in the word. For example:

# >>> letter_histogram('banana')
# {'a': 3, 'b': 1, 'n': 2}
# In this exercise, are you using dynamic keys or fixed keys?
# # first gets word from user
impWord = raw_input("Please give me a word. ").lower()
# init empty dictionary
histogram_dict = {}
# iterates through word for each character
for i in impWord:
    # if i is already in histogram_dict, add one to the value for key i
    if i in histogram_dict:
        histogram_dict[i] += 1
    # if i is not already in histogram_dict, add the key i to the dictionary with a value of 1
    else:
        histogram_dict[i] = 1
# print the dictionary out
print histogram_dict


   
# Word Summary
# Write a word_histogram function that takes a paragraph of text as its input, and returns a dictionary containing the tally of how many times each letter in the alphabet was used in the text. For example:

# >>> word_histogram('To be or not to be')
# {'to': 2, 'be': 2, 'or': 1, 'not': 1}
# In this exercise, are you using dynamic keys or fixed keys?

# # First get a phrase from the user
# userPhrase = raw_input("Please enter a phrase. ")
# # Split userPhrase into a list
# userList = userPhrase.split(" ")
# # init an empty dictionary for the new histogram
# countHistogram = {}
# for i in userList:
#     if i in countHistogram:
#         countHistogram[i] += 1
#     else:
#         countHistogram[i] = 1
# print countHistogram


# Bonus Challenge
# Given a histogram tally (one returned from either letter_histogram or word_summary), print the top 3 words or letters.

## first gets word from user
# impWord = raw_input("Please give me a word. ") 
# histogram_dict = {}
# for i in impWord:
#     if i in histogram_dict:
#         histogram_dict[i] += 1
#     else:
#         histogram_dict[i] = 1
# print histogram_dict

# Super Bonus Challenge
# Given a list (example below), create a function that takes the list and returns a dictionary that has a key "one," "two," "three," and so on. Assign the value for each key to be a list of however many times a value shows up in the list. 

# list1 = [1,45,65,4,45,"Jim",1,"Jim",3,4,1,1,True,3,45,4,1,"The Beetles",9]
# sortedList1 = sorted(list1)
# print sortedList1
# final_dictionary = {}
# for i in sortedList1:
#     if i in 



# final_dictionary = {
#     'one': ["The Beetles",9,True,65]
#     'two': ["Jim",3]
#     'three': [45,4]
#     'five': [1] 
# }
# Ultra Bonus Challenge
# Do the super bonus with multiple lists.