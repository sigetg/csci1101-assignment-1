# Assignment 1 Problem A 
#
# Write a program to do basic unit conversion for measurements.  Specifically,
# your program will prompt the user for a number of yards, a number of feet,
# and a number of inches.  Assume that all user inputs are non-negative whole
# numbers (i.e., non-negative integers).  Your program must compute the total
# number of inches by converting each of the three inputs into inches and
# adding them together.  Finally, print out the total length in inches.  Recall
# that 1 yard = 3 feet, and 1 foot = 12 inches.
#
# Your input and output messages must conform to the following example: 
#
# Enter the number of yards: 1 
# Enter the number of feet: 2 
# Enter the number of inches: 3 
# Total number of inches = 63
#
# Note the order of inputs, capitalization of messages, spacing, etc. 

a = int(input("Yards:"))
b = int(input("Feet:"))
c = int(input("Inches:"))


print("feet:",a*3)
print("inches:",b*12)
print("total inches:",a*36+b*12+c)
