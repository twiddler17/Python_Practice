############################################################
#
#   File Name:          string_lists.py
#   Author:             George Sinitsyn (github: twiddler17)
#   Date create:        10/31/2018
#   Date last modified: 11/7/2018
#   Python Version:     3.7.0
#
#   Update: Final
#
############################################################

#My way too overcomplicated way

#Begin

#Functions


def reverse(w):
    rev_w = ''
    for i in range(len(w) - 1, -1, -1):
        rev_w += w[i]
    return rev_w

word = input("Please enter a word: ")
rev_word = reverse(word)
print("Reversed: " + rev_word)
if word == rev_word:
    print(word, "is a palindrome")
else:
    print(word, "is not a palindrome")

"""
#End

#Best Way

#Begin

wrd=input("Please enter a word")
wrd=str(wrd)
rvs=wrd[::-1]
print(rvs)
if wrd == rvs:
    print("This word is a palindrome")
else:
    print("This word is not a palindrome")

#End

"""