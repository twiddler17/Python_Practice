############################################################
#
#   File Name:          list_overlap.py
#   Author:             George Sinitsyn (github: twiddler17)
#   Date create:        10/10/2018
#   Date last modified: 10/10/2018
#   Python Version:     3.6.1
#
#   Update: First commit.
#
############################################################

#Begin

a = {1, 2, 3, 3}
b = {2, 3, 4, 5}
c = []

for i in a:
    if i in b: c.append(i)

print(c)

#End