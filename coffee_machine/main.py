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

COST = "cost"
OFF = "off"
REPORT = "report"

menu_items = list(MENU.keys())
resource_items = list(RESOURCES.keys())

def format_menu_amount(name):
    """Return the amount of an item formatted to have two decimal places."""
    return "$" + '%.2f' % MENU[name][COST]

def print_menu():
    print("Coffee Menu:\n")

    for item in menu_items:
        print(f"{item.capitalize()}: {format_menu_amount(item)}")


def print_report(profit):
    for item in resource_items:
        measurement = "ml"
        if item == "coffee":
            measurement = "g"
        print(f"{item.capitalize()}: {RESOURCES[item]}{measurement}")

    print(f"Profit: ${profit}")

def start_coffee_machine():
    is_machine_on = True

    while is_machine_on is True:
        print_menu()
        choice = input("Which coffee would you like? Espresso, Latte, or Cappuccino? ")

        if choice == "off":
            is_machine_on = False
            return
        elif choice == "report":
            print()


#entering "off" will terminate the app
#print the report of current resources when entering "report"​
# check resources - when user selects a drink, check if all its resources are sufficient
    # else, print "Sorry there is not enough {resource}"

# if there are enough resources, prompt the user for coins and calculate the coins

# check for successful transaction - check if the user entered enough coins
    # if no, print "Sorry that's not enough money. Money refunded." and set the coins amount to 0
    # if yes, add the drinks cost to the report's profit property, and offer change if the user entered too much money - “Here is $2.45 dollars in change.” 
        # deduct the resources for the drink from the resources dict
        # print "Here is your {drink}. Enjoy!"

# print the prompt again for what the user would like

# start_coffee_machine()