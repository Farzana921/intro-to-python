# who open the door ?

import random 
names = ["Farzana", "Fatema", "Nargis", "Roya", "Maryam"]
door_opener = random.choice(names)
names.remove(door_opener)

door_holder = random.choice(names)

print(" Door Opener:", door_opener)
print(" Door Holder:", door_holder)

print(door_opener + " opens the door like a hero! 🦸‍♀️")
print(door_holder + " holds the door with style! 😎")
