#Day 6 of Code

### Blocks printed with hyphens between are seperate lessons and will have comments for what is covered in the space ###

###--Dictionaries, looping through them, key value pairs--###

#Glossary: Make a key value pair for words and definition. Print each word and definition

definition ={'dev':'...', 'programmer':'...', 'binary':'...'}
for word in definition:
    print(f"{word}:\n{definition[word]}")

#Glossary 2: make the previous print statement a for loop
for key, value in definition.items():
    print(f"{key}:\n{value}")

#Rivers: Create a dictionary with rivers and their location: Print them in a sentence as the river is located ...

rivers = {"nile":"egypt", "mississippi":"usa","louvre":"europe"}
for river in rivers:
    print(f"{river} is located {rivers[river]}")

for river, location in rivers.items():
    print(f"{river}")
for river, location in rivers.items(): 
    print(f"{location}")

#Polling: use code from fav_language: create new list of users and create a for loop check if any users in new list are in fav language. If they are thank them for taking poll and if not ask them to take poll




aeinstein= {
    'first': 'albert',
    'last': 'einstein',
    'location': 'priniceton',
    'age': 72
}

mcurie={
    'first': 'marie',
    'last': 'curie',
    'location': 'paris',
    'age': 93
}

dcurry ={
    'first': 'denzel',
    'last': 'curry',
    'location': 'usa',
    'age': 103
}

jcole = {
    'first': 'jermaine',
    'last': 'cole',
    'location': 'north carolina',
    'age': 9
}

people = [aeinstein, mcurie, dcurry, jcole]

for person in people:
    print(f"{person['first'].title()}'s last name in {person['last']},and they are {person['age']}")
