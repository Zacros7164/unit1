# Uppercase a String
# Given a string, print the string uppercased. #string #easy

# aString = "sweet"
# print aString.upper()

# Capitalize a String
# Given a string, print the string capitalized. #string #easy

# print aString.capitalize()

# Reverse a String
# Given a string, print the string reversed.

# print aString[::-1]

# -----

# aStringAsList = list(aString)
# aStringAsList.reverse()
# print ''.join(aStringAsList)

# ----

# print aString[0]
# lengthOfString = len(aString)
# print lengthOfString
# reversedString = ""
# for i in range(0, lengthOfString):
#     reversedString += aString[lengthOfString-(i+1)]
# print reversedString

# Leetspeak
# Given a paragraph of text as a string, print the paragraph in leetspeak. To translate a string to leetspeak, you need to replace make the following character replacements (treat all input characters as uppercase):

# A => 4
# E => 3
# G => 6
# I => 1
# O => 0
# S => 5
# T => 7
# Example: Leet => l337

# leetDict = {
#     "A": 4,
#     "E": 3,
#     "G": 6,
#     "I": 1,
#     "O": 0,
#     "S": 5,
#     "T": 7
# }
# leetString = "Sean McQuaid"
# newString= leetString.upper()
# finalString = ""
# for i in range(0,len(newString)):
#     currentLetter = newString[i]
#     # print currentLetter
#     if(currentLetter in leetDict):
#         currentLetter = leetDict[currentLetter]
#     finalString += str(currentLetter)
# print finalString

# Long-long Vowels
# Given a word as a string, print the result of extending any long vowels to the length of 5. Examples:

# Good => Goooood
# Cheese => Cheeeeese
# Man => Man
# Spoon => Spooooon

# vowels = "AEIOUeiou"
# numVal = 0
# vSet = set(vowels)
# # print vSet
# rendWord = []
# impWord = raw_input("Please enter a word. ")
# for letter in impWord:
#     if letter in vSet:
#         numVal += 1
#         rendWord.append(letter)
#         if numVal == 2:
#             rendWord.append((letter)*3)
#     else:
#         numVal = 0
#         rendWord.append(letter)
# wordRendered = "".join(rendWord)
# print wordRendered

# vowelDict = {
#     "a": "aaaaa",
#     "e": "eeeee",
#     "i": "iiiii",
#     "o": "ooooo",
#     "u": "uuuuu"
# }
# longVowelStr = ""
# for i in range(0,len(impWord)):
#     currentLetter = impWord[i]
#     nextLetter = impWord[i +1]
#     if(currentLetter == nextLetter) and (i != len(impWord)-1):
#         if(currentLetter in vowelDict):
#             currentLetter = vowelDict[currentLetter]
#         longVowelStr += currentLetter
# print longVowelStr    

# Caesar Cipher
# Given a string, print the Caesar Cipher (or ROT13) of that string. What is Caesar Cipher? http://practicalcryptography.com/ciphers/caesar-cipher/

# Use your solution to decipher the following text: "lbh zhfg hayrnea jung lbh unir yrnearq"