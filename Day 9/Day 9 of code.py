#Day 9 of Code

### Blocks printed with hyphens between are seperate lessons and will have comments for what is covered in the space ###

###--Users input, manipulating user input, loops with user input, storing user input--###

#Three exist: stop the previous block of code with a while stop/active/break statement

#!!!! Currently this code still prints the $15 dollar amount for the last block and I will fix this a little later
while True:
    age = input("What is your age? Enter q to quit: ")
    if age.lower() != 'q':
       age = int(age)
       if age < 3:
           print("Free")
       elif age < 13:
           print("$10")
       else:
           print("$15") 
    else:
        break

active = True
while active:
    age = input("What is your age? Enter q to quit: ")
    if age.lower() != 'q':
       age = int(age)
       if age < 3:
           print("Free")
       elif age < 13:
           print("$10")
       else:
           print("$15")
    else:
        active = False

asking = ("What is your age? Enter q to quit: ")
age = ""
while age != -1:
    ask = input(asking)
    if ask == 'q':
        break
    else:
        age = int(ask)
        if age < 3 and age > 0:
            print("Free")
        elif age < 13 and age >= 3:
            print("$10")
        else:
            print("$15")
        #I fixed it by adding another if statement to check for q to quit

#Infinite loop: Create an infinite loop. It is commented out for the sake of testing

x = 5
#while x < 10:
#    print("mine")

#Deli: Make a sandwich order list and make an empty list to store finished sandwiches. Loop through adding the sandwiches to list as they are finished and print a message saying you are making it when you loop through

orders = ['a', 'b', 'c']
finished = []

for order in orders:
    print(f"Making {order}")
    finished.append(order)

print("The following orders are complete")
for order in finished:
    print(order)

#No a: use previous code and print we are out of a if when looping through listnand remove all orders asking for a

orders = ['a', 'a', 'b', 'c']
print(f"We are out of a")
while 'a' in orders:
    orders.remove('a')
for order in orders:
    print(f"{order} is ready")

#Dream Vacay: Ask where dream vacation would be and include block that prints results

vacays = ("Where is your dream vacation. enter q to quit")
ask = ""
vacay = []

while ask.lower != 'q':
    ask = input(vacays)
    vacays.append(ask)
print("You all want to visit:")
for v in vacay:
    print(v)

#Message write a fuction- display message that prints one sentence telling everyone what you are learning. Call function

def greet_user():
    """Greet user"""
    print("I have learned a lot")

greet_user()

#Fav book: fav book functioni that takes in book title and prints out one of my fav books is...

def fav_book(title):
    """prints fav book"""
    print(f"One of my fav books is {title}")

fav_book("Perks of being a wallflower")

