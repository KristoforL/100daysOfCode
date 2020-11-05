#This is further practive bfore the test on Sunday. I will be reading the chapters again from the pcep website and having some of the practice executed here

###--Practice and review questions before PCEP--###
#Same as from the 21st day of code practice
# I have gotten some of these practice problems from https://www.practicepython.org/exercise/2014/01/29/01-character-input.html

# Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome is a string that reads the same forwards and backwards.)

def palindrome():
    """Takes in  word from user and returns if it is a palindrome"""
    word = input("Provide a word I will let you know if it is a palidrome:\n")

    #Creates empty list to compare
    newWord = []
    backwards = []
    #Appends letters from word into newWord
    for letter in word:
        newWord.append(letter)

    #Inserts letters at elelment 0 so word is now in reverse
    for letter in newWord:
        backwards.insert(0, letter)

    #Compares the list and if they are the same it is a palindrome. Otherwise it is not and is shown the reverse order
    if newWord == backwards:
        print(f"{word.title()} is a palindrome")
    else:
        print(f"{word.title()} is not a palindrome")
        for item in backwards:
            print(f"{item}",end="")


palindrome()