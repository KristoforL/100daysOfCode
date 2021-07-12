#Day 15.1 of Code

### Blocks printed with hyphens between are seperate lessons and will have comments for what is covered in the space ###

###--Classes Continued, changing values in functions, manipulating values with methods, importing from other files current files--###

#Imported Restaurant: Store resstaurant in file and import it and make a restaurant and call method to show it works.



#Multiple modeules: Store user class in a file and privileeges and admin in another file. Do the same as above:

from justuser import *
from justadmin import *

j = admin('j','k','MA')
j.privileges.show_privs()

#Dice: Make a class called Die with one attribute called sides which is 6 by default. Write a method called roll that prints random number between 1 and number of sides. Make a 6 sside die and roll it 10x. Make a 10 and 20 side die and roll each 10x

from random import randint

class die:
    """Create a die of any size"""
    def __init__(self, sides):
        """Init attributes"""
        self.sides = sides

    def roll(self):
        """Roll die with number of sides"""
        print(randint(1, self.sides))

six = die(6)
ten = die(10)
twenty = die(20)
x = 0
y = 0
z = 0

while x < 10:
    six.roll()
    x+=1

print("\n")
while y < 10:
    ten.roll()
    y+=1

print("\n")
while z < 20:
    twenty.roll()
    z+=1

#Lottery: Make tuple of 10 numbers and 5 letters. Randomly select 4 numbers or letterss from the list and print a message ssaying this is the winning ticket. 

from random import choice

lots = (0,1,2,3,4,5,6,7,8,9,'j','k','l','m')
ticket =[]
x = 0

while x < 4:
    pick = choice(lots)
    ticket.append(pick)
    x+=1

print(f"The winning ticket is\n{ticket}")