############################################################
#
#   File Name:          Lower_Than.py
#   Author:             George Sinitsyn (github: twiddler17)
#   Date create:        10/3/2018
#   Date last modified: 10/3/2018
#   Python Version:     3.7.0
#
#   Update: First Commit
#
############################################################

#Begin

#Part 1

list1 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
list2 = []

for x in list1:
    if x < 5: print(x, end = ' ')

print()
#Part 2

for x in list1:
    if x < 5: list2.append(x)

for x in list2: 
    print(x, end = ' ')

print()

#Part 4

list2.clear()

less_num = int(input("Please enter a number: "))

for x in list1:
    if x < less_num: list2.append(x)

for x in list2: 
    print(x, end = ' ')

#End