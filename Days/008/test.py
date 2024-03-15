import string

alphabet = string.ascii_lowercase


def caesar_cipher(text, shift, mode):
    if mode == "decrypt":
        shift = -shift
    return "".join(
        [
            alphabet[(alphabet.index(letter) + shift) % 26]
            if letter in alphabet
            else letter
            for letter in text
        ]
    )


while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    input_text = input("Type your message:\n").lower()
    input_shift = int(input("Type the shift number (1 - 20):\n"))

    if direction == "encode":
        print(
            f"The encoded text is {caesar_cipher(input_text, input_shift, 'encrypt')}"
        )
    elif direction == "decode":
        print(
            f"The decoded text is {caesar_cipher(input_text, input_shift, 'decrypt')}"
        )

    again = input("Do you want to go again? Type 'yes' or 'no':\n")
    if again != "yes":
        break
