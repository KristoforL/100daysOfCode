#Day 8 of Code

### Blocks printed with hyphens between are seperate lessons and will have comments for what is covered in the space ###

###--Users input, manipulating user input--###

#Rental Car: Ask for user input on what kind of rental car they would like: return let me see if we a (input)

car = input("What type of car would you like to rent: ")
print(f"Let me see if we have {car}")

#Restaurant seating: ASk user how many people: if more than 8 say they will have to wait otherwise table is ready

seating = input("How many people are in the party: ")
seating = int(seating)
if seating < 8:
    print("There is a table ready")
else:
    print("There will be a wait")

#Multiples of ten: Ask user for number and see if it is a multiple of ten. If so then print multiple of ten and if not then it will say not mukltiple of ten

number = input ("Enter a number: ")
number = int(number)
if number%10 == 0:
    print("That is a multiple of 10")
else:
    print("That is not a multiple of 10")

#Pizza toppings: write a look that ask a user for pizza toppings until they enter quit. Print we will add that topping to your pizza

topp = ("What topping would you like? Enter quit to end: \n")
topping = ""
while topping.lower() != 'quit':
    topping = input(topp)
    print(f"We will add {topping}\n")
    
#Movie Tickets: Ask for age and print price based on age in logo

age = input("What is your age? Enter 00 to quit:\n")
age = int(age)

while age != 00:
    if age < 3:
        print("Free")
    elif age < 13:
        print("$10")
    else:
        print("$15")
