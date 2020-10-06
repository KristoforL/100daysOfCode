#Day 15.1 of Code

### Blocks printed with hyphens between are seperate lessons and will have comments for what is covered in the space ###

###--Classes Continued, changing values in functions, manipulating values with methods, importing from other files current files--###

#Imported Restaurant: Store resstaurant in file and import it and make a restaurant and call method to show it works.



#Multiple modeules: Store user class in a file and privileeges and admin in another file. Do the same as above:

from justuser import *
from justadmin import *

j = admin('j','k','MA')
j.privileges.show_privs()

#Dice: Make a class called Die with one attribute