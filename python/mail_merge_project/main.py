PLACEHOLDER = "[name]"


with open("./Input/Letters/starting_letter.txt") as new_letter:
    letter = new_letter.read()

with open("./Input/Names/invited_names.txt") as new_invited_names:
    invited_names = new_invited_names.readlines()
    for name in invited_names:
        name = name.strip()
        with open(f"./Output/ReadyToSend/letter_for_{name}.doc", mode="w") as letter_for_name:
            fresh_letter = letter.replace(PLACEHOLDER, name)
            letter_for_name.write(fresh_letter)
