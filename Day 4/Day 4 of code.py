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

#This will fail
buffet[0] = "Tacos"

#This will not because we are redefining it and not changing its content
buffet = ()
print(buffet)

#Make sure to look into PEP8 standards for coding and best practices. Make sure all code up until now and future follows that protocol

###---------------------------------------------------------------------###


###Conditional testing: comparing string values, if statements, and more
