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


def insert_coins(item):
    """Takes number of coins as input from the user and totals the amount"""
    print("Please insert coins.")

    coins = {'quarters': {'value': 0.25,
                          'amount': int(input("How many quarters?: "))},

             'dimes': {'value': 0.10,
                       'amount': int(input("How many dimes?: "))},

             'nickles': {'value': 0.05,
                         'amount': int(input("How many nickles?: "))},

             'pennies': {'value': 0.01,
                         'amount': int(input("How many pennies?: "))}
             }

    coins_inserted = 0

    for coin in coins:
        value = coins[coin]['value']
        amount = coins[coin]['amount']
        coins_inserted += (value * amount)

    total_money = coins_inserted
    item = MENU[item]
    money_required = item['cost']
    is_enough_money = total_money >= money_required

    if is_enough_money:
        total_money = round_money(float(total_money) - float(money_required))
    else:
        print("Sorry, that's not enough money. Money refunded.")

    return total_money, is_enough_money


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
