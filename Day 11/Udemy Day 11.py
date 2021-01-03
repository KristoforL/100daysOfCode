#The goal is to make a blackjack game
import random as r
import blackjack_art as ba
import math as m


############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created: 
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
#user_cards = []
#computer_cards = []

#Hint 6: Create a function called calculate_score() that takes a List of cards as input 
#and returns the score. 
#Look up the sum() function to help you do this.

#Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

#Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

#Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

#Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.


print(f'{ba.logo}')
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


#def blackjack():

# def again():
#     again = input('Do you want to play again? Y/N\n').lower()
#     if again == 'y':
#        blackjack()
#     else:
#        return 'Gameover\nThank you for playing' 


play = input('Do you want to play a game of blackjack? Y/N\n').lower()

player = []
computer = []

#Dealing the cards and adding them to the hands
if play == 'y':
    for count in range(2):
        player.append(r.choice(cards))
        computer.append(r.choice(cards))
    
#Counting the card amounts the players have
player_count = player[0] + player[1]
computer_count = computer[0] + computer[1]

#Just checking to make sure everything is working
#print(f'{player}\n{computer}\n[{computer[0]}]') 

gameover = True

#Just checking to make sure everything is working
print(f'Player: {player}\nDealer: [{computer[0]}]') 

while gameover:

    if player_count > 21:
        for card in enumerate(player):
            if card == 11:
                player[card] = 1
        if player_count > 21:
            print(f'Your score is {player_count}. You bust! You lose')
            print(f'Player Hand: {player}\nComputer Hand: [{computer}]')
        #again = input('Do you want to play again? Y/N\n').lower()
        #if again == 'y':
        #    blackjack()
        #else:
        #    return 'Gameover\nThank you for playing'    
        break
    elif player_count == 21:
        if computer_count == 21:
            print(f'Dealer wins\nPlayer Hand: {player}\nDealer Hand: {computer}')
            #again = input('Do you want to play again? Y/N\n').lower()
            #if again == 'y':
            #    blackjack()
            #else:
            #    return 'Gameover\nThank you for playing' 
        else:
            print(f'You win\nPlayer Hand: {player}\nDealer Hand: {computer}')
            #again = input('Do you want to play again? Y/N\n').lower()
            #if again == 'y':
            #    blackjack()
            #else:
            #    return 'Gameover\nThank you for playing' 
            break

    hit = input('Do you want to hit? Y/N\n').lower()
    if hit == 'y': 
        player.append(r.choice(cards))
        choice = player[-1]
        player_count += choice
        print(f'Player Hand: {player}\nComputer Hand: [{computer[0]}]')
        if player_count > 21:
            for card in player:
                if card == 11:
                    player[card] = 1
            if player_count > 21:
                print(f'Your score is {player_count}. You bust! You lose')
                print(f'Player Hand: {player}\nComputer Hand: [{computer}]')
                gameover = False

        elif player_count == 21:
            if computer_count == 21:
                print(f'Dealer wins\nPlayer Hand: {player}\nDealer Hand: {computer}')
                gameover = False
            else:
                print(f'You win\nPlayer Hand: {player}\nDealer Hand: {computer}')
                gameover = False

    elif hit == 'n':
        if computer_count < 17:
            computer.append(r.choice(cards))
            another_one = computer[-1]
            computer_count += another_one
            if computer_count == 21:
                if player_count == 21:
                    print(f'Dealer wins\nPlayer Hand: {player}\nDealer Hand: {computer}')
                    gameover = False
                    #again = input('Do you want to play again? Y/N\n').lower()
                    #if again == 'y':
                    #    blackjack()
                    #else:
                    #    return 'Gameover\nThank you for playing'
                else:
                    print(f'Dealer wins\nPlayer Hand: {player}\nDealer Hand: {computer}')
                    gameover = False
            elif computer_count > 21:
                for card in enumerate(computer):
                    if card == 11:
                        computer[card] = 1
                    if computer_count > 21:
                        print(f'Player wins\nPlayer Hand: {player}\nDealer Hand: {computer}')
                        gameover = False
        
        elif computer_count == 21:
            print(f'Dealer wins\nPlayer Hand: {player}\nDealer Hand: {computer}')
            gameover = False
            #again = input('Do you want to play again? Y/N\n').lower()
            #if again == 'y':
            #    blackjack()
            #else:
            #    return 'Gameover\nThank you for playing' 
        elif computer_count < 21:
            if player_count > computer_count:
                print(f'Player wins\nPlayer Hand: {player}\nDealer Hand: {computer}')
                gameover = False
                #again = input('Do you want to play again? Y/N\n').lower()
                #if again == 'y':
                #    blackjack()
                #else:
                #    return 'Gameover\nThank you for playing' 
            elif player_count == computer_count:
                print(f'It is a draw\nPlayer: {player_count}\nDealer: {computer_count}')
                gameover = False
                #again = input('Do you want to play again? Y/N\n').lower()
                #if again == 'y':
                #    blackjack()
                #else:
                #    return 'Gameover\nThank you for playing'
            elif player_count < computer_count:
                print(f'Dealer wins\nPlayer Hand: {player}\nDealer Hand: {computer}')
                gameover = False
                #again = input('Do you want to play again? Y/N\n').lower()
                #if again == 'y':
                #    blackjack()
                #else:
                #    return 'Gameover\nThank you for playing' 
    
        gameover = False
        








