import random

rock = r"""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = r"""
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors = r"""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

game_images = [rock, paper, scissors]
names = ["Rock", "Paper", "Scissors"]

while True:
    user_input = input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors (q to quit): ")

    if user_input.lower() == "q":
        print("Bye! 👋")
        break

    if not user_input.isdigit():
        print("Invalid input. Please type 0, 1, or 2.")
        continue

    user_choice = int(user_input)

    if user_choice < 0 or user_choice > 2:
        print("You typed an invalid number, you lose!")
        continue

    print(f"\nYou chose: {names[user_choice]}")
    print(game_images[user_choice])

    computer_choice = random.randint(0, 2)
    print(f"Computer chose: {names[computer_choice]}")
    print(game_images[computer_choice])

    # winner
    if user_choice == computer_choice:
        print("It's a draw!\n")
    elif (user_choice == 0 and computer_choice == 2) or \
         (user_choice == 2 and computer_choice == 1) or \
         (user_choice == 1 and computer_choice == 0):
        print("You win!\n")
    else:
        print("You lose!\n")
