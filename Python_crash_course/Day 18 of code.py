#Day 18 of Code

### Blocks printed with hyphens between are separate lessons and will have comments for what is covered in the space ###

###--Files and exceptions. creating/editing/opening --###

#Guestbook: Write a program that loops prompting for name and appending to the textfile on new line



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

#Addition Calculator: Wrap above in while loop. I got ahead of myself and did that already.

#Cats and dogs: Make two ffiles with 3 names in each. Write a progra to try and read file. Wrap in try catch filenotfound errors. Test that error works

def read(file):
    try:
        with open(file) as file:
            content = file.read()
    except FileNotFoundError:
        print('File is not found here. Check location')
    else:
        print(content)


read('cats.txt')
read('dogs.txt')

#Modify above code so that it does not print and error rather passes on it


def read(file):
    try:
        with open(file) as file:
            content = file.read()
    except FileNotFoundError:
        #The pass keyword ignores that there is an error and not interrupt the flow of the program
        pass
    else:
        print(content)

#Common words: Get text from gutenberg.org and find a few text you'd like to analyze. Write a program that reads the files and determines how many times the word 'the' appears in each text. Also try ' the ' with spaces to get a more accurate count or space before and after to get most accurate results


#My code works but does not work as expected. Could use some touching up to work like the block of code below
file = 'apology.txt'

the = 'the'
count = 0
with open(file) as file:
    contents = file.readlines()
    for line in contents:
        for the in line:
            count += 1
    print(count)    


#This works but not with words that are set in variables. Far off
file = 'apology.txt'
def count_word(book, word):
    with open(book, encoding = 'utf-8') as file:
        lines = file.read()
        count = lines.lower().count(word)
        print(count)

count_word(file, ' the ')