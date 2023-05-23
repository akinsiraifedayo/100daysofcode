# Author: Ifedayo Akinsira-Olumide
# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
amount = 0
if str.lower(size) == "s":
  amount += 15
  if str.lower(add_pepperoni) == "y":
    amount += 2
elif str.lower(size) == "m":
  amount += 20
  if str.lower(add_pepperoni) == "y":
    amount += 3
elif str.lower(size) == "l":
  amount += 25
  if str.lower(add_pepperoni) == "y":
    amount += 3
else:
  print("You entered an invalid input")
  exit()

if str.lower(extra_cheese) == "y":
  amount += 1

print(f"Your final bill is ${amount}.")





