#This is further practive bfore the test on Sunday. I will be reading the chapters again from the pcep website and having some of the practice executed here

###--Practice and review questions before PCEP--###
#Same as from the 21st day of code practice
# I have gotten some of these practice problems from https://www.practicepython.org/exercise/2014/01/29/01-character-input.html


# Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game)

# Remember the rules:

# Rock beats scissors
# Scissors beats paper
# Paper beats rock

import random
#This allows commands to be used to clear the terminal so that that player two can input their choice.
import os

def rps():
    """Playing a game of rock paper scissors"""
    #Keeping count of who won
    win = 0
    loss = 0

    #Computer chooses random number for rock paper scissors
    comp = random.randint(1,101)
    throw = ""
    if comp > 0 and comp <= 33:
        throw = "rock"
    elif comp > 33 and comp <= 66:
        throw = "paper"
    elif comp > 66 and comp <= 100:
        throw = "scissors"

    #Checking to see if the random is randomS
    print(comp)
    print(throw)

    choose = input("Rock, Paper, or Scissors:\n")
    #This is what I mean in import os
    os.system('cls')


    if choose.lower() == "rock":   
        #Throwing Rock
        if choose.lower() == "rock" and throw == "scissors":
            print("Computer threw scissors. You win")      
        elif choose.lower() == "rock" and throw == "paper":
            print("Computer threw paper. You lose")
        elif choose.lower() == "rock" and throw == "rock":
            print("Computer threw rock. It's a draw")

    elif choose.lower() == "paper":
        #Throwing Paper
        if choose.lower() == "paper" and throw == "rock":
            print("Computer threw rock. You win")      
        elif choose.lower() == "paper" and throw == "scissors":
            print("Computer threw scissors. You lose")
        elif choose.lower() == "paper" and throw == "paper":
            print("Computer threw paper. It's a draw")

    elif choose.lower() == "scissors":
        #Throwing Scissors
        if choose.lower() == "scissors" and throw == "paper":
            print("Computer threw paper. You win")      
        elif choose.lower() == "scissors" and throw == "rock":
            print("Computer threw rock. You lose")
        elif choose.lower() == "scissors" and throw == "scissors":
            print("Computer threw scissors. It's a draw")

    elif choose.lower() == "q":
            print("Game over")
            #break
    else:
        print("Please use rock paper or scissors only")   

rps()