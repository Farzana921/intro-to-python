print("Welcome to Split the Bill!")

# input
total_bill = float(input("What was the total bill? $"))

tip_percentage = int(input("What percentage tip would you like to give? 10 / 12 / 15 "))

people = int(input("How many people to split the bill? "))

tip_amount = total_bill * tip_percentage / 100

total_with_tip = total_bill + tip_amount

each_person = total_with_tip / people

# result
print(f"Each person should pay: ${round(each_person, 2)}")
