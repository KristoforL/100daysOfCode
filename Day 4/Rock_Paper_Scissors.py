import random

print('Welcome to rock paper scissors!!')
player = input('Choose R for Rock, P for Paper, S for Scissors.\n')

computer = random.randint(1,3)

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""
scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

RPS = [rock, paper, scissors]


#Rock
if player.lower() == 'r':
    print(RPS[0])
    if computer == 1:
        print(RPS[0])
        print('Computer threw rock. It is a tie')
    elif computer == 2:
        print(RPS[1])   
        print('Copmuter threw paper. Computer wins')
    elif computer == 3:
        print(RPS[2])
        print('Computer threw scissors. You win')

#Paper
elif player.lower() == 'p':
    print(RPS[1])
    if computer == 1:
        print(RPS[0])
        print('Computer threw rock. You Win')
    elif computer == 2:
        print(RPS[1])   
        print('Copmuter threw paper. It is a tie')
    elif computer == 3:
        print(RPS[2])
        print('Copmuter threw scissors. You Lose')
#Scissors
elif player.lower() == 's':
    print(RPS[2])
    if computer == 1:
        print(RPS[0])
        print('Computer threw rock. You lose')
    elif computer == 2:
        print(RPS[1])   
        print('Copmuter threw paper. You Win')
    elif computer == 3:
        print(RPS[2])
        print('Computer threw scissors. It is a tie.')

else:
    print('You chose an invalid selection. You lose')