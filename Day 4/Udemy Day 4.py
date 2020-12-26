#Day 4 of code will be about using random module
#A module is a python file that containes many functions, classes, and methods to limit the amount of code necessary in programs
import random

rand_int = random.randint(100,200)
print(rand_int)

rand_float = random.random()
print(rand_float)

rf= rand_float * 5
print(rf)

#Day 4 Challenge 1 is to make a heads or tails generator

HoT = random.randint(0,1)
if HoT == 1:
    print('Heads')
else:
    print('Tails')

