# Author: Ifedayo Akinsira-Olumide
welcome_message = "Welcome to the tip calculator."
print(welcome_message)
bill_message = "What was the total bill? $"
bill = float(input(bill_message))
tip_message = "What percentage of tip would you like to give? eg 10, 12, 15 "
tip = int(input(tip_message))
people_message = "How many peopke to split the bill? "
people = int(input(people_message))
new_bill = bill + (bill * (tip / 100))
amount = new_bill / people
result = f"Each person should pay: ${round(amount, 2)}"
print(result)
