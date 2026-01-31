print("Welcome to Pizza Deliveries!")

bill = 0
# Ask for pizza size
size = input("What size pizza do you want? S, M, or L: ")
if size == "S":
    bill = 15
elif size == "M":
    bill = 20
elif size == "L":
    bill = 25
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
if pepperoni == "Y":
    if size == "S":
        bill += 1
    else:
        bill += 2
# Ask for extra cheese
extra_cheese = input("Do you want extra cheese? Y or N: ")

if extra_cheese == "Y":
    bill += 1

# result
print(f"Your final bill is: ${bill}.")
