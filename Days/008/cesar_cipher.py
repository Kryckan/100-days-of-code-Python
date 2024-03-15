alphabet = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
input_text = input("Type your message:\n").lower()
input_shift = int(input("Type the shift number (1 - 20):\n"))


def encrypt(text, shift):
    encryptMessage = []
    for letter in text:  # itterate through the message
        if letter not in alphabet:  # check if char is not in list
            encryptMessage.append(letter)
        else:
            if (alphabet.index(letter) + shift) > 25:
                encryptMessage.append(alphabet[alphabet.index(letter) + shift - 26])
            else:
                encryptMessage.append(alphabet[alphabet.index(letter) + shift])
    # Join all the elements in the list and turn it into a String.
    print(f"The encoded text is {''.join(encryptMessage)}")


def decrypt(text, shift):
    decryptMessage = []
    for letter in text:  # itterate through the message
        if letter not in alphabet:  # check if char is not in list
            decryptMessage.append(letter)
        else:
            if (alphabet.index(letter) + shift) < 0:
                decryptMessage.append(alphabet[alphabet.index(letter) - shift + 26])
            else:
                decryptMessage.append(alphabet[alphabet.index(letter) - shift])
    # Join all the elements in the list and turn it into a String.
    print(f"The decoded text is {''.join(decryptMessage)}")


if direction == "encode":
    encrypt(input_text, input_shift)
elif direction == "decode":
    decrypt(input_text, input_shift)
