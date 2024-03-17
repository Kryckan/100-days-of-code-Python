import os

import art
import letters

cont = True


# Encryption
def encrypt(text, shift):
    encryptMessage = []
    for letter in text:  # itterate through the message
        if letter not in letters.alphabet:  # check if char is not in list
            encryptMessage.append(letter)
        else:
            if (letters.alphabet.index(letter) + shift) > 25:
                encryptMessage.append(
                    letters.alphabet[letters.alphabet.index(letter) + shift - 26]
                )
            else:
                encryptMessage.append(
                    letters.alphabet[letters.alphabet.index(letter) + shift]
                )
    # Join all the elements in the list and turn it into a String.
    print(f"The encoded text is {''.join(encryptMessage)}")


# Decryption
def decrypt(text, shift):
    decryptMessage = []
    for letter in text:  # itterate through the message
        if letter not in letters.alphabet:  # check if char is not in list
            decryptMessage.append(letter)
        else:
            if (letters.alphabet.index(letter) + shift) < 0:
                decryptMessage.append(
                    letters.alphabet[letters.alphabet.index(letter) - shift + 26]
                )
            else:
                decryptMessage.append(
                    letters.alphabet[letters.alphabet.index(letter) - shift]
                )
    # Join all the elements in the list and turn it into a String.
    print(f"The decoded text is {''.join(decryptMessage)}")


def clearScreen():
    os.system("cls")


while cont is True:
    clearScreen()

    print(art.logo)
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    input_text = input("Type your message:\n").lower()
    input_shift = int(input("Type the shift number (1 - 25):\n"))

    if direction == "encode":
        encrypt(text=input_text, shift=input_shift)
    elif direction == "decode":
        decrypt(text=input_text, shift=input_shift)
    elif direction == "decode":
        decrypt(text=input_text, shift=input_shift)
        decrypt(text=input_text, shift=input_shift)

    askCont = input("Do you want to go again? y / n \n")
    if askCont == "y":
        cont = True
    else:
        cont = False
