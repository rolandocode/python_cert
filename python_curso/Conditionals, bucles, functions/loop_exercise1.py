
import random;
names_count = 4

names = []

while len(names) < names_count:
    name = input ("Enter a name ")
    names.append(name)

randomName = names[random.randint(0, names_count-1)]

print (randomName)