#Day 18 of Code

### Blocks printed with hyphens between are seperate lessons and will have comments for what is covered in the space ###

###--Files and exceptions. creating/editing/opening --###

#Guestbook: Write a program that loops prompting for name and appending to the textfilie on new line



while True:
    #Brings in file and ask for user input
    guest = input('What is your name: ')
    file = 'guest.txt'

    print('Enter q to quit')
    if guest.lower() == 'q':
        break
    else:
        #Appends input to the file and starts a new line
        with open(file, 'a') as file:
            file.write(f'{guest}\n')

#Prints the files contents
file = 'guest.txt'
with open(file) as file:
    contents = file.readlines()
for line in contents:
    print(f'{line}')

#Programming poll: Write a while loop that ask why they like programming. Add each to a file that stores responses.

while True:
    answer = 'poll.txt'
    poll = input('Why do you like to program:\nEnter q to quit\n')
    if poll.lower() == 'q':
        break
    else:
        with open(answer, 'a') as file:
            file.write(f'{poll}\n')

answer = 'poll.txt'
with open(answer) as file:
    contents = file.readlines()
for line in contents:
    print(f'{line}')


#Addtion: ASk use for for two numbers to add together. Convert them to ints, then add them, but do a try catch and throw Value error

print('Give me two numbers to add')
print('Enter q to quit')

while True:
    first = input('First #:\n')
    if first.lower() == 'q':
        break
    second = input('Second #:\n')
    if second.lower() =='q':
        break
    try:
        answer = int(first) + int(second)
    #You can use multiple excepts and if this was a division problem then you will see this error when dividing by zero
    # except ZeroDivisionError:
    #     print("Can't divide by zero")   

    except ValueError:
        print('Please use numbers')

    else:
        print(answer)

print(5/0)