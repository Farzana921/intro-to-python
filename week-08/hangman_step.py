chosen_word = "fox"
guess = "x"
# TODO 4: create placeholder
placeholder = ""
for letter in chosen_word:
    placeholder += "_"

print("Placeholder:", placeholder)
# TODO 5: create display
display = ""
for letter in chosen_word:
    if letter == guess:
        display += letter
    else:
        display += "_"

print("Display:", display)