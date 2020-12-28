#Using what we have learned so far to create  hangman game at the end of the lesson.

import random


stages = [
    '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', 
'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', 
'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', 
'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
''', 
'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', 
'''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', 
'''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = ["aardvark", "baboon", "camel"]
lives = 6

hang = stages[lives]

chosen_word = random.choice(word_list)

completed = []
for letter in chosen_word:
    completed.append('_')

print(hang)
print(chosen_word)
print(completed)



end_game = False

while not end_game:
    guess = input('Guess a letter\n').lower()
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if guess == letter:
            #print(guess)
            #completed.append('_')
            completed[position] = letter

    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            print('You Lose')
            end_game = True
    
    print(completed)
    print(stages[lives])

    if '_' not in completed:
        print('The word is ' + ''.join(completed) + '. You Win')
        end_game = True

    


