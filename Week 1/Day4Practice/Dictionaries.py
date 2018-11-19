# Dictionaries
# Dictionaries are just like lists
# Except instead of numbered indices, they have English indices
# A dictionary is like a list of variables
name = "greg"
gender= "male"
height = "tall"
job = "developer"

greg = [
    "Greg",
    "male",
    "tall",
    "developer"
]
# If you wanted to know Greg's job, you have to do greg[3]
# No one is  going to expect that

# ==== Key:Value Pair ====
# Key goes on the left 
greg = {
    "name": "Greg",
    "gender": "male",
    "height": "tall",
    "job": "developer"
}

# print greg["name"]
# print greg["job"]

# make a new dictionary
zombie = {} #dictionary
zombies = [] #list
# zombies.append() for lists
zombie['weapon'] = 'fist'
zombie['health'] = 100
zombie["speed"] = 10
# print zombie
# print zombie["weapon"]
# for key,value in zombie.items(): #items i a built in dictionary method so python knows how to fetch things
#     print "Zombie has a key of %s with a value of %s" % (key,value)

# dictionaries do not print out in the order you put them in
# you can force it to come out in a specific order with .iteritems()

# in our game, poor zombie loses his weapon, arm falls off
# we need to remove his 'weapon' key
del zombie['weapon'] #deletes key:value pairs from dictionary
# print zombie
is_nighttime = True
if(is_nighttime):
    zombie['health'] += 50
# put lists and dictionaries together
zombies = []
zombies.append({
    "name": "hank",
    'weapon': "baseball bat",
    "speed": 10
})
zombies.append({
    'name': "Willie",
    'weapon': "Axe",
    "speed": 3,
    "victims": [
        'squirrel',
        'rabbit',
        'racoon'
    ]
})

# if we wanted to know zombie1's weapon, how do we do that?
# print zombies[0]['weapon']
# zombie2's second victim is
print zombies[1]['victims'][1]
