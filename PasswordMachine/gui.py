import pyfiglet
from pwdCreator import Creator

title = pyfiglet.figlet_format("Welcome to the PasswordEater", font="slant")


print("**************************************************************************************************************************\n")
print(title)  
print("==========================================================================================================================\n")
print("Created by Daniel Rodriguez 12/4/2021")
print("**************************************************************************************************************************\n")

while True:
    password = input("Enet your current password (making it long): ")
    pwd = Creator(password)
    print(pwd.new_pwd())
