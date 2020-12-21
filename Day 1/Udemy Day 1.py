print('Hello World')    

#Day 1 Challenge 1 asked me to print the following: 
# Day 1 - Python Print Function
# The function is declared like this:
# print('what to print')
print('Day 1 - Python Print Function')
print('What to print?')
print("print('what to print')")

#Here we will learn about manipulating the strings
#New lines use \n which means new line
#We can add strings together as well with concatination
print('This is all on the same line\nin the code')
print('Hello ' + 'Kris')

#Day 1 challenge 2 asked me to correct the following code:
# print(Day 1 - String Manipulation")- missing quotation
# print("String Concatenation is done with the "+" sign.") - The plus sign is part of the string and not adding the strings together
#   print('e.g. print("Hello " + "world")')- Indenting problems
# print(("New lines can be created with a backslash and n.") - extra parenthesis

print("Day 1 - String Manipulation")
print("String Concatenation is done with the '+' sign.")
print('e.g. print("Hello " + "world")')
print("New lines can be created with a backslash and n.")

#Input function is used so that you can take input from a user. The information is saved and input is now a variable
#You can even print it all in one line so that you can address yourself
input(('What is your name: ')) #Do not put print into the input function as it will print the statement for you
print('Hello '+ input('What is your name: '))
name = input("What is your name:\n")

#Day 1 Challenge 2 asked me to print out the length of a persons name
#Because I am far more advanced I know how to use the len() function
#Below I have brokoen each function with indention to show what is happening
print(
    len(
        input(
            'What is your name: ')))


#Day 1 Challenge 3 asked me to switch variable values with the code they have provided
# 🚨 Don't change the code below 👇
a = input("a: ")
b = input("b: ")
# 🚨 Don't change the code above 👆
####################################
#Write your code below this line 👇

c = a #Pretty simple to add a variable that is not equal to anything
a = b #Set a equal to be and b = c 
b = c

#Write your code above this line 👆
####################################
# 🚨 Don't change the code below 👇
print("a: " + a)
print("b: " + b)

