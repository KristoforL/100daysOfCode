#This is further practive bfore the test on Sunday. I will be reading the chapters again from the pcep website and having some of the practice executed here

###--Practice and review questions before PCEP--###
#Same as from the 21st day of code practice
# I have gotten some of these practice problems from https://www.practicepython.org/exercise/2014/01/29/01-character-input.html

#This week’s exercise is going to be revisiting an old exercise (see Exercise 5), except require the solution in a different way.

#Take two lists, say for example these two:

# 	a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# 	b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# and write a program that returns a list that contains only the elements that are common between the lists (without duplicates). Make sure your program works on two lists of different sizes. Write this in one line of Python using at least one list comprehension. (Hint: Remember list comprehensions from Exercise 7).

# The original formulation of this exercise said to write the solution using one line of Python, but a few readers pointed out that this was impossible to do without using sets that I had not yet discussed on the blog, so you can either choose to use the original directive and read about the set command in Python 3.3, or try to implement this on your own and use at least one list comprehension in the solution.

# Extra:

# Randomly generate two lists to test this


a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

common = []

#This will take the list and print the common items in each list with not duplicates
for item in a:
    if item in b and item not in common:
        common.append(item)
print(f"The common items in the list are:\n{[number for number in common]}\n")


#This program will take in two list and return the common items in both with no duplicates. Based off the simple function above.
def alike(list1, list2):
    """This will check and return the list items that are the same"""
    common = []
    
    for item in list1:
        if item in list2 and item not in common:
            common.append(item)

    print(f"The common items in the taken list are:\n{[number for number in common]}\n")

#Must call this function for it to be printed out.
alike(a,b)


#Imported the random class so that I can generate random numbers for the list and the length of the list
import random

def makingList():
    """This will check and return the list items that are the same"""
    
    #This section will generate a random number for the list length and append random numbers between 1 and 11 including 1 to the list
    a = random.randint(1,21)
    listA = []
    while a >= 1:
        listA.append(random.randint(1,11))
        a -= 1
    
    b = random.randint(1,11)
    listB = []
    while  b >= 1:
        listB.append(random.randint(1,11))
        b -= 1

    #This is a list to add common items to call back later
    #I could just print them out as the are recognized but in case this needs to be printed out else where we will just return the list.
    common = []

    for item in listA:
        if item in listB and item not in common:
            common.append(item)

    #Can be written in both ways and it will return the same out put. One is just to read with less characters
    print(f"The first list is:\n{listA}\nThe second list is:\n{listB}\nThe common items in the taken list are:\n{[number for number in common]}\n")
    #print(f"The first list is:\n{listA}\nThe second list is:\n{listB}\nThe common items in the taken list are:\n{common}")


makingList()