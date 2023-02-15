from game_data import MENU,resources

def check_supplies(order_ingredients):
    """Loops thorugh order ingredients and check with the resurces. Returns True or False"""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry not enough {item}")
            return False
        else:
            return True

def make_coffe(drink, order_ingredients):
    """Subtracts the order ingredients from the resources that the machine has. No return"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here comes your {drink}")


def monetary_transaction(drink_value):
    """Invite user to pay for his drink and see if he inserted enough coins. TRUE or FALSE return
    If TRUE adds the payment in the resources['cost']"""
    print(f"The {drink} costs {drink_value}$. Insert coins")
    sum = int(input("How many quarters? ")) * 0.25
    sum += int(input("How many dimes? ")) * 0.1
    sum += int(input("How many nickles? ")) * 0.05
    sum += int(input("How many pennies? ")) * 0.01
    if sum < drink_value:
        print("Sorry, not enough money. Money refunded")
        return False
    else:
        resources['cost'] += drink_value
        print(f"Your rest is: ${round(sum - drink_value, 2)}")
        return True

is_on = True

while is_on:
    drink = input("What would you like?:(espresso/latte/cappuccino): ").lower()
    if drink == "report":
        print(f"Water: {resources['water']}ml\n"
              f"Milk: {resources['milk']}ml\n"
              f"Coffee: {resources['coffee']}gr\n"
              f"Money: ${resources['cost']}")
    elif drink == "off":
        is_on = False
    else:
        if check_supplies(MENU[drink]['ingredients']):
            if monetary_transaction(MENU[drink]['cost']):
                make_coffe(drink, MENU[drink]['ingredients'])
        else:
            is_on = False
