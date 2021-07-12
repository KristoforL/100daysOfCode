# #Day 4 of code will be about using random module
# #A module is a python file that contains many functions, classes, and methods to limit the amount of code necessary in programs
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

#Moving into list. They start with a bracket and separated by commas
states_of_amaerica = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]

print(states_of_amaerica[0])
states_of_amaerica[0] == 'delaware'
states_of_amaerica.append('Puerto Rico')


#Day 4 challenge 2 wants me to split everyones name
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
chosen_one = random.choice(names)#Was not allowed to use choice but it works just the same
chosen = names[random.randint(0,len(names))]

print(f'{chosen.title()} will be paying today.')

#Out of index error
states_of_amaerica.pop()
print(len(states_of_amaerica))

#List manipulation
dirty_dozen = ['Strawberries', 'Spinach', 'Kale', 'Nectarines', 'Apples', 'Grapes', 'Peaches', 'Cherries', 'Pears', 'Tomatoes', 'Celery', 'Potatoes']
clean_15 = ['Avocados', 'Sweet corn', 'Pineapples', 'Cabbages', 'Onions', 'Sweet peas (frozen)', 'Papayas', 'Asparagus', 'Mangoes', 'Eggplants', 'Honeydew melons', 'Kiwis', 'Cantaloupes', 'Cauliflower', 'Broccoli']

#This will show the list combined and in double brackets because it is a list inside of a list
combined =  [dirty_dozen, clean_15]
print(combined)
#Because this is a nested list it would be considered 2 dimensional where the first number is which list to reference and the second being which item in that list to reference.

#Day 4 Challenge 4 wants me to 

# 🚨 Don't change the code below 👇
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? Use a two digit number where the first number is vertical and the second number is how far to the right such as 11, 32, or 21 for example\n")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

vert = int(position[0]) - 1
hor = int(position[1]) - 1
map[vert][hor] = 'X'

#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")