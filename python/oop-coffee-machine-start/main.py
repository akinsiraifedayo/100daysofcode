from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()


def full_report():
    coffee_maker.report()
    money_machine.report()


is_running = True


while is_running:
    options = menu.get_items()
    command = input(f"What drink do you want? {options}  :  ").lower()
    if command == "report":
        full_report()
    elif command == "end" or command == "stop":
        full_report()
        print("GoodBye!!")
        is_running = False
    elif command in options:
        drink = menu.find_drink(command)
        is_enough_ingredients = coffee_maker.is_resource_sufficient(drink)
        is_enough_money = money_machine.make_payment(cost=drink.cost)
        if is_enough_ingredients and is_enough_money:
            coffee_maker.make_coffee(menu.find_drink(command))
    else:
        print("You entered an invalid input")
