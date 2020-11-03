#This is further practive bfore the test on Sunday. I will be reading the chapters again from the pcep website and having some of the practice executed here

###--Practice and review questions before PCEP--###
#Same as from the 21st day of code practice
# I have gotten some of these practice problems from https://www.practicepython.org/exercise/2014/01/29/01-character-input.html

#Take a list, say for example this one:
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# and write a program that prints out all the elements of the list that are less than 5.

# Extras:

# Instead of printing the elements one by one, make a new list that has all the elements less than 5 from this list in it and print out this new list.
# Write this in one line of Python.
# Ask the user for a number and return a list that contains only elements from the original list a that are smaller than that number given by the user.

#List for testing
test = [1,54,67,43,7,24,0,99]

#Create a function that takes in a list
def lessThan5(list):
    """Takes in list and prints out all numbers in list if less than 5"""
    #List to append values to
    newlist =[]
    #Compares the number to 5 and if less than 5 append to newlist[]
    for i in list:
        if i <5:
            newlist.append(i)
    #When the list is done being looped through then the print statement will show all values that are less than 5
    print(f"The items in your list less then five are as follows\n {newlist}")                    

#Must call the function for it to work
lessThan5(test)