#Day 7 of Code

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

fav_languages = {'J':'python', 'K':'c#', 'L':'js', 'M':'ruby'}
fav_lower = []
for key, value in fav_languages.items():
    fav_lower.append(key.lower())
need_poll = ['j','q','m','l']
for name in need_poll:
    if name in fav_lower:
        print(f"Thank you for taking poll {name.title()}")
    else:
        print(f"Plesae take the poll {name.title()}")

#Poeple: Create dictionaries representing people and put them in a list and loop through the list printing everything you know about the person:


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

#Pets: Create a 3 pet dictionary. Put them in a list and then loop through them
waldo = {'First':'Waldo', 'breed':'boxerPitt', 'owner':'j'}
bella = {'First': 'Bella', 'breed': 'Lab shep', 'owner': 'l'}
blue = {'First': 'Blue', 'breed': 'lab shep', 'owner': 'c'}

pets = [waldo, bella, blue]

for pet in pets:
    print(f"{pet['First']}'s breed is {pet['breed']},and their owner is {pet['owner']}")


#Fav places: Create a dictionary for peoiple as keys and places as values(so a list)

fav_places ={'j':['jinya','fogo'], 'k':['moon','saturn']}
for key, value in fav_places.items():
    print(f"{key} likes to visit:")
    for value in values:
        print(f"{value}")

#Fav_number: modify fav number so each person has more that one fav_number and loop through it

fav_number