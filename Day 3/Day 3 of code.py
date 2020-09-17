#Day 3 of Code

### Blocks printed with hyphens between are seperate lessons and will have comments for what is covered in the space ###

###--List, for loops,  numbers in list--###

#Pizzas: Make pizza list and print each pizza using for list
pizzas = ["pepperoni", "cheese", "Italian sausage"]
for pizza in pizzas:
    print(f"{pizzas} is a pizza")

#Animals: Make an animal list for 3 animals, print statement for each using for loop, and add a line outside to print random message one time
animals = ["Dog", "Fish", "Cat"]
for animal in animals:
    print(f"{animals} is a domestic animal")
print("Any of these animals would be a great pet")

#Counting to twenty
numbers = list(range(1,21))
print(numbers)

#1million: make a list to 1 million and print it out
one_mil = list(range(1,1000001))
###Commented out because the printing of the numbers can take some time
#for number in one_mil:
#    print(number)

#Summing 1million using list from above print sum of 1million
print(sum(one_mil))

#Odd numbers: use 3rd arguement range to print odd numbers
odds = (range(1,20,2))
for number in odds:
    print(number)

#Threes: Make a list 3-30 with listing numbers for multiples of 3
threes = list(range(3,31,3))
for number in threes:
    print(number)

#Cubes: Make a list 1-10 and cube each number to print
cubes = list(range(1,11))
for cube in cubes:
    print(cube**3)

#Cube Comprehension: Use comprehension to do the same thing as above but efficienly
cubed = [value**3 for value in range(1,11)]
print(cubed)
