MENU = {
    "espresso": {
        "ingredients": {
            "water": 10,
            "coffee": 20,
        },
        "cost": 2,
    },

    "latte": {
        "ingredients": {
            "water": 15,
            "coffee": 25,
            "milk": 15,
        },
        "cost": 3,
    },
        "cappuccino": {
            "ingredients": {
                "water": 20,
                "coffee": 30,
                "milk": 20,
        },
        "cost": 4,
    },
}

profit = 0

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def is_resource_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True

def process_coins():
    print("Please insert coins. ")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.10
    total += int(input("How many nickels?: ")) * 0.05
    total += int(input("How many penny?: ")) * 0.01
    return total

def is_transaction_successful(money_received, drink_cost):
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is your change: ${change}")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money Refunded")
        return False

is_on = True

while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino) ")
    if choice == "off":
        is_on = False
    elif choice == "report":
       print(f"water: {resources['water']}ml")
       print(f"milk: {resources['milk']}ml")
       print(f"coffee: {resources['coffee']}g")
       print(f"money: {profit}")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            is_transaction_successful(payment, drink["cost"])
