import random
class Generator:
    def __init__ (self, pwd):#pwd is a password passed as a string
        self.pwd = pwd

    def create_new_pwd(pwd):
        numChar = len(pwd)#gets length of the string
        rand = random.randrange(0, numChar/2)#get a random num within parameters
        p1 = pwd[rand:]#gets substring
        new_password = p1 + pwd
        return new_password
