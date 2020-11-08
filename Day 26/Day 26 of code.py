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
    draw = 0

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
    

    while True:

        if choose.lower() == "rock":   
            #Throwing Rock
            if choose.lower() == "rock" and throw == "scissors":
                print("Computer threw scissors. You win")
                win += 1   
            elif choose.lower() == "rock" and throw == "paper":
                print("Computer threw paper. You lose")
                lose += 1
            elif choose.lower() == "rock" and throw == "rock":
                print("Computer threw rock. It's a draw")
                draw += 1

        elif choose.lower() == "paper":
            #Throwing Paper
            if choose.lower() == "paper" and throw == "rock":
                print("Computer threw rock. You win")
                win += 1      
            elif choose.lower() == "paper" and throw == "scissors":
                print("Computer threw scissors. You lose")
                lose += 1
            elif choose.lower() == "paper" and throw == "paper":
                print("Computer threw paper. It's a draw")
                draw += 1

        elif choose.lower() == "scissors":
            #Throwing Scissors
            if choose.lower() == "scissors" and throw == "paper":
                print("Computer threw paper. You win")
                win += 1      
            elif choose.lower() == "scissors" and throw == "rock":
                print("Computer threw rock. You lose")
                lose += 1
            elif choose.lower() == "scissors" and throw == "scissors":
                print("Computer threw scissors. It's a draw")
                draw += 1

        elif choose.lower() == "q":
                print("Game over")
                print(f"P1\nW: {win}\nL: {loss}\nDraw: {draw}")
                break
        else:
            print("Please use rock paper or scissors only")   

#Multiplayer Rock paper scissors
def rps2player():
    """Playing a game of rock paper scissors with a friend"""
    #Keeping count of who won
    p1w = 0
    p2w = 0
    draws = 0

    #Loops through the game so there can be a
    while True:
        p1 = input("Player 1\nR = Rock, P = Paper, S = Scissors, Q = quit\n")
        #This is what I mean in import os
        os.system('cls')
        p2 = input("Player 2\nR = Rock, P = Paper, S = Scissors, Q = quit\n")
        
        #Checks to see who won each round and adds to the score
        if p1.lower() == "r":   
            #Throwing Rock
            if p1.lower() == "r" and p2.lower() == "s":
                print("Player 1 wins")  
                p1w += 1
            elif p1.lower() == "r" and p2.lower() == "p":
                print("Player 2 wins")
                p2w += 1
            elif p1.lower() == "r" and p2.lower() == "r":
                print("It's a draw")
                draws += 1

        elif p1.lower() == "p":
            #Throwing Paper
            if p1.lower() == "p" and p2.lower() == "r":
                print("Player 1  wins")
                p1w += 1
            elif p1.lower() == "p" and p2.lower() == "s":
                print("Player 2 wins")
                p2w += 1
            elif p1.lower() == "p" and p2.lower() == "p":
                print("It's a draw")
                draws += 1

        elif p1.lower() == "s":
            #Throwing Scissors
            if p1.lower() == "s" and p2.lower() == "p":
                print("Player 1 wins")
                p1w += 1      
            elif p1.lower() == "s" and p2.lower() == "r":
                print("Player 2 winss")
                p2w += 1
            elif p1.lower() == "s" and p2.lower() == "s":
                print("It's a draw")
                draws += 1

        #Checks if anyone quit the game and returns the scores
        if p1.lower() == "q":
                print("Game over")
                print(f"Player 1 wins: {p1w}\nPlayer 2 wins: {p2w}\nDraws: {draws}")
                break
        elif p2.lower() == "q":
                print("Game over")
                print(f"Player 1 wins: {p1w}\nPlayer 2 wins: {p2w}\nDraws: {draws}")
                break     
        else:
            print("Please use rock paper or scissors only")   


#rps()
#rps2player()
