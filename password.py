#!/usr/bin/python3
global code
code='@asmap'

def passwd_check():
    password = input("Enter your password")
    if password==code:
        print('Password Correct')
    else:
        print("Password Incorrect")



passwd_check()




