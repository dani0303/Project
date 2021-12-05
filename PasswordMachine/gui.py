import pyfiglet
from pwdCreator import Generator

title = pyfiglet.figlet_format("Welcome to the PasswordEater", font="slant")

print("**************************************************************************************************************************\n")
print(title)
print("**************************************************************************************************************************\n")

while True:
    try:
        password = input("Enet your current password (making it long): ")
        if len(password) <= 1:
            raise ValueError
        else:
            pwd = Generator(password)
            print(pwd.new_pwd())

    except ValueError:
        print("Give me a password that will fit!")
