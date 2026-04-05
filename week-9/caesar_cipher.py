import string

alphabet = list(string.ascii_lowercase)

def caesar_cipher(text, shift, direction):
    result = ""

    shift = shift % 26

    if direction == "decode":
        shift *= -1

    for char in text:
        if char in alphabet:
            index = alphabet.index(char)
            new_index = index + shift
            result += alphabet[new_index % 26]
        else:
            result += char  

    return result


print(" Caesar Cipher Program")

while True:
    direction = input("\nType 'encode' to encrypt, 'decode' to decrypt: ").lower()
    
    if direction not in ["encode", "decode"]:
        print("Invalid choice.")
        continue

    text = input("Enter your message: ").lower()
    shift = input("Enter shift number: ")

    if not shift.isdigit():
        print("Shift must be a number.")
        continue

    shift = int(shift)

    result = caesar_cipher(text, shift, direction)

    print(f"\nResult: {result}")

    restart = input("\nDo you want to continue? (yes/no): ").lower()
    if restart != "yes":
        print("Goodbye")
        break