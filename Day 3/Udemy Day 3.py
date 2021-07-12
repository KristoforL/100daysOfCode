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


#Day 3 Challenge 3 wants to check and return if a year is a leap year

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



#Sometimes you will have to ask multiple things and to final results
if height > 1.2:
    age = int(input('How old are you?\n'))
    bill = 0
    if age < 12:
        print('Price is $5')
        bill = 5
    elif age <=18:
        print('Price is $7')
        bill = 7
    else:
        print('Price is $12')
        bill = 12

    extra = input('Do you want a photo taken? y/N\n')
    if extra == 'y':
        bill+=3
        print(f'You pay ${bill}')
    else:
        print(f'You pay ${bill}')

else:
    print('Sorry you have to wait until you are taller to ride')


#Day 3 Challenge 4 wants me to make an auto pizza order program

# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

total = 0

if size == 'S':
    if add_pepperoni =='Y':
        total += 17
    elif add_pepperoni == 'N':
        total += 15
elif size == 'M':
    if add_pepperoni =='Y':
        total += 23
    elif add_pepperoni == 'N':
        total += 20
elif size == 'L':
    if add_pepperoni =='Y':
        total += 28
    elif add_pepperoni == 'N':
        total += 25
if extra_cheese == 'Y':
    total += 1

print(f'Your total is ${total}')


#The above rollercoaster program could be made easier with logical operators
if height > 1.2:
    age = int(input('How old are you?\n'))
    bill = 0
    if age < 12:
        print('Price is $5')
        bill = 5
    elif age <=18:
        print('Price is $7')
        bill = 7
    elif age >= 45 and age <= 55:
        print('Free for you')
    else:
        print('Price is $12')
        bill = 12

    extra = input('Do you want a photo taken? y/N\n')
    if extra == 'y':
        bill+=3
        print(f'You pay ${bill}')
    else:
        print(f'You pay ${bill}')

else:
    print('Sorry you have to wait until you are taller to ride')



#Day 4 Challenge 4 is a compatible calculator where we check names for love

# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

true = 'true'
love = 'love'

true_total = 0
love_total = 0

complete = name1 + name2

for letter in true:
    count = complete.count(letter.lower())
    true_total += count

for letter in love:
    count = complete.count(letter.lower())
    love_total += count

combined = int(str(true_total) + str(love_total))

if combined <10 or combined >90:
    print(f"Your score is {combined}, you go together like coke and mentos.")
elif combined > 40 and combined  < 50:
    print(f"Your score is {combined}, you are alright together.")
else:
    print(f"Your score is {combined}.")

