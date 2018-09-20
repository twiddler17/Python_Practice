############################################################
#
#   File Name:          CharacterInput.py
#   Author:             George Sinitsyn (github: twiddler17)
#   Date create:        9/19/2018
#   Date last modified: 9/19/2018
#   Python Version:     3.6.1
#
############################################################

#Begin

#Importing datetime class from datetime module
from datetime import datetime

name_empty = True
age_empty = True

while name_empty == True:
    print("What's your name?:", end = " ")
    name = input()
    if not name:
        print("Please enter your name:")
    else:
        name_empty = False

while age_empty == True:
    print("What's your age?:", end = " ")
    age = int(input())
    if not age:
        print("Please enter your age:")
    else:
        age_empty = False

current_year = datetime.now().year

if age == 100:
    print(name + ", you are already 100 years old.")
else:
    date_old = str(current_year + 100 - age)
    print(name + ", you will be 100 years old in " + date_old + ".")

#End