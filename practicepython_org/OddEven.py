############################################################
#
#   File Name:          OddEven.py
#   Author:             George Sinitsyn (github: twiddler17)
#   Date create:        9/21/2018
#   Date last modified: 9/21/2018
#   Python Version:     3.6.1
#
#   Update: First Commit.
#
############################################################

#Begin

#Part 1

#Input
num = int(input("Please enter a number: "))

#Checking remainder
if not num % 4:
    print(num, "is divisible by 4")
elif not num % 2:
    print(num, "is an even number")
else:
    print(num, "is an odd number")

#Part 2

#Input
num = int(input("Please enter a number: "))
div = int(input("Please enter the divider: "))

#Division
if not num % div:
    print(num, "is divisible by", div, "and equals to", int(num / div))
else:
    print(num, "will not evenly divide by", div)