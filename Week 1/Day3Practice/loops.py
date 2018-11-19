# 1 to 10
# Using a for loop and the range function, print out the numbers between 1 and 10 inclusive, one on a line. Example output:

# $ python 1_to_10.py
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10
# n to m
# Same as the previous problem, except you will prompt the user for the number to start on and the number to end on. Example session:

# $ python n_to_m.py
# Start from: 2
# End on: 8
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# Odd Numbers
# Print each odd number between 1 and 10 inclusive. Example output:

# $ python odd_numbers.py
# 1
# 3
# 5
# 7
# 9
# Hint: you will need to use the modulus operator % to determine whether a number is odd or even.

# Print a Square
# Print a 5x5 square of * characters. Example output:

# $ python square.py
# *****
# *****
# *****
# *****
# *****
# Print a Square II
# Print a NxN square of * characters. Prompt the user for N. Example output:

# $ python square2.py
# How big is the square? 10
# **********
# **********
# **********
# **********
# **********
# **********
# **********
# **********
# **********
# **********
# Print a Box
# Given a height and width, input by the user, print a box consisting of * characters as its border. Example session:

# $ python box.py
# Width? 6
# Height? 4
# ******
# *    *
# *    *
# ******

# width = int(raw_input("What is the width of the box? "))
# height = int(raw_input("What is the height of the box? "))
# print "* " * width
# for i in range(0, height+1):
#     i = i-2
#     print "* " + "  " * (width-2) + "*"
# print "* " * width


# Print a Triangle
# Print a triangle consisting of * characters like this:

#    *
#   ***
#  *****
# *******
# Print a Triangle II
# Given a number as the height, print a triangle as in "Print a Triangle" but with the given height.

# p = int(raw_input("How big is your triangle? "))
# p = p+1
# for i in range(1,p,2):
#     print " "*p+i*"*"
#     p -= 1

# Multiplication Table
# Print the multiplication table for numbers from 1 up to 10. Example output:

# $ python multiplication_table.py
# 1 X 1 = 1
# 1 X 2 = 2
# 1 X 3 = 3
# 1 X 4 = 4
# ...
# 5 X 5 = 25
# 5 X 6 = 30
# 5 X 7 = 35
# ...
# 10 X 8 = 80
# 10 X 9 = 90
# 10 X 10 = 100

# for i in range(1, 11):
#     for j in range(1,11):
#         answer = i*j
#         print "%i x %i = %i" % (i, j, answer)


# Bonus: Print a Banner
# Given a string, input by the user, print that string with a box around it. The box should stretch to the length of the string. Example session:

# $ python banner.py
# Text? Welcome to DigitalCrafts
# ****************************
# * Welcome to DigitalCrafts *
# ****************************





