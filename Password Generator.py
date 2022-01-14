'''
Project Title: Password Generator
Project Goal: A generator that suggests if a user's inputted password is either weak, decent, or strong.
'''

import math

#Function 1


#main
def ascii_name_plaque(name):
    '''
    (name)->name
    Preconditions: must multiply star by total amount of characters in given name
    Returns: a box made of stars with a _name_ in the center of it
    '''
    fandl= len(name)+8
    print("*"*fandl)
    print("*" + " " *(fandl-2) + "*")
    print("*" + " " + " _" +name+ "_" + "  *")
    print("*" + " " *(fandl-2) + "*")
    print("*"*fandl)

ascii_name_plaque("YO")

name=input("What is your name?")

ascii_name_plaque("Alright " + name + ", let us try and create a password. Remember, you must have at least one of each type of character with a capital letter.")

password=input("Now, please enter your password")

#conditions:
#- If all the characters in the password are simply either letters, numbers,or only one type of character, that password is deemed weak
#- If all
#
#
#
#
#
#
#
#
#
#
