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

    water_needed = item['ingredients']['water']
    if current_water < water_needed:
        print("Not enough water.")
        return False

    coffee_needed = item['ingredients']['water']
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
        coins_inserted += value * amount

    total_coins_inserted = round_money(coins_inserted)
    print(f"Money inserted: ${total_coins_inserted}")

    money_required = round_money(item['cost'])
    print(f"Money required: ${money_required}")

    is_enough_money = total_coins_inserted >= money_required

    return total_coins_inserted, is_enough_money


def check_money(item):
    print(item)


def round_money(amount):
    """Takes a number and returns a 2 decimal float with trailing zeros."""
    return '{:.2f}'.format(round(amount, 2))


def make_espresso():
    water_needed = MENU['espresso']['ingredients']['water']
    coffee_needed = MENU['espresso']['ingredients']['water']

    current_water = resources['water']
    current_coffee = resources['coffee']

    if current_water < water_needed:
        return

    money_needed = MENU['espresso']['cost']
    if money < money_needed:
        print("Not enough money.")
        return

    resources['water'] -= water_needed
    resources['coffee'] -= coffee_needed


def latte():
    print("Make latte")


def cappuccino():
    print("Make cappuccino")


def report():
    for item in resources:
        print(f"{item.title()}: {resources[item]}ml")
    print(f"Money: ${money}")


money = 500
machine_on = True
enough_resources = False
enough_money = False
money_inserted = 0

while machine_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    drink = {}
    make_drink = False

    if choice == "report":
        report()
    elif choice == "off":
        print("Coffee machine powering off.")
        machine_on = False
    elif choice == "espresso":
        drink = MENU["espresso"]
        make_drink = True
    elif choice == "latte":
        latte()
    elif choice == "cappuccino":
        cappuccino()
    else:
        print("Invalid choice.")

    if make_drink:
        enough_resources = check_resources(drink)
        money_inserted, enough_money = insert_coins(drink)

