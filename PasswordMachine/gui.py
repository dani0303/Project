import pyfiglet
from pwdCreator import Creator
from datetime import datetime

today = datetime.now()
title = pyfiglet.figlet_format("Welcome to the PasswordEater", font="slant")

print("**************************************************************************************************************************\n")
print(title)
print("==========================================================================================================================\n")
print("Created by Daniel Rodriguez 12/4/2021")
print("**************************************************************************************************************************\n")

while True:
    try:
        p1 = input("Before we make your password what is your name?: ")
        #the purpose of this recursion is to go through every character that is
        #inside the string and return an ValueError if it contains a digit
        for character in p1:
            if character.isdigit():
                raise ValueError

        p2 = int(input("What year were u born?: "))
        if type(p2) != int:
            raise ValueError

        p3 = int(input("What year was one of your parents born?: "))
        if type(p3) != int:
            raise ValueError

        pwd = Creator(p1, p2, p3)
        password = pwd.new_pwd()
        print("Your new password is: " + password)
        passwords_file = open("passwords.txt", "a")
        passwords_file.write(password)
        passwords_file.write("\n")
        passwords_file.close()
        break

    except ValueError:
        print("invalid")
