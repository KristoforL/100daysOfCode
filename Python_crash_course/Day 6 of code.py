#Day 6 of Code

### Blocks printed with hyphens between are seperate lessons and will have comments for what is covered in the space ###

###--Coditional statements continued with if else, and if elif else statements --###

#Hello admin: Make a list of 5 users including admin. Loop through list greeting everyone and a different for the admin

users = ["admin", "kris", "JKL", "Ninty"]
for user in users:
    if user.lower() == "admin":
        print("Hello Admin, would you like to see a status report")
    else:
        print(f"Hello {user}")

#No users in list? Add and if test to previous block and test your code to see if list is empty

users = []

if users == []:
    print("The list is empty")
else:
    if user.lower() == "admin":
        print("Hello Admin, would you like to see a status report")
    else:
        print(f"Hello {user}")


#Checking usernames: Create a list of users. Make a list of new users with one user being the samae in both, then compare and check if there are double users
users = ["Fred", "Kris", "Bob", "Dan", "Frank"]
new_users = ["frank", "kaleb", "Corey", "Trish", "Potts"]
users_lower = []

for user in users:
    users_lower.append(user.lower())

for user in new_users:
    if user.lower() in users_lower:
        print(f"{user} not available")


#Ordinal numbers: store numbers 1-9 in list and print each one on new line with st rd nd and th for the respective number

ordinal = list(range(1,10))

for number in ordinal:
    if number == 1:
        print(f"{number}st")
    elif number == 2:
        print(f"{number}nd")
    elif number == 3:
        print(f"{number}rd")
    else:
        print(f"{number}th")

#-----------------------------------------------------------------------------#

###--Dictionaries, looping through them, key value pairs--###

#Person: create a dictionary for a person and include first/last name, age, and city they are from, then print each piece of info out DICTIONARIES USE CURLY BRACES{}

person ={'first':'J', 'last':'L', 'age':26, 'city':'Atlanta'}
print(f"Persons name is {person['first']} {person['last']}")
print(f"{person['age']}")
print(f"{person['city']}")

#Favorite number: Create a dictionary for people and their fav number
fav_number = {"J":5, "K":34, "JN":3}
for name in fav_number:
    print(f"{name}'s favorite number is {fav_number[name]}")
