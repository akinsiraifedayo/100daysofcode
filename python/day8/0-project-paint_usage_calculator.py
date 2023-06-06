# Author: Ifedayo Akinsira-Olumide
# Paint needed Calculator
# Define a function called paint_calc() so that the code below works.
import math
def paint_calc(height, width, cover):
    number_of_cans =  (height * width) / cover
    # round to the next number
    number_of_cans = math.ceil(number_of_cans)
    print(f"You need {number_of_cans} cans of paint to paint a wall of {height} by {width}")
# 🚨 Don't change the code below 👇
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)



