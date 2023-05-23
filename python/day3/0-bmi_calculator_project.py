#Author: Ifedayo Akinsira-Olumide
# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
BMI = round(weight / height ** 2)
if BMI < 18.5:
  print(f"Users BMI is {BMI} and User is underweight")
elif BMI < 25:
  print(f"Users BMI is {BMI} and User has a normal weight")
elif BMI < 30:
  print(f"Users BMI is {BMI} and User is overweight")
elif BMI < 35:
  print(f"Users BMI is {BMI} and User is Obese")
else:
  print(f"Users BMI is {BMI} and User is clinically obese")


