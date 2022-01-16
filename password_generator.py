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

password=input(str(("Now, please enter your password betweem 9-25 characters.")))

    '''
flag = True
while flag:
count = 0
    '''
    if len(password) < 9:
        print("Sorry, your password is too short. Please try in between 9 and 25 characters.")
        
    elif len(password) > 25:
        print("Sorry, your password is too lengthy. Please try in between 9 and 25 characters.")
            
    elif (password == "" ) or (password == "" ) or (password == "" ):
        print("Sorry your password is too WEAK! Please try again:) ")

    elif ("" in password) and ("" in password) and ("" in password):
        print("Not bad, your password is decent. Not good enough though, Try again.")

    elif ("" in password) and ("" in password) and ("" in password):
        print("Noice, your password is strong! Now you have an ironclad password to protect you from Hackers.")

#conditions:
# The password must be from 9-25 characters in length
#- If all the characters in the password are simply either letters, numbers,or only one type of a character, that password is deemed weak
#- If the password
#
#
#
#
#
#
#
#- If the password has a consistent combination of letters(at least 4), numbers(at least 4) and special characters(at least 2), then the password is deemed Strong
# Have special characters replaced for certain letters for example, the letter "a" can be "@" or the letter "o" can be "0"
# After 10 tries, the UI will suggest a new password through a series of questions in which it will createa new password based off the questions
