############################################################
#
#   File Name:          all_divisers.py
#   Author:             George Sinitsyn (github: twiddler17)
#   Date create:        10/10/2018
#   Date last modified: 10/10/2018
#   Python Version:     3.6.1
#
#   Update: First commit.
#
############################################################

#Begin

num = int(input("Please enter a number: "))
divisors = []

for i in range(1, num + 1):
    if not num % i:
        print(i, end = ', ')

#End