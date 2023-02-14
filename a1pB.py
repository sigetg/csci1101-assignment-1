# Assignment 1 Problem B
#
# Write a program that does the reverse conversion of Problem A.  That is, your
# program reads in a single number of inches and converts it back to the
# corresponding number of yards, feet, and inches.  Note that you do not
# convert the number of inches separately into yards, then feet, then inches.
# Instead the program must calculate how many yards there are in the given
# number of inches, then convert the remaining inches into feet, and finally
# have the left over inches directly.  For example, if the user enters 50 for
# the total number of inches, your program should compute that that is equal to
# 1 yard, 1 foot, and 2 inches.
#
# Your input and output messages must conform to the following example: 
#
# Enter the number of inches: 50
# Number of yards = 1
# Number of feet = 1
# Number of inches = 2
#
# Note the order of outputs, capitalization of messages, spacing, etc

a=int(input("Inches:"))
print("yards:",a//36)
print("feet:",a%36//12)
print("inches:",a%36%12)
