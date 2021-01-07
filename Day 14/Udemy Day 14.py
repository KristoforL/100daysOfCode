#Creating a game called higher or lower

import game_data as ga
import random as r
import higher_or_lower_art as hla
import sys as s
import os





def clear():
    """Clears the window based on the operating system"""
    if s.platform == "linux" or s.platform == "linux2":
        #linux
        os.system('clear')
    elif s.platform == "darwin":
        # OS X
        os.system("clear")
    elif s.platform == "win32":
        # Windows...
        os.system("cls")

def data():
    """Gets a random piece of data from game data file"""
    return r.choice(ga.data)

def score_up(a):
    """Increases the score"""
    a +=1
    return a
#Select two distinct random indexes in the code for compare and show name. If the same index gets picked then choose another one before print. Provide choice for them to choose one or the other A or B

score = 0

choice1 = data()
choice2 = data()



if choice1 == choice2:
    choice2 = data()

def vs():
    """Shows who the player has to choose between"""
    print(f'{choice1}\n{hla.vs}\n{choice2}')

#If they pick correct then keep then keep the second and then choose another random choice. 

#Add to their score until they get it wrong and then end the program

#Now to make the game continuous

gameover = False

while not gameover:
    
    vs()

    guess = input('Does A or B have more followers? A/B\n').lower()

    if guess == 'a':
        if choice1['follower_count'] > choice2['follower_count']:
            score = score_up(score)
            chioce2 = data()
            print(f'{score}\nCorrect!!')
            vs()
        elif choice2['follower_count'] > choice1['follower_count']:
            #clear()
            print(f'Sorry that is wrong.\nYour score: {score}')
    elif guess == 'b':
        if choice2['follower_count'] > choice1['follower_count']:
            score = score_up(score)
            choice1 = choice2
            choice2 = data()
            print(f'{score}\nCorrect!!')
            vs()
        elif choice1['follower_count'] > choice2['follower_count']:
            #clear()
            print(f'Sorry that is wrong.\nYour score: {score}')
    else:
        print('Please select from A or B only.')












