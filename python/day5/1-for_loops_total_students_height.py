# Author: Ifedayo AKinsira-Olumide
# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆
  # Initializing total
  if n == 0:
    total = 0
  total += student_heights[n]
  n += 1

#Write your code below this row 👇
print(round(total / n))




