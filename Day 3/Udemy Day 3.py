#Todays lesson will be about conditional statements

#There are if else statements


water_level = 50

if water_level > 80:
    print('Drain Water')
else:
    print('Continue')

print('Welcome to the rollercoaster!!')
height = int(input('How tall are you in inches\n'))

if height > 53:
    print('Enjoy the ride')
else:
    print('Sorry you have to wait until you are taller to ride')


#Day 3 Challenge 1 Create code that returns if a number is even or odd

# 🚨 Don't change the code below 👇
number = int(input("Which number do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
if number % 2 == 0:
    print(f'{number} is even')
else:
    print(f'{number} is odd')

#If Else statements can be nested within other if else statements
if height > 53:
    age = int(input('How old are you?\n'))
    if age < 12:
        print('Price is $5')
    elif age <=18:
        print('Price is $7')
    else:
        print('Price is $12')
else:
    print('Sorry you have to wait until you are taller to ride')


#Day 3 Challenge 2 wants me to update my BMI calculator from Day 2

# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

BMI = round(weight/ height**2)

if BMI < 18.5:
    print(f'Your BMI is {BMI}. You are "underweight"')
elif BMI < 25:
    print(f'Your BMI is {BMI}. You are "normal" weight')
elif BMI < 30:
    print(f'Your BMI is {BMI}. You are "slightly overweight"')
elif BMI < 35:
    print(f'Your BMI is {BMI}. You are "obese"')
else:
    print(f'Your BMI is {BMI}. You are "clinically obese"')


#Day 3 Challenege 3 wants to chek and return if a year is a leap year

# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
           print('Leap year')
        else:
            print('Not leap year')        
    else:
        print('Leap year')
else:
    print('Not leap Year')