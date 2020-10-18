#Day 19 of Code

### Blocks printed with hyphens between are seperate lessons and will have comments for what is covered in the space ###

###--Files and exceptions. creating/editing/opening --###


#Fav number: write a program that prompts for users favorite number. use json.dump() to store this number in a file. Write a seperate program that reads in this value and prints the message.  I know your fav number. It's...

import json

 file = 'numbers.json'

 fav = input('What is your favorite number?\n')

 with open(file, 'w') as f:
     json.dump(fav, f)

 with open(file) as f:
     number = json.load(f)
 print(f'I know what your favorite number is. It is {number}')


#Fav number, remembered: Combine two blocks of code from avove into a file. If the number is already stored report the fav number to the user. If not, prompt for the users fav number and store it in a file. Run 2x to see if it works

#Supposed to create a json file
file = 'numbers.json'

def get_number():
    try:
        with open(file) as f:
            number = json.load(f)
    except FileNotFoundError:
        num = input('What is your favorite number?\n')
        with open(file, 'w') as f:
            json.dump(num, f)
    else:
        print(f'I know your favorite number. It is {number}')

get_number()
