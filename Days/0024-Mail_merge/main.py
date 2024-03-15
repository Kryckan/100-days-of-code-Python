import os

root_directory = os.path.dirname(__file__)
file_path = os.path.join(root_directory)

_names: list[str] = []


def main():
    extract_names()
    create_letters(_names)


def create_letters(names: list[str]):
    with open(file_path + "/Input/Letters/starting_letter.txt") as letter_file:
        letter = letter_file.read()
        for name in names:
            new_letter = letter.replace("[name]", name)
            with open(
                file_path + "/Output/ReadyToSend/letter_for_" + name + ".txt", mode="w"
            ) as new_letter_file:
                new_letter_file.write(new_letter)


def extract_names():
    with open(file_path + "/Input/Names/invited_names.txt") as names_file:
        names = names_file.readlines()
        for name in names:
            _names.append(name.strip())


if __name__ == "__main__":
    main()
