#This is further practive bfore the test on Sunday. I will be reading the chapters again from the pcep website and having some of the practice executed here

###--Practice and review questions before PCEP--###
#Same as from the 21st day of code practice
# I have gotten some of these practice problems from https://www.practicepython.org/exercise/2014/01/29/01-character-input.html

# Create a program that asks the user for a number and then prints out a list of all the divisors of that number. (If you don’t know what a divisor is, it is a number that divides evenly into another number. For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)

def divisors():
    """This will ask for input and return list of all divisors of number"""
    
    while True:
        number = input("Give me a number and I will return all divisors:\n")
        try: 
            number = int(number)
        except TypeError:
            print("Please use integers only")        
            continue
        except ValueError:
            print("Please use integers only")
            continue
        else:
            break

    for i in range(1,number+1):
        if number%i == 0:
            print(i)


divisors()