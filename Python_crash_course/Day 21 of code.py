#Day 21 of Code

### Blocks printed with hyphens between are seperate lessons and will have comments for what is covered in the space ###

###--Practice and review questions before PCEP--###
# I have gotten some of these practice problems from https://www.practicepython.org/exercise/2014/01/29/01-character-input.html

#Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.

#Import this library so that we have access to the datetime functions
import datetime

#Fetches the specific year for todays date
year = datetime.date.today().year

#Created a fucntion that gathers the age from the user and then does some math to findout what year they would turn 100
#Extras
#Add on to the previous program by asking the user for another number and printing out that many copies of the previous message. (Hint: order of operations exists in Python)
#Print out that many copies of the previous message on separate lines. (Hint: the string "\n is the same as pressing the ENTER button)

def Century_years():
    """Tells you what year you will be 100 in"""
    #Ask for users age
    name = input('What is your name?\n')
    age = input('What is your age?\n')
    #Converts the string age to an integer
    age = int(age)
    #Subtracts the age from 100 and then adds it to the current year
    century_year=(100-age)+year
    info = f'{name} will be 100 in year {century_year}'
    print(info)

    #Extras
    #Gathers information about the number of times the message should print
    x=0
    count = input('How many times do you want to see that message?\n')
    #Converts count to integer
    count = int(count)
    #While loop to print the previous statement as many times as indicated
    while x < count:
        print(info)
        x+=1
    
#Century_years()


#Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. Hint: how does an even / odd number react differently when divided by 2?

#Extras:
#If the number is a multiple of 4, print out a different message.
#Ask the user for two numbers: one number to check(call it num) and one number to divide by(check). If check divides evenly into num, tell that to the user. If not, print a different appropriate message.

def even_odd():
    number = input('Put in a number\n')
    number = int(number)
    if number%2==0 and number%4==0:
        print(f'{number} is even and a multiple of 4')
    elif number%2==0:
        print(f'{number} is even')
    else:
        print(f'{number} is odd')


def divide():
    num = input('Give me a number\n')
    num = int(num)
    check = input('Give me another number\n')
    check = int(check)

    try:
        answer = num/check
    except ZeroDivisionError:
        print('Can not divide by zero')
    else:
        print(answer)

even_odd()
divide()
