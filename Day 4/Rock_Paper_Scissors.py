import random

print('Welcome to rock paper scissors!!')
player = input('Choose R for Rock, P for Paper, S for Scissors.\n')

computer = random.randint(1,3)

#Rock
if player.lower() == 'r':
    print("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")
    if computer == 1:
        print("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")
        print('Computer threw rock. It is a tie')
    elif computer == 2:
        print("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")   
        print('Copmuter threw paper. Computer wins')
    elif computer == 3:
        print("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
        print('Computer threw scissors. You win')

#Paper
elif player.lower() == 'p':
    print("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")
    if computer == 1:
        print("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")
        print('Computer threw rock. You Win')
    elif computer == 2:
        print("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")   
        print('Copmuter threw paper. It is a tie')
    elif computer == 3:
        print("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
        print('Copmuter threw scissors. You Lose')
#Scissors
elif player.lower() == 's':
    print("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
    if computer == 1:
        print("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")
        print('Computer threw rock. You lose')
    elif computer == 2:
        print("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")   
        print('Copmuter threw paper. You Win')
    elif computer == 3:
        print("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
        print('Compuer threw scissors. It is a tie.')

else:
    print('You chose an invalid selection. You lose')