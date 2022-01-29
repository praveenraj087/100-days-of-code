

import caesarcipher_art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print(caesarcipher_art.logo)
toContinue = True


def caesar(text, shift, direction):
    end_text = ""

    shift = shift % 26

    if(direction == "encode"):
        for letter in text:
            if(letter not in alphabet):
                end_text += letter
            else:
                pos = alphabet.index(letter)
                new_pos = pos+shift
                new_letter = alphabet[new_pos]
                end_text += new_letter
        print(f"The encoded text is {end_text}")
    if(direction == "decode"):
        for letter in text:
            if(letter not in alphabet):
                end_text += letter
            else:
                pos = alphabet.index(letter)
                new_pos = pos-shift
                new_letter = alphabet[new_pos]
                end_text += new_letter
        print(f"The decoded text is {end_text}")


while toContinue:
    direction = input(
        "Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(text, shift, direction)
    decision = input("Do you want to continue? Yes or no ").lower()
    if(decision == "yes"):
        toContinue = True
    else:
        toContinue = False
