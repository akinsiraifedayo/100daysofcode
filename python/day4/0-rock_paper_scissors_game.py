# Author: Ifedayo Akinsira-Olumide
import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

computer = random.randint(0, 2)
decisions = [rock, paper, scissors]
user = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if user < 0 or user > 2:
  print("User has entered invalid input")
  exit()

print(decisions[user] + "\nYou choose")
print(decisions[computer] + "\nComputer choose")

if (computer == 0) and user == 2:
  print("You lose")
elif (computer == 2) and user == 0:
  print("You win")
elif (user == computer):
  print("its a draw")
elif (user > computer):
  print("You win")
else:
  print("You Lose")



