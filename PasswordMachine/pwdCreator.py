import random

special_char = ['!', '@', '#', '$', '%', '&', '*', '~', '-', '_', '+', '=']

class Creator:#constructor
    def __init__ (self, p1, p2, p3):#pwd is a password passed as a string
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

    """
    #p1 user's name
    #p2 user's birthyear
    #p3 parents birthyear
    """

    def new_pwd(self):#method accessor
        str_p1 = len(self.p1)
        rand1 = random.randrange(0, str_p1)
        new_str1 = self.p1[rand1:]

        int_str = str(self.p2)
        str_p2 = len(int_str)
        rand2 = random.randrange(0, str_p2)
        new_str2 = int_str[rand2:]

        int_str2 = str(self.p3)
        str_p3 = len(int_str2)
        rand3 = random.randrange(0, str_p3)
        new_str3 = int_str2[rand3:]

        random_char = random.randrange(0, len(special_char))
        random_char2 = random.randrange(0, len(special_char))

        new_password = new_str1 + new_str2 + new_str3 + special_char[random_char] + special_char[random_char2]

        return new_password
