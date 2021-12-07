import pyfiglet
from pwdCreator import Creator

title = pyfiglet.figlet_format("Welcome to the PasswordEater", font="slant")

print("**************************************************************************************************************************\n")
print(title)
print("==========================================================================================================================\n")
print("Created by Daniel Rodriguez 12/4/2021")
print("**************************************************************************************************************************\n")

while True:
    try:

        p1 = input("Before we make your password what is your name?: ")
        if type(p1) == int:
            raise ValueError

        p2 = int(input("What year were u born?: "))
        if type(p2) != int:
            raise ValueError

        p3 = int(input("What year was one of your parents born?: "))
        if type(p3) != int:
            raise ValueError

        pwd = Creator(p1, p2, p3)
        print(pwd.new_pwd())

    except ValueError:
        print("invalid")
