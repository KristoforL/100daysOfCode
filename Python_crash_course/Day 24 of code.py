#This is further practive bfore the test on Sunday. I will be reading the chapters again from the pcep website and having some of the practice executed here

###--Practice and review questions before PCEP--###
#Same as from the 21st day of code practice
# I have gotten some of these practice problems from https://www.practicepython.org/exercise/2014/01/29/01-character-input.html

# Take two lists, say for example these two:
#   a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#   b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# and write a program that returns a list that contains only the elements that are common between the lists (without duplicates). Make sure your program works on two lists of different sizes.

# Extras:

# Randomly generate two lists to test this
# Write this in one line of Python (don’t worry if you can’t figure this out at this point - we’ll get to it soon)
# List properties

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

def sameElements(a, b):
    """Takes in two list and return a list of the elements that are the same"""
    #Creates a list that will store all the same values from each list
    c = []
    #Takes one element at a time and compares it to other list to see if it is in the list and then makes sure it is not already in the new c before appending it in the list so that there are no copies in list c
    for element in a:
        if element in b and element not in c:
            c.append(element)
    #Prints all the items that are in both list
    print(f"All elements that are in both list\n{c}")


sameElements(a,b)

###---------------Extra-----------###

import random

def randomListCompare():
    """Generates two randome element list and return a list of the elements that are the same"""

    a = []
    b = []

    length = random.randint(1,101)
    for number in range(length):
        value = random.randint(0,101)
        a.append(value)
        
    length = random.randint(1,101)
    for number in range(length):
        b.append(random.randint(0,101))
    
    #Creates a list that will store all the same values from each list
    c = []
    for element in a:
        if element in b and element not in c:
            c.append(element)

    #Takes one element at a time and compares it to other list to see if it is in the list and then makes sure it is not already in the new c before appending it in the list so that there are no copies in list c
    for element in a:
        if element in b and element not in c:
            c.append(element)
    #Prints all the items that are in both list
    
    print(f"The list generated are a:\n{a}\nb:\n{b}\n")
    c.sort()
    print(f"All elements that are in both list\n{c}")

randomListCompare()

#How do they put all of this into one line of code?

print("Single Line execution")
#Still prints double numbers though
print([number for number in a if number in b])