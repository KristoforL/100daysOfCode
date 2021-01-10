#Focusing on OOP and making sure we understand Object Oriented Programming concepts

#The Coffee machine from Day 15 used procedural programming where the code is ran from top to bottom and jumping into functions as needed


#Classes and Objects
#Classes are the stencil for the object
# Objects have attributes(Variable associated with object) and methods(Function that an object would do)

#Classes are just blueprints for objects

import turtle
import prettytable as pt

# Jimmy = turtle.Turtle()
# print(Jimmy)

# #Class methods
# Jimmy.shape('turtle')
# Jimmy.color('green')
# Jimmy.forward(100)

# my_screen = turtle.Screen()
# my_screen.exitonclick()

table = pt.PrettyTable()
table.field_names = ['Pokemon Name', 'Type']
table.add_rows(
    [
        ['Pikachu','Electric'],
        ['Squirtle','Water'],
        ['Charmander','Fire'],
        ['Baulbasaur','Grass'],
    ])

print(table)

#Class attribute/field
table.align = 'l'
print(table)









