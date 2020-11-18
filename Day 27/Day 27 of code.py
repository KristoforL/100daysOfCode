#This is further practive bfore the test on Sunday. I will be reading the chapters again from the pcep website and having some of the practice executed here

###--Practice and review questions before PCEP--###
#Same as from the 21st day of code practice
# I have gotten some of these practice problems from https://www.practicepython.org/exercise/2014/01/29/01-character-input.html

# Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right. (Hint: remember to use the user input lessons from the very first exercise)

# Extras:

# Keep the game going until the user types “exit”
# Keep track of how many guesses the user has taken, and when the game ends, print this out.

import random

ans = random.randint(1,10)
#checking the random
print(ans)
used = []
tried = 0


while True:
    guess = input("Guess the number between 1 and 10 including both 1 and 10. Q to leave:\n")
    if guess.lower == 'q':
        break
    else:
        guess = int(guess)
    
    if guess in used:
        print(f"You already guessed {guess}. Try again\n")
        used.append(guess)
        tried+=1
    else:
        if guess == ans:
            print(f"Aye you got it! The number is {guess}.\nIt only took you {tried} tries.\nYour guess in order were {used}")

            break
        elif guess > ans:
            print("Sorry that is too high. Try again\n")
            used.append(guess)
            tried += 1
        else:
            print("Sorry that is too low. Try again\n")
            used.append(guess)
            tried += 1
 