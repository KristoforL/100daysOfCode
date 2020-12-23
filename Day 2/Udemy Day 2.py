# Day 2 of the Udemy course dealing with Data Type

#You can print the a specific character of a string within the print statement
print('Hello' [0])
print('Hello' [4])

#Because I am familiar with the data types I will be commenting or making examples

#Numeric Data types
int
float

#Boolean Data types
True
False

#There is a type() method that will return the type
string = 'fishing'
num = len(string)
print(type(num))

#The above is useful if you are not sure what data type a vairable is
#This becomes useful when it comes to casting or converting data types
num = str(num)
print(type(num))
#Now you see after casting this is now a string and can be used with strings

#Taking advantage of the data types you can use numbers in strings and even vice versa if needed

#Day 2 Challenge 1 wants me to add the digits in a two digit number
# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇
total = int(two_digit_number[0]) + int(two_digit_number[1])
print(total)


#There are all types of operators for math in python
# +
# -
# /
# *
# ** #Exponential 


#There is an order of operations we know that is PEMDAS and from Left to Right
print(3*3+3/3-3)
#Changing it so we get three
print(3*3+3/3-7)
#or
print(3*(3+3)/3-3)


#Day 2 Challenge 2 is BMI calculator
# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

BMI = int(weight)/(float(height)**2)
BMI = int(BMI)
print(BMI)


#Floats can be formatted as well as rounded
round(34.7) #Used to round number to nearest whole number
print(round(8/3))
print(round(2.6666666666666, 2))
print(8//3) #Floor division which prints the floating number to the base whole number

#F strings allow you to print variable and data type content in the middle of a string
score = 0
height = 1.9
isWinning = True

print(f'Your score is {score}, you height is {height}. Is that {isWinning}?')


#Day 2 Challenge 3 to calculate how much longer until you are 90

# 🚨 Don't change the code below 👇
age = input("What is your current age?\n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
age = int(age)
years = 90 - age
months = years * 12
weeks = years * 52
days =  years * 365


print(f'You have\n{months} months\n{weeks} weeks\n{days} days\nleft until you are 90')







