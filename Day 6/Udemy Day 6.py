#This is for Udemy focusing on Beginners Python functions and Karel the robot
#More loops and calling functions

#Functions are recognized by name and immediate parenthesis
#Methods usually follow a variable with a <.'name of method'()>
#Print() is a funcitons

#We can create our own functions by defining def with a name parenthesis and then a colon
def myFunction():
    print('Hello')
    print('Bye')

#You must call your function for it to be triggered.
myFunction()

#Indentation determines blocks of codes functions and loop items
    
#While loop are loops that will have a condition that needs to be met before it stops. Copmared to for loops, for loops will continue for a set amount of time specified. While loops might not ever end

#For loops are good for iterating and performing task with each iteration
#While loops are better when there is not clear indication of how many iterations are needed to meet the goal


#There were about 4 or 5 Challenges and all dealing with loops found on this page: https://www.udemy.com/course/100-days-of-code/learn/lecture/19115618#overview

#Code below for the final loops
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
    
# def jump():
#     while wall_on_right():
#         move()
#     turn_right()
#     move()
#     turn_right()
#     while front_is_clear():
#         move()
#     turn_left()         
    
# while not at_goal():
#     if front_is_clear():
#         move()
#     else:
#         turn_left()
#         jump()




#The final project is the reborgs world maze where we get reborg to leave the maze

# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()       

# while front_is_clear():
#     move()
    
# while not at_goal():
#     if right_is_clear():
#         turn_right()
#         move()
#     elif front_is_clear():
#         move()
#     else:
#         turn_left()