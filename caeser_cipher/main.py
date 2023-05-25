# This is a sample Python script.

def caeser(plain_text,shift_index,direction):
    cipher_text = ""
    if direction == "decode":
        shift_index *= -1
    for letter in plain_text:
        if letter in alphabet:
            x = alphabet.index(letter)
            new_position = x + shift_index
            if new_position > 25:
                cipher_text += alphabet[new_position-26]
            else:
                cipher_text += alphabet[new_position]
        else:
            cipher_text += letter
    print(f"the {direction}d text is: {cipher_text}")

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
option = True
while option == True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    shift = shift % 26

    caeser(text,shift,direction)
    choice = input("enter 'yes' to continue, 'no' to exit\n")
    if choice == "yes":
        option = True
    else:
        option = False
        print("goodbye")



