#This is further practive bfore the test on Sunday. I will be reading the chapters again from the pcep website and having some of the practice executed here

###--Practice and review questions before PCEP--###
#Same as from the 21st day of code practice
# I have gotten some of these practice problems from https://www.practicepython.org/exercise/2014/01/29/01-character-input.html


#Write a program that asks the user how many Fibonnaci numbers to generate and then generates them. Take this opportunity to think about how you can use functions. Make sure to ask the user to enter the number of numbers in the sequence to generate.(Hint: The Fibonnaci seqence is a sequence of numbers where the next number in the sequence is the sum of the previous two numbers in the sequence. The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)

#Set global the liat to append to.
fibList = []

#Sets the function to the create the list
def fib():
    """Generates list of fibonnaci numbers the length of the parameter given"""
    number = int(input("How many Fibonnaci numbers do you want to see:\n"))
    count = 1
    
    #Checks the number to see if it is 0 or 1 because I learned that the when setting up fib sequence the negative numbers is not ignored
    if number == 0:
        fibList = []
    elif number == 1: #The first number in the sequence is 1 so the two numbers before would be negative
        fibList == [1]
    elif number == 2: #Starts list at 1, 1 so the number can be added together and continue the sequence
        fibList == [1,1]
    elif number > 2:
        fibList = [1,1]
        while count < (number-1): #Checks the count at a range less than the number asked because the sequece we have will end at the number is asked for
            fibList.append(fibList[count] + fibList[count-1])
            count += 1
    return fibList #Returns the list to end the program

print(fib())