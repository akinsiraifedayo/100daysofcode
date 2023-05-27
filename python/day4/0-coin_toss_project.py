# Author: Ifedayo Akinsira-Olumide
#Write your code below this line 👇
#Hint: Remember to import the random module first. 🎲
import random
#The seed number helps generate the same value with the same seed number
test_seed = int(input("create a seed number: "))
random.seed(test_seed)

#Generate a random integer either 1 or 2
guess = random.randint(1, 2)
if guess == 1:
  print("Heads")
else:
  print("Tails")



