#This is my attmept at the coffee shop and will revisit or change the code based on the walkthrough

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
# b. The prompt should show every time action has completed, e.g. once the drink is
# dispensed. The prompt should show again to serve the next customer.

#TODO: 2. Turn off the Coffee Machine by entering “off” to the prompt.
# a. For maintainers of the coffee machine, they can use “off” as the secret word to turn off
# the machine. Your code should end execution when this happens.

#TODO 3. Print report.
# a. When the user enters “report” to the prompt, a report should be generated that shows
# the current resource values. e.g.
# Water: 100ml
# Milk: 50ml
# Coffee: 76g
# Money: $2.5


def java(coffee):
    """Makes coffe upon request"""
    if coffee == 'off' or coffee == 'report':
        if coffee == 'off':
            return 'Goodbye'
        elif coffee == 'report':
            for item in resources:
                return f"{item}: {resources[item]}"
    elif coffee != 'off' or coffee != 'report':
        if coffee == 'espresso':
            return f"That will cost ${MENU[coffee]['cost']}"
        elif coffee == 'latte':
            return f"That will cost ${MENU[coffee]['cost']}"
        elif coffee == 'cappuccino':
            return f"That will cost ${MENU[coffee]['cost']}"
        else:
            return f'Sorry {coffee} is not an option'


#TODO 4. Check resources sufficient?
# a. When the user chooses a drink, the program should check if there are enough
# resources to make that drink.
# b. E.g. if Latte requires 200ml water but there is only 100ml left in the machine. It should
# not continue to make the drink but print: “Sorry there is not enough water.”
# c. The same should happen if another resource is depleted, e.g. milk or coffee.


def transaction(cafe):
    """Calculates amount and informs if enough money is given"""
    if cafe == 'latte' or cafe == 'cappuccino':
        water = MENU[cafe]['ingredients']['water']
        milk = MENU[cafe]['ingredients']['milk']
        coffee = MENU[cafe]['ingredients']['coffee']

        if resources['water'] >= water and resources['milk'] >= milk and resources['coffee'] >= coffee:
            resources['water'] -= water
            resources['milk'] -= milk
            resources['coffee'] -= coffee
        else:
            return 'Sorry, there are not enough ingredients to make this drink.'
    elif cafe == 'espresso':
        water = MENU[cafe]['ingredients']['water']
        coffee = MENU[cafe]['ingredients']['coffee']

        if resources['water'] >= water and resources['coffee'] >= coffee:
            resources['water'] -= water
            resources['coffee'] -= coffee
        else:
            return 'Sorry, there are not enough ingredients to make this drink.'


print(resources)

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

# 6. Check transaction successful?
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



def complete(change, price):
    """Checks to see if money is adequate foe purchase and gives change"""
    clear()
    profit = float(0)
    if change == price:
        return 'Approved'
        profit += change
    elif change > price:
        profit += change
        remainder = change - price
        return f' Here is your change: ${remainder}'
    elif change < price:
        return 'Not adequate amount. Here is your refund', profit




# 7. Make Coffee.
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



cafe = input('What would you like? (espresso/latte/cappuccino):\n').lower()
price = float(MENU[cafe]['cost'])
change = coins()

java(cafe)
transaction(cafe)
print(complete(change, price))



