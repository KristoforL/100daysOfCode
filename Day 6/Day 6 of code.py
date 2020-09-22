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

