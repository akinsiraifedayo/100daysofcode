#Author: Ifedayo Akinsira-Olumide
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
if height < 0:
  print("You entered an invalid height")
  exit()
if height >= 120:
  print("You can ride the rollercoaster Congratulations")
  age = int(input("Enter your age "))
  if age <= 0:
    print("You entered an invalid age")
    exit()
  elif age < 12:
    print("Child tickets are $5")
    amount = 5
  elif age <= 18:
    print("Youth tickets are $7")
    amount = 7
  else:
    print("Adult tickets are 12$")
    amount = 12
  photos = str.lower(input("Do you want photos? please type 'YES' or 'NO' "))

  if photos == "yes":
    amount += 2
  elif photos == "no":
    amount = amount
  else:
    print("You entered invalid input")
    exit()
  print(f"Your final bill is ${amount}")



else:
  print("You cannot ride the roller coaster, please grow taller")
