import random

pwd = "Codejbngjk32#@$@$"
numChar = len(pwd)#gets length of the string
rand = random.randrange(0, numChar/2)#get a random num within parameters
p1 = pwd[rand:]#gets substring
new_password = p1 + pwd
print(new_password)
