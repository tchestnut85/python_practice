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

RESOURCES = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

COINS = {
    "quarters": 0.25,
    "dimes": 0.10,
    "nickels": 0.05,
    "pennies": 0.01
}

MEASUREMENTS = ("ml", "g")

COST = "cost"
OFF = "off"
REPORT = "report"
INGREDIENTS = "ingredients"

menu_items = list(MENU.keys())
resource_items = list(RESOURCES.keys())

def format_amount(amount):
    """Accepts a number or float and formats it to a string with $ and to two decimals."""
    return "$" + "%.2f" % amount


def format_menu_amount(name):
    """Return the amount of an item formatted to have two decimal places."""
    return "$" + "%.2f" % MENU[name][COST]


def print_menu():
    print("Coffee Menu:\n")

    for item in menu_items:
        print(f"{item.capitalize()}: {format_menu_amount(item)}")


def print_report(profit):
    print("\nCoffee Machine Status Report:\n")

    for item in resource_items:
        measurement = MEASUREMENTS[0]
        if item == "coffee":
            measurement = MEASUREMENTS[1]
        print(f"{item.capitalize()}: {RESOURCES[item]}{measurement}")

    print(f"Profit: {format_amount(profit)}\n")
    print("------------------\n")


def check_resources(coffee_name):
    """Check if there is enough of each ingredient for the given coffee."""
    has_enough_ingredients = True

    for ingredient in MENU[coffee_name][INGREDIENTS]:
        current_ingredient_supply = MENU[coffee_name][INGREDIENTS][ingredient]

        if RESOURCES[ingredient] < current_ingredient_supply:
            has_enough_ingredients = False

    return has_enough_ingredients


def deduct_resources(coffee_name):
    """Deduct the ingredient amount from the total resources."""
    for ingredient in MENU[coffee_name][INGREDIENTS]:
        RESOURCES[ingredient] -= MENU[coffee_name][INGREDIENTS][ingredient]


def accept_payment():
    """Prompt user for how many coins to insert and return the total amount of money."""
    amount = 0.0

    for coin in COINS:
        coin_value = COINS[coin]
        coin_count = float(input(f"How many {coin}? "))
        coin_amount = coin_count * coin_value
        amount += coin_amount

    return amount

def start_coffee_machine():
    """Start the program and prompt user for coffee selection."""
    is_machine_on = True
    profit = 0.0

    while is_machine_on is True:
        print_menu()

        coffee_choice = input("\nWhich coffee would you like: Espresso, Latte, or Cappuccino? ").lower()

        if coffee_choice == OFF:
            is_machine_on = False
            print("\nShutting down coffee machine.\n")
            return
        elif coffee_choice == "report":
            print_report(profit)
        elif coffee_choice in menu_items:
            has_enough_resources = check_resources(coffee_choice)

            if not has_enough_resources:
                print(f"Sorry, there are not enough ingredients for a {coffee_choice}.\nPlease try selecting another coffee.\n")
                continue

            deduct_resources(coffee_choice)
            
            payment = accept_payment()

            print(f"\nYou entered {format_amount(payment)}.\n")

            coffee_cost = MENU[coffee_choice][COST]
            if coffee_cost > payment:
                print(f"\nSorry, {format_amount(payment)} is not enough for {coffee_choice}. It costs {format_amount(coffee_cost)}.")
                continue

            profit += MENU[coffee_choice][COST]
            
            print(f"Here is your {coffee_choice} ☕️. Enjoy!\n")

            if payment - coffee_cost > 0:
                print(f"Here is your change... {format_amount(payment - coffee_cost)}.\n")
                print("------------------------\n")
        else:
            print("\nSorry, we don't have that type of coffee. Please choose again.\n")


start_coffee_machine()
