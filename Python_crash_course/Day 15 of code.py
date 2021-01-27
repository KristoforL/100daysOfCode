#Day 15 of Code

### Blocks printed with hyphens between are seperate lessons and will have comments for what is covered in the space ###

###--Classes Continued, changing values in functions, manipulating values with methods, importing from other files current files--###

#Imported Restaurant: Store resstaurant in file and import it and make a restaurant and call method to show it works. 

from restaurant import *

southern = restaurant('Soul Shot', 'southern')
print(southern.served)
southern.describe()
southern.increment_served(15)
print(southern.served)


#Imported admin: Store user admin and privileges in a file and import all them to another file. Make an admin and show privs.

from alluser import *
jkl = admin('j','k','MA')
jkl.privileges.show_privs()

