#This is further practive bfore the test on Sunday. I will be reading the chapters again from the pcep website and having some of the practice executed here

###--Practice and review questions before PCEP--###
#Same as from the 21st day of code practice
# I have gotten some of these practice problems from https://www.practicepython.org/exercise/2014/01/29/01-character-input.html

#Ask the user for a number and determine whether the number is prime or not. (For those who have forgotten, a prime number is a number that has no divisors.). You can (and should!) use your answer to Exercise 4 to help you. Take this opportunity to practice using functions, described below.


digit = input("Provide a number and I will tell you if it is prime:\n")
digit = int(digit)

primes = [2,3,5,7]


#Checks to see if the number is divisible by another number besides itself and one
#1, 2 , or 3 are prime so we do not check them and check to see if they are divisible by other

# if digit == 0 | digit ==1:
#     print(f"{digit} is not a prime number ")
# elif digit in primes:
#     print(f"The number {digit} is prime\n")
# elif digit % 2 == 0:
#     print(f"{digit} is not prime")
# elif digit % 3 == 0:
#     print(f"{digit} is not prime")
# elif digit % 4 == 0:
#     print(f"{digit} is not prime")
# elif digit % 5 == 0:
#     print(f"{digit} is not prime")
# elif digit % 6 == 0:
#     print(f"{digit} is not prime")
# elif digit % 7 == 0:
#     print(f"{digit} is not prime")
# elif digit % 8 == 0:
#     print(f"{digit} is not prime")
# elif digit % 9 == 0:
#     print(f"{digit} is not prime")
# else:
#     print(f"{digit} is prime\n")

# There is a more efficient way to write this and I am going to try this one more way
#This is not working but I will look into this again another time
for number in range(2,digit+1):
    if digit in primes:
        print(f"The number {digit} is prime\n")
        break
    elif digit == 0 | digit == 1:
        print(f"{digit} is not a prime number")
        break
    
    elif digit % number == 0:
        print(f"{digit} is not prime")
        break
    else:
        print(f"{digit} is prime")
        break

#This is the example that I have seen in the solution for the problem:
if number == 1:
    prime = False
elif number == 2:
    prime = True
#All other primes    
else:
    prime = True
    for check_number in range(2, (number / 2)+1):
        if number % check_number == 0:
            prime = False
            break
return prime

#This is slightly different from what I cdid in mine for the range
#They only returned true if it was prime and if there was nothing returned then it was not prime and another function would handle it
