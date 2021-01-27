#Day 19.1 of Code

### Blocks printed with hyphens between are seperate lessons and will have comments for what is covered in the space ###

###--Files and exceptions. creating/editing/opening --###

#Verify-User Remeber_me.py aassumes either that the user has enetered their username or that the program is running for the first time. We should modify it in case the current user isnt the last person to login. Before Greeting the user ask if this is the correct username. If not call get_new_user to get correct username

import json

def get_stored_username():
    filename = 'username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username

def greet_user():
    username = get_stored_username()
    if username:
        print(f'Welcome back {username}')
    else:
        username = input('What is your name?\n')
        filename = 'username.json'
        with open(filename, 'w') as f:
            json.dump(username, f)
            print(f'We will remember your next time {username}')

def get_new_username():
    username= input('What is your name?\n')
    file = 'username.json'
    with open(file, 'w') as f:
        json.dump(username, f)
    return username

def greet_user():
    username = get_stored_username()
    if username:
        returning = input(f'Is this {username}? Y/N\n')
        if returning.lower() == 'y':
            print(f'Welcome back {username}')
        else:
            get_new_username()
    else:
        get_new_username()


greet_user()
get_stored_username()
get_new_username()