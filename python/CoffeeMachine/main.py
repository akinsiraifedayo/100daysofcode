MENU = {
    "espresso": {
        "ingredients": {
            "milk": 0,
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
        "image": '🍸',

    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
        "image": '☕',
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
        "image": '🍺'
    }
}

resources = {
    "water": 600,
    "milk": 400,
    "coffee": 200,
    "money": 0
}

is_working = True


def report():
    """returns the resources of shop"""
    return (f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g"
            f"\nMoney: ${round(resources['money'], 2)}")


def can_buy(change):
    if change > 0:
        return True
    else:
        return False


def is_available(item):
    global resources
    if resources[item] < 0:
        print(f"There's not enough {item}")
        return False
    else:
        return True


def reset_resources(resources, needed_water, needed_milk, needed_coffee):
    resources["water"] += needed_water
    resources["milk"] += needed_milk
    resources["coffee"] += needed_coffee
    return resources


def topup_resources(resources):
    resources["water"] = 600
    resources["milk"] = 400
    resources["coffee"] = 200
    return resources


def start():
    global resources, is_working
    while is_working:
        user_request = input("What would you like? (espresso/latte/cappuccino): ").lower()

        if user_request == "report":
            print(report())
            start()
        elif user_request == "end" or user_request == "stop":
            print(f"Closing Reports: "
                  f"{report()}\nGoodBye!!")
            is_working = False
        elif user_request == "espresso" or user_request == "latte" or user_request == "cappuccino":
            # TODO 2: Deduct drink price
            needed_water = MENU[user_request]["ingredients"]["water"]
            needed_milk = MENU[user_request]["ingredients"]["milk"]
            needed_coffee = MENU[user_request]["ingredients"]["coffee"]
            resources["water"] -= needed_water
            resources["milk"] -= needed_milk
            resources["coffee"] -= needed_coffee
            is_enough = is_available("water") and is_available("milk") and is_available("coffee")
            if is_enough:

                print("Please Input Coins")
                # TODO 1 Print Create money quarter, dime,  nickels, penny
                quarter = input("How many quarters? ")
                dimes = input("How many dimes? ")
                nickels = input("How many nickels? ")
                pennies = input("How many pennies? ")
                money_a = [quarter, dimes, nickels, pennies]
                # for money in money_a:
                #     if type(money) != type(1):
                #         print("Invaid Input, Pease Start Again")
                #         start()
                quarter = 0.25 * int(quarter)
                dimes = 0.1 * int(dimes)
                nickels = 0.05 * int(nickels)
                pennies = 0.01 * int(pennies)
                total_cost = quarter + dimes + nickels + pennies
                drink_cost = MENU[user_request]["cost"]
                change = total_cost - drink_cost

                if can_buy(change):
                    print(f"Here is ${round(change, 2)} in change\n"
                          f"Here is your {user_request} {MENU[user_request]['image']} Enjoy!")
                    resources["money"] += drink_cost

                else:
                    print("Sorry that's not enough money. Money refunded")
                    resources = reset_resources(resources, needed_water, needed_milk, needed_coffee)
                    start()
            else:
                resources = reset_resources(resources, needed_water, needed_milk, needed_coffee)
        elif user_request == "topup" or user_request == "top up":
            resources = topup_resources(resources)
            print("Topped up successfully")
        else:
            print("You entered an invalid input try again!")
            start()


start()
