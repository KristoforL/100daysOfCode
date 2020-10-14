#Day 17 of Code

### Blocks printed with hyphens between are seperate lessons and will have comments for what is covered in the space ###

###--Files and exceptions. creating/editing/opening --###

#Learning Python: open blank filie in your tect editor. Write a few lins about what you learned. In Python you can... Save file in same directory. Write program that reads a file and prints what you wrote 3x. Print the contents once by reading in the entire file, once by looping over the file object, once by storing the lines in a list aanad then working with them outsiide with block

#I am sure there is a way to have a variable for the file only once
#For some reason, I have had to variable this file a few tiems
file = 'python.txt'

with open('python.txt') as file:
    contents = file.read()
print(contents)

file = 'python.txt'
with open(file) as file:
    for line in file:
        print(line)

file = 'python.txt'
with open(file) as file:
    lines = file.readlines()
for line in lines:
    print(line.rstrip())


#Learning C: Using the same file above replace Python with C

file = 'python.txt'
with open(file) as file:
    lines = file.readlines()

for line in lines:
    line.rstrip()
    print(line.replace('Python', 'C'))

#Guest: Ask for user input name. Append name to file called guest
guest = input("What is your name: ")

file = 'guest.txt'
