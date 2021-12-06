"""
What I would like to do next is making it spit out the changed password
but have the same amount of characters from the first one
"""

import random
class Creator:
    def __init__ (self, pwd):#pwd is a password passed as a string
        self.pwd = pwd

    def new_pwd(self):
        numChar = len(self.pwd)
        rand = random.randrange(0, numChar)#get a random num within parameters
        p1 = self.pwd[rand:]#gets substring
        p2 = self.pwd[int(rand/2):]
        new_password = p1 + p2
        return "new password is " + new_password
