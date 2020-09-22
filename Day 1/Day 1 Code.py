# Day 1 code will have comments before the block of code
### Blocks printed with hyphens between are seperate lessons and will have comments for what is covered in the space ###

###--Variables, manipulating variaable and representing variables in print statements--###

#Simple Message: Basics to create a variable and print it
message = "100 days of code has started"
print(message)

#Simple messages: Printing the previous message, changing it, then printing it to show it has changed
message = ("Now this is when it gets a little bothersome typing all this out")
print(message)

#Peresonal Message: THis will be a message to someone with their name being represented as a variable.
first = "Jacquawn"
last =  "Lockhart"
#In this I made the first and last name a variable so that I do not haveto type the first and last name variable every time
full = f"{first} {last}"
print(f"Hello {full}, how are you?")

#Name Cases: This will show how to use/call some premade methods so that you can adjust the upper or lower case letters
print(f"{full.upper()}, {full.lower()}, {full.title()}")

#Making a message from variables and putting them in strings
famous_per = "Albert Einstein"
famous_quote = "e=mc^2"
print(f"{famous_per}, once saide {famous_quote}")

#Making a string message variable that includes other variables
message = f"{famous_per}, once said the famous calculation {famous_quote}"
print(message)

#Stripping Names: Removing Space from left, right or either side
name = "  JKL  "
print(name)
print(f"\thello{name.lstrip()}hello\n")
print(f"hello{name.rstrip()}hello")
print(f"hello{name.strip()}hello")

#Numbers and operations. Prints Results for each operation to equal 8. For this to work you must enclose them in parenthesis
print(4+4)
print(10-2)
print(2*4)
print(16/2)

#Fav number: Have a variable to represent my favorite number
fav_number = 5
print(f"My favorite number is {fav_number}")

#Adding Comments: Just a general rule of thumb to add comments so that other coders are not asking you what your code does

#-----------------------------------------------------------------------------#

###--list (LIST ARE SQUARE BRACKETS), and modifying list--###

#Names: create a list of n ames and print each persons name by element

friend = ["James", "Eric", "Waldo"]
print(f"{friend[0]}, {friend[1]}, {friend[2]}")

#Greetings: Printing a message to each person in the list
print(f"Hello {friend[0]}")
print(f"Hello {friend[1]}")
print(f"Hello {friend[2]}")

#Custom list: Create a list of transportation. Print statements about a few
transit = ["Jeep", "Fort GT", "Plane"]

print(f"I love my {transit[0]}")
print(f"I want a {transit[1]}")
print(f"I like to travel by {transit[2]}")

#Guest list: create a list of people you would like to invite to dinner
invited = ["Eric", "Lemeul", "Cookie"]
print(f"{invited[0]}, you're invited")
print(f"{invited[1]}, you're invited")
print(f"{invited[2]}, you're invited")

#Changing a guest list: Alter the guest list, changing one name to another
invited[1] = "Kobe"
print(f"{invited[0]}, you're invited")
print(f"{invited[1]}, you're invited")
print(f"{invited[2]}, you're invited")

#More guest list: add 3 guest to list using insert() and append()
invited.insert(0, "Chadwich")
invited.insert(1, "Robin W.")
invited.append("Lemeul")

#Shrinking List: Removing items from list using del and pop
print(f"Sorry {invited.pop()}")
print(f"Sorry {invited.pop()}")
print(f"Sorry {invited.pop()}")
print(f"Sorry {invited.pop()}")
print(f"{invited[0]}, you're still invited")
print(f"{invited[1]}, you're still invited")
del(invited[0])
del(invited[0])
print(invited)
