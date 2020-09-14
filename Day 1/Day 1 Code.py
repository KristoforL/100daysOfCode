# Day 1 code will have comments before the block of code
# Blocks printed with hyphens between are seperate lessons and will have comments for what is covered in the space

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