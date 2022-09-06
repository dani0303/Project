import random

first_name = "Joe"
last_name = "Mama"

rand1 = random.randrange(0, len(first_name))
print(rand1)
rand2 = random.randrange(0, len(first_name))
print(rand2)

while rand1 == rand2:
	rand2 = random.randrange(0, len(first_name))
	print(rand2)

