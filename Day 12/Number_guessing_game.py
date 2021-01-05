import random as r
import guessing_game_art as gga
import sys as s
import os

number = 0
guess = 0

def guess_game():
    """Play a guessing game to guess number with easy or hard modes"""

    level = input('Do you want ot play easy or hard? E/H\n').lower()

    if level == 'e':
        guess = 10
    elif level == 'h':
        guess = 5
    
    while guess > 0:
        attempt = int(input('Guess a number:\n'))
        
        if attempt == number:
            print(f'{attempt} is correct! You win')
            guess = 0
        elif attempt > number:
            guess -= 1
            print(f'{attempt} is too big. You have {guess} tries left')
        else:
            guess -= 1
            print(f'{attempt} is too small You have  {guess} tries left')

        if guess == 0 and attempt != number:
            print(f'Nice try but the number was {number}')

def clear():
    if s.platform == "linux" or s.platform == "linux2":
        #linux
        os.system('clear')
    elif s.platform == "darwin":
        # OS X
        os.system("clear")
    elif s.platform == "win32":
        # Windows...
        os.system("cls")

while input('Do you want to play a number guessing game? Y/N\n').lower() == 'y':
    clear()
    print(gga.logo)
    number = r.randint(1, 100)
    guess_game()

clear()
print(f'Thank you. See you again')
