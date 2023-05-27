# Author: Ifedayo AKinsira-Olumide
# import my_module
# print(my_module.pi)
import random

# Generates random number between 0 and 5
random_integer = random.randint(0, 5)
print(random_integer)

#generates between 0  and 1 not including 1
random_float = random.random()
print(random_float)

#generates random floats between 0 and 5 not including 5
print(random_float * 5)
print(random_integer + random_float)

