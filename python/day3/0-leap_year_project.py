#Author: Ifedayo Akinsira-Olumide
# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      result = "a leap"
    else:
      result = "not a leap"
  else:
    result = "a leap"
else:
  result = "not a leap"
print(f"{year} is {result} year")



