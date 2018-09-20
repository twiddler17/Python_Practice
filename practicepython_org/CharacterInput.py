############################################################
#
#   File Name:          CharacterInput.py
#   Author:             George Sinitsyn (github: twiddler17)
#   Date create:        9/19/2018
#   Date last modified: 9/20/2018
#   Python Version:     3.6.1
#
#   Update: Modified to display num_times
#
############################################################

#Begin

#Importing datetime class from datetime module
from datetime import datetime

name_empty = True
age_empty = True
num_empty = True

while name_empty:
    name = input("What's your name?: ")
    if not name:
        pass
    else:
        name_empty = False

while age_empty:
    age = int(input("What's your age?: "))
    if not age:
        pass
    else:
        age_empty = False

while num_empty:
    num_times = int(input("Number of times to be displayed: "))
    if not num_times:
        pass
    else:
        num_empty = False

current_year = datetime.now().year

while num_times > 0:
    if age == 100:
        print(name + ", you are already 100 years old.")
    else:
        date_old = str(current_year + 100 - age)
        print(name + ", you will be 100 years old in " + date_old + ".")
    num_times -= 1

#End