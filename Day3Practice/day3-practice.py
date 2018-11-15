# ======BASIC STRING MANIPULATION======



# randomString = "hello world"
# print randomString
# print randomString.upper()
# print randomString.capitalize()
# reverseString = randomString [::-1]
# print reverseString

# ====LEETSPEAK====

# myParagraph = "Sometime we can feel a bit dull in the morning and we need to produce our own sunshine energy."
# leetSpeak = (("A", "4"), ("E", "3"), ("G", "6"), ("I", "1"), ("O", "0"), ("S", "5"), ("T", "7"),("a", "4"), ("e", "3"), ("g", "6"),("i", "1"), ("o", "0"),("s", "5"), ("t", "7"))
# myParagraphUpper = myParagraph.upper()
# leetParagraph = myParagraphUpper
# for i, j in leetSpeak:
#     leetParagraph = myParagraphUpper.replace(i, j)

# print leetParagraph


# ====LONG VOWELS====

# userString = raw_input("Give me a word. ")
# print userString
# stringAsAList = list(userString)
# stringLength = len(stringAsAList)
# lowerCaseVowel = ["a", "e", "i", "o", "u"]
# for i in range(0, stringLength):
#     print stringAsAList[i]
#     for j in lowerCaseVowel:
#         if i == j:
#             print "Sweet!"
# print ''.join(stringAsAList)



# ====CAESAR CIPHER====

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
encryptedMessage = "lbh zhfg hayrnea jung lbh unir yrnearq"

