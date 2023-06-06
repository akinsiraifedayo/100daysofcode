# Author: Ifedayo Akinsira-Olumide

# # comment here
# def prime_checker(number):
#     if number == 2 or number == 3 or number == 5 or number == 7:
#         print(f"{number} is a prime number")
#     elif number % 2 != 0 and number % 3 != 0 and number % 5 != 0 and number % 7 != 0:
#         print(f"{number} is a prime number")
#     else:
#         print(f"{number} is not a prime number")
# # to here

# mehod 2 (personal challenge)
import math


def prime_checker(number):
    is_prime = True
    sqrt_num = math.ceil(number**0.5)
    for i in range(2, sqrt_num):
        if number % i == 0:
            is_prime = False
            print(i)
    if is_prime == True:
        print(f"{number} is a prime number")
    else:
        print(f"{number} is not a prime number")


#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)

