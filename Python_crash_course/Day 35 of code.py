#This is further practive bfore the test on Sunday. I will be reading the chapters again from the pcep website and having some of the practice executed here

###--Practice and review questions before PCEP--###
#Same as from the 21st day of code practice
# I have gotten some of these practice problems from https://www.practicepython.org/exercise/2014/01/29/01-character-input.html

# Write a program (using functions!) that asks the user for a long string containing multiple words. Print back to the user the same string, except with the words in backwards order. For example, say I type the string:

#   My name is Michele
# Then I would see the string:

#   Michele is name My
# shown back to me.

def reverser():
    """Reverses whatever the user inputs"""
    string = input("Type in something and I will print it in reverse:\n")

    #Splits the string into an array of words where there is a space
    split = string.split()

    #An empty string for reversing the string
    reverse = []

    #Loop that will take elevery element in the split list and appends it to the 0th index so the string is put in reverse state
    for item in split:
        reverse.insert(0, item)
    
    #Joins the list with a space so the list is now a string
    joined = " ".join(reverse)

    print(joined)

reverser()

#This works but would not work if the user has punctuation in it