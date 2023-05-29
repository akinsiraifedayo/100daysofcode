# Author: Ifedayo Akinsira-Olumide
#Write your code below this row 👇
# This is a program to do the FIZZ BUZZ Interview question
for i in range(1,101):
  if i % 3 == 0 and i % 5 == 0:
    print("FizzBuzz")
  elif i % 3 == 0:
    print("Fizz")
  elif i % 5 == 0:
    print("Buzz")
  else:
    print(i)

