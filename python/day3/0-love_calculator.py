#Author: Ifedayo AKinsira-Olumide
print("Welcome to the Love Calcuator")
name1 = str.lower(input("What is your name? \n"))
name2 = str.lower(input("What is your partner's name \n"))

a = 0
b = 0
i = 0

# __________USING FOR LOOP ________________
# both_names = name1 + name2
# for i in both_:names
#   if (i == "t") or (i == "r") or (i == "u") or (i == "e"):
#     a += 1
#   if  (i == "l") or (i == "o") or (i == "v") or (i == "e"):
#     b += 1
# for i in name2:
#   if (i == "t") or (i == "r") or (i == "u") or (i == "e"):
#     a += 1
#   if  (i == "l") or (i == "o") or (i == "v") or (i == "e"):
#     b += 1
# print(f"Your True Love score is {a}{b}")

#____________USING THE BASIC METHOD_________________

both_names = name1 + name2
t = both_names.count("t")
r = both_names.count("r")
u = both_names.count("u")
e = both_names.count("e")
tens = t + r + u + e

l = both_names.count("l")
o = both_names.count("o")
v = both_names.count("v")
e = both_names.count("e")
units = l + o + v + e

score = str(tens) + str(units)
score = int(score)

message = ""
if score < 10 or score > 90:
  message = ", you go together like coke and mentos"
elif score >= 40 or score <= 50:
  message = ", you are alright together"
print(f"Your Love score is {score}% {message}")
