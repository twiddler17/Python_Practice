############################################################
#
#   File Name:          string_lists.py
#   Author:             George Sinitsyn (github: twiddler17)
#   Date create:        10/31/2018
#   Date last modified: 10/31/2018
#   Python Version:     3.7.0
#
#   Update: First Commit
#
############################################################

#Begin

#Functions

def reverse(w):
    rev_w = []
    for i in range(len(w) - 1, -1, -1):
        rev_w.append(w[i])
    return rev_w

word = input("Please enter a word: ")
rev_word = reverse(word)
rev_word = ''.join(str(i) for i in rev_word)
if(word == rev_word):
    print(word, "is a palindrome")
else:
    print(word, "is not a palindrome")


#End