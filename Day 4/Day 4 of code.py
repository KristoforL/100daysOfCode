#Day 4 of Code

### Blocks printed with hyphens between are seperate lessons and will have comments for what is covered in the space ###

###--Continued List, for loops,  numbers in list, and using functions like --###

#Slices: using a previous list add linees to end print first 3 middle three and last three

animals = ["Dog", "Fish", "Cat", "Hedgehog", "Snake"]
print("The first three items are:")
for animal in animals[:3]:
    print(animal)

print("The middle three items are:")
for animal in animals[1:4]:
    print(animal)

print("The last three items are:")
for animal in animals[2:5]:
    print(animal)


#My pizzas/Your pizzas: Use list from earlier for pizza. Copy pizza for friends pizza list, append pizza to both and print out the pizzas you and your friend like
pizzas = ["pepperoni", "cheese", "Italian sausage"]
friends_pizza = pizzas[:]

pizzas.append("Bacon")
friends_pizza.append("Anchoivies")

print("Some of my fav pizzas are")
for pizza in pizzas:
    print(pizza)


print("Some of my friends fav pizzas are")
for pizza in friends_pizza:
    print(pizza)


#More loops: make a for loop to print each list of foods
#Because I am confident in this I will not do the above assignment

#Buffet TUPLES!!! Using parenthesis instead of square brakcets. Tuples are immutable and cannot be altered/changed but can be redefined
buffet = ("Chicken", "Fish", "Pizza", "French Fries", "Burgers")

for food in buffet:
    print(food)

#This will fail. Commented out for the code to work with no errors
##buffet[0] = "Tacos"

#This will not because we are redefining it and not changing its content
buffet = ()
print(buffet)

#Make sure to look into PEP8 standards for coding and best practices. Make sure all code up until now and future follows that protocol

#--------------------------------------------------------------------------------------------------------------------------#

###Conditional testing: comparing string values, if statements, and more###

#Print conditional stateements
person = 'you'
print("is person == 'you'? I predict true")
print(person == 'you')

person = 'me'
print("is person == 'you'? I predict false")
print(person == 'me')

#Additional practice asking to print statements that are true and false. 5 for each
#Will not be doing as it is practice I do not believe I need

#More conditional statements: Test for (in)equality, test using lower method, numerical test, >/</>=/<=/=/!=, and/or, and if is(not) in list
people = "Us"
number = 5
numbers = [5, 7, 8, 21, 2, 0] #No parenthesis needed as these are integers
print(people == "us")
print(people == "Us")
if number > 10:
    print("oh Yeaaa")
if number > 10 and people == "Us":
    print("Yes Yes")
if people.lower()== "us":
    print("Case Ignored")
print(number == 5)
print(number <= 5)
print(number > 5)
print(number != 5)
if number < 3 or number > 4:
    print("Big numbers")
if 8 in numbers:
    print("We found it")

