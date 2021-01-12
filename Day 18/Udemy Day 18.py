#Todays lesson will be interacting with the GUI, Tuples, and finishing up with making art
import turtle as t

timmy = t.Turtle()
timmy.color('green')
timmy.shape('turtle')

#Turtle challenge 1: Draw a box
def turtle_box(turtle):
    """Makes turtle draw a box"""
    for i in range(4):
        turtle.forward(100)
        turtle.left(90)


#Importing modules

#Basic Import

#import <module name>
#from <module name> import <item of code in module>
#from <module name> import * (all items in module)
#import <module name> as <alias name>

#Installing modules. Not all modules are a packaged with python basic library. Some need to be installed

#install with pip
#install with IDE if it has that functionality

#Turtle CHallenge 2: Draw a dashed line
#My code to move th turtle moving forward
def ten_paces(turtle, distance):
    """Makes turtle go for jog ten paces"""
    place = 0
    while place < distance:
        turtle.forward(10)
        turtle.pu()
        turtle.forward(10)
        turtle.pd()
        place += 10

#Reviewed code from Udemy
def turtle_paces(turtle):
    for i in range(15):
        turtle.forward(10)
        turtle.pu()
        turtle.forward(10)
        turtle.pd()


#Turtle Challenge 3 is to create a shape using polygons
#This is rather long and over the top. I need to know the math behind it 
from random import *
colors = ['red', 'blue', 'black', 'green', 'coral', 'brown', 'purple', 'yellow']

def turtle_shapes(turtle):
    turtle.speed(7)
    turtle.color(choice(colors))
    for i in range(3):
        turtle.forward(100)
        turtle.left((120))
    turtle.color(choice(colors))
    for i in range(4):
        turtle.forward(100)
        turtle.left(90)
    turtle.color(choice(colors))
    for i in range(5):
        turtle.forward(100)
        turtle.left(72)
    turtle.color(choice(colors))
    for i in range(6):
        turtle.forward(100)
        turtle.left(60)
    turtle.color(choice(colors))
    for i in range(7):
        turtle.forward(100)
        turtle.left(51.5)
    turtle.color(choice(colors))
    for i in range(8):
        turtle.forward(100)
        turtle.left(45)
    turtle.color(choice(colors))
    for i in range(9):
        turtle.forward(100)
        turtle.left(39.95)

def turtle_speed(turtle):
    """Draws first 8 polygons with turtle"""
    sides = 3
    count = 0
    while count < 8:
        turn = 360 / sides 
        turtle.color(choice(colors))
        for i in range(sides):
            turtle.forward(100)
            turtle.left((turn))
        sides += 1
        count +=1

#Udemy challenge 3 solution:
def shapes(sides):
    angle = 360 / sides
    for i in range(sides):
        timmy.forward(100)
        timmy.left(angle)


#Tuples and how to generate random RGD colors
#Tuples are data types with parenthesis separated by commas

t.colormode(255)

def rand_color():
    """Creates random color rgb values to return"""
    r = randint(0,255)
    g = randint(0,255)
    b = randint(0,255)

    rgb = (r,g,b)
    return rgb

#Turtle Challenge 4 is generating random walk
direction = [0,90,180,270]
import random as r

def walk(turtle, steps):
    timmy.pensize(5)
    turtle.speed('fastest')
    for i in range(steps):
        turtle.forward(30)
        turtle.seth(r.choice(direction))
        turtle.pencolor(rand_color())


#Challenge 5 is to make a spirograph
# for i in range(360):
#     timmy.speed('fastest')
#     timmy.circle(120, 360)
#     timmy.left(1)
#     timmy.pencolor(rand_color())

#Udemy spirograph block
def spirograph(turtle, gap):
    turtle.speed('fastest') 
    for i in range(int(360 / gap)):
        turtle.color(rand_color())
        turtle.circle(100)
        turtle.seth(turtle.heading() + gap)



screen = t.Screen()
#ten_paces(timmy, 100)
#turtle_box(timmy)
#turtle_paces(timmy)
#turtle_speed(timmy)
# for sides in range(3,11):
#     shapes(sides)
#     timmy.color(choice(colors))
#walk(timmy, 100)
#spirograph(timmy, 15)
screen.exitonclick()