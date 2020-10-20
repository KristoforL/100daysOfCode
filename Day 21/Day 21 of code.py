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
def Century_years():
    """Tells you what year you will be 100 in"""
    #Ask for users age
    age = input('What is your age?\n')
    #Converts the string age to an integer
    age = int(age)
    #Subtracts the age from 100 and then adds it to the current year
    century_year=(100-age)+year
    print(f'You will be 100 in year {century_year}')

#Century_years()