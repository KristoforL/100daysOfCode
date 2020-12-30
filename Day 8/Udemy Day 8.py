#This will cover inputs and functions

#Some functions will not paramters
def greet():
    print('Hello.')
    print('Hope you are well.')
    print('Welcome to the code.')




#Some functions will take in paramters that will be used in the function. Parameters are just the data passed in and arguements are the actual value
def greet_person(name):
    print(f'Hello, {name}')
    print(f'Hope you are well {name}')
    print(f'Welcome to the code, {name}')

who = input('What is your name?\n')

#Can add in multiple parameters
def greet_with(name, location):
    print(f'Hello {name}.')
    print(f'What is it like in {location}?')


#You can get the position wrong and make utter nonsense with this
#Unless you predetermine the input somewhere else and use that in the function
greet_with('J','Miami')
#You can use the keyword to make the position not matter
greet_with(location = 'LA', name = 'Kris')
#greet_person(who)
greet()

#Day 8 Challenge 1 wants me to create an area calculator

import math as m

#Write your code below this line 👇

def paint_calc(height, width, cover):
    number_of_cans =  m.ceil((height * width) / coverage)
    print(f'You will need {number_of_cans} cans of paint.')

#Write your code above this line 👆
# Define a function called paint_calc() so that the code below works.   

# 🚨 Don't change the code below 👇
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)

#Day 8 Challenge 2 wants me to create a prime number checker

#Write your code below this line 👇

def prime_checker(number):
    if number == 0 or number == 1:
        print(f'{number} is not prime')
    elif number == 2:
        print(f'{number} is prime.')
    else:
        for digit in range(2, number):
            if number % digit == 0:
                print(f'{number} is not prime.')
                break
            if number % digit != 0:
                print(f'{number} is prime:')
                break

#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)