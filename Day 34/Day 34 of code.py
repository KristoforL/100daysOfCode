#This is further practive bfore the test on Sunday. I will be reading the chapters again from the pcep website and having some of the practice executed here

###--Practice and review questions before PCEP--###
#Same as from the 21st day of code practice
# I have gotten some of these practice problems from https://www.practicepython.org/exercise/2014/01/29/01-character-input.html

# Write a program (function!) that takes a list and returns a new list that contains all the elements of the first list minus all the duplicates.

# Extras:

# Write two different functions to do this - one using a loop and constructing a list, and another using sets.
# Go back and do Exercise 5 using sets, and write the solution for that in a different function.

original = [1,1,2,4,5,5,7,3,3,3,2,2,4,5,6,7,2,2,4,2,5,3,6,3,3,6,7,75,4,74,245,673,75]
#Empty list so that we can check across the new numbers taken in and ensure that there is only one of each element in there
new = []


def no_duplicates(lista):
    """Takes in list and then appends all none duplicates to the new list"""
    #Checks each element in the list and sees if it is in the new list and if it is alread in the list it is a duplicate and does not append it to the list
    for element in original:
        if element not in new:
            new.append(element)
    
    print(f"The list of integers with no duplicates is below:\n{new}")

no_duplicates(original)


#This could be done with strings as well to and checks cases
#I have modofied it below to test this out

names = ['kris', 'Kris', 'j', 'J', 'john', 'Doe', 'KRIS']
check_names = []

def no_duplicate_names(lista):
    """Takes in list and then appends all none duplicates to the new list"""
    #Checks each element in the list and sees if it is in the new list and if it is alread in the list it is a duplicate and does not append it to the list
    lower = []
    for element in names:
        #Takes in the list of strings and adds them to a list in lowercase to chacek against and another list in title case to be a little cleaner upon returm 
        if element.lower() not in lower:
            lower.append(element.lower())
            check_names.append(element.title())
    
    print(f"The list of strings with no duplicates is below:\n{check_names}")

no_duplicate_names(names)