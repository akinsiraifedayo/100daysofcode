# Author: Ifedayo Akinsira-Olumide
#Password Generator Project to gerarate a password based on the users request

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

#making sure all values are greater than zero
if nr_letters < 0 or nr_numbers < 0 or nr_symbols < 0:
    print("Error: You should only enter numbers greater than zero")
    exit()

#initialising the randomised password in normal order
new_password = ""

#initialising the randomised password in random order
new_password2 = ""

# Generating random letters with the number user requested as reference
for i in range(0, nr_letters):
    new_password += random.choice(letters)

# Generating random numbers with the number user requested as reference
for i in range(0, nr_numbers):
    new_password += random.choice(numbers)

# Generating random symbols with the number user requested as reference
for i in range(0, nr_symbols):
    new_password += random.choice(symbols)


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

# getting the password as a list so we can pick individual values and remove them
password_list = list(new_password)

# shuffling the values of the pasword
for i in range(0, len(new_password)):
  password_value = random.choice(password_list)
  new_password2 += str(password_value)
  password_list.remove(password_value)
# random.shuffle(password_list) # would pretty much do the same thing which i just wrote the above function for above # And convert the ist back to a string

print(f"Your new password without mixing {new_password}")
print(f"Your new password shuffling the values {new_password2}")
