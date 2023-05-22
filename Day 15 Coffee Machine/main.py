import numbers

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },

    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },

    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def check_resources(item):
    current_water = resources['water']
    current_coffee = resources['coffee']
    current_milk = resources['milk']

    item = MENU[item]

    water_needed = item['ingredients']['water']
    if current_water < water_needed:
        print("Not enough water.")
        return False

    coffee_needed = item['ingredients']['coffee']
    if current_coffee < coffee_needed:
        print("Not enough coffee.")
        return False

    if item != MENU['espresso']:
        milk_needed = item['ingredients']['milk']
        if current_milk < milk_needed:
            print("Not enough milk.")
            return False

    return True


def validate_coin_amount(amount, coin_type):
    try:
        amount = int(amount)
    except:
        print(f'You entered an invalid input, no {coin_type} added')
        return 0
    else:
        return int(amount)


def insert_coins(item):
    """Takes number of coins as input from the user and totals the amount.
    Checks if it's enough and returns the
    change and is_enough_money as a boolean."""
    print("Please insert coins.")

    # Validate a number is entered, otherwise 0
    num_quarters = validate_coin_amount(input("How many quarters?: "), "quarters")
    num_dimes = validate_coin_amount(input("How many dimes?: "), "dimes")
    num_nickles = validate_coin_amount(input("How many nickles?: "), "nickles")
    num_pennies = validate_coin_amount(input("How many pennies?: "), "pennies")

    coins = {'quarters': {'value': 0.25,
                          'amount': num_quarters},
             'dimes': {'value': 0.10,
                       'amount': num_dimes},
             'nickles': {'value': 0.05,
                         'amount': num_nickles},
             'pennies': {'value': 0.01,
                         'amount': num_pennies}
             }

    money_inserted = 0
    change = 0

    for coin in coins:
        value = coins[coin]['value']
        amount = coins[coin]['amount']
        money_inserted += (value * amount)

    item = MENU[item]
    money_required = item['cost']
    is_enough_money = money_inserted >= money_required

    if is_enough_money:
        change = round_money(float(money_inserted) - float(money_required))
    else:
        print("Sorry, that's not enough money. Money refunded.")

    return change, is_enough_money


def round_money(amount):
    """Takes a number and returns a 2 decimal float including trailing zeros."""
    return '{:.2f}'.format(float(round(amount, 2)))


def dispense_drink(drink_to_make):
    drink_to_make = MENU[drink_to_make]

    water_needed = drink_to_make['ingredients']['water']
    coffee_needed = drink_to_make['ingredients']['coffee']

    resources['water'] -= water_needed
    resources['coffee'] -= coffee_needed

    if "milk" in drink_to_make:
        milk_needed = drink_to_make['ingredients']['milk']
        resources['milk'] -= milk_needed


def report():
    for item in resources:
        print(f"{item.title()}: {resources[item]}ml")
    print(f"Money: ${money}")


money = 0
machine_on = True
enough_resources = False
enough_money = False

while machine_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    drink_choice = {}
    make_drink = False

    if choice == "report":
        report()
    elif choice == "off":
        print("Coffee machine powering off.")
        machine_on = False
    elif choice == "espresso":
        drink_choice = "espresso"
        make_drink = True
    elif choice == "latte":
        drink_choice = "latte"
        make_drink = True
    elif choice == "cappuccino":
        drink_choice = "cappuccino"
        make_drink = True
    else:
        print("Invalid choice.")

    if make_drink:
        enough_resources = check_resources(drink_choice)
        money, enough_money = insert_coins(drink_choice)

    if enough_resources and enough_money:
        dispense_drink(drink_choice)
        print(f'Here is ${money} in change.')
        print(f'Here is your {drink_choice} ☕. Enjoy!')
        money = 0
