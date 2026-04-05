import random

word_list = ["python", "developer", "hangman", "challenge", "programming"]

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

display = ["_"] * word_length
guessed_letters = []
lives = 6

print(" Welcome to Hangman!")
print("Word:", " ".join(display))

stages = [
r'''
  +---+
  |   |
      |
      |
      |
      |
=========
''',
r'''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''',
r'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''',
r'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
''',
r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''',
r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''',
r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
'''
]

game_over = False

while not game_over:
    guess = input("\nGuess a letter: ").lower()

    # Validate input
    if not guess.isalpha() or len(guess) != 1:
        print(" Please enter a single letter.")
        continue

    # Already guessed
    if guess in guessed_letters:
        print(" You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    # Correct guess
    if guess in chosen_word:
        for position in range(word_length):
            if chosen_word[position] == guess:
                display[position] = guess
        print(" Correct!")
    else:
        lives -= 1
        print(" Wrong!")

    # Show hangman stage
    print(stages[6 - lives])

    # Show progress
    print("Word:", " ".join(display))
    print("Guessed letters:", ", ".join(guessed_letters))

    # Win condition
    if "_" not in display:
        print("\n🎉 Congratulations! You WIN!")
        game_over = True

    # Lose condition
    if lives == 0:
        print("\n💀 Game Over! You LOSE!")
        print("The word was:", chosen_word)
        game_over = True