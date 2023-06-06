# Author: Ifedayo Akinsira-Olumide
#Step 1
import random
word_list = ["aardvark", "baboon", "camel"]
display_input = ""
#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
blanks = []
for letter in chosen_word:
  blanks += "_"
print(blanks)
#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
guessed_letter = str.lower(input("Guess a letter: "))
#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

end_of_game = False
while not end_of_game:
  for i in range(word_length):
    if chosen_word[i] == guessed_letter:
      blanks[i] = guessed_letter

  if "_" not in blanks:
    print(blanks + "\nYou Guessed Right")
    end_of_game = True
  else:
    print(blanks)
    guessed_letter = str.lower(input("Guess a letter: "))
# display_input = ""
# for blank in blanks:
#   display_input += (blank + " ")
# print(display_input)
