import random

letters = "abcdeABCDE"
numbers = "0123456789"
symbols = "!@#"

password = ""

a = int(input("How many letters? "))
b = int(input("How many numbers? "))
c = int(input("How many symbols? "))

for i in range(a):
    password = password + random.choice(letters)

for i in range(b):
    password = password + random.choice(numbers)

for i in range(c):
    password = password + random.choice(symbols)

print(password)