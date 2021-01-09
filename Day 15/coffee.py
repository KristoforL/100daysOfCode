#Coffee Machine

import coffee_art as ca
import os
import sys as s


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

profit = 0

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def clear():
    """Clears the window based on the operating system"""
    if s.platform == "linux" or s.platform == "linux2":
        #linux
        os.system('clear')
    elif s.platform == "darwin":
        # OS X
        os.system("clear")
    elif s.platform == "win32":
        # Windows...
        os.system("cls")


#TODO: 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
# a. Check the user’s input to decide what to do next.
# b. The prompt should show every time action has completed, e.g. once the drink is dispensed. The prompt should show again to serve the next customer.

#TODO: 2. Turn off the Coffee Machine by entering “off” to the prompt.
# a. For maintainers of the coffee machine, they can use “off” as the secret word to turn off the machine. Your code should end execution when this happens.

#TODO 3. Print report.
# a. When the user enters “report” to the prompt, a report should be generated that shows
# the current resource values. e.g.
# Water: 100ml
# Milk: 50ml
# Coffee: 76g
# Money: $2.5


#TODO 4. Check resources sufficient?
# a. When the user chooses a drink, the program should check if there are enough
# resources to make that drink.
# b. E.g. if Latte requires 200ml water but there is only 100ml left in the machine. It should
# not continue to make the drink but print: “Sorry there is not enough water.”
# c. The same should happen if another resource is depleted, e.g. milk or coffee.
def ingredients(drink):
    """Checks to see if there are enough ingredients to make the drink"""
    for item in drink:
        if drink[item] >= resources[item]:
            print(f'Sorry there is not enough {item}')
            return False
    return True

#TODO 5. Process coins.
# a. If there are sufficient resources to make the drink selected, then the program should
# prompt the user to insert coins.
# b. Remember that quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
# c. Calculate the monetary value of the coins inserted. E.g. 1 quarter, 2 dimes, 1 nickel, 2
# pennies = 0.25 + 0.1 x 2 + 0.05 + 0.01 x 2 = $0.52

def coins():
    """Adds coins to amount deposited for drink"""
    quarters = int(input('How many quarters:\n')) * .25
    dimes = int(input('How many dimes:\n')) * .1
    nickels = int(input('How many nickels:\n')) * .05
    pennies = int(input('How many pennies:\n')) * .01

    total = float("{:.2f}".format(quarters + dimes + nickels + pennies))

    return total

#TODO 6. Check transaction successful?
# a. Check that the user has inserted enough money to purchase the drink they selected.
# E.g Latte cost $2.50, but they only inserted $0.52 then after counting the coins the
# program should say “Sorry that's not enough money. Money refunded.”.
# b. But if the user has inserted enough money, then the cost of the drink gets added to the
# machine as the profit and this will be reflected the next time “report” is triggered. E.g.
# Water: 100ml
# Milk: 50ml
# Coffee: 76g
# Money: $2.5
# c. If the user has inserted too much money, the machine should offer change.
# E.g. “Here is $2.45 dollars in change.” The change should be rounded to 2 decimal
# places.

def transaction_complete(change, price):
    """Checks to see if money is adequate foe purchase and gives change"""
    clear()
    global profit
    if change >= price:
        profit += change
        remainder = round(change - price, 2) 
        if remainder != 0:
            print(f'Here is your change: ${remainder}')
        return True        
    elif change < price:
        print('Not adequate amount. Here is your refund')
        return False


#TODO 7. Make Coffee.
# a. If the transaction is successful and there are enough resources to make the drink the
# user selected, then the ingredients to make the drink should be deducted from the coffee machine resources.
# E.g. report before purchasing latte:
# Water: 300ml
# Milk: 200ml
# Coffee: 100g
# Money: $0
# Report after purchasing latte:
# Water: 100ml
# Milk: 50ml
# Coffee: 76g
# Money: $2.5
# b. Once all resources have been deducted, tell the user “Here is your latte. Enjoy!”. If latte was their choice of drink.

def make_drink(cafe, ingredients):
    """Calculates amount and informs if enough money is given"""
    for item in ingredients:
        resources[item] -= ingredients[item]
    print(f'Here is your {cafe}!')



on = True
while on:
    cafe = input('What would you like? (espresso/latte/cappuccino):\n').lower()
    if cafe == 'off':
        on = False
    elif cafe == 'report':
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[cafe]
        if ingredients(drink['ingredients']):
            payment = coins()
            transaction_complete(payment, drink['cost'])
            make_drink(cafe, drink['ingredients'])





