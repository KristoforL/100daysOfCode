#Day 14 of Code

### Blocks printed with hyphens between are seperate lessons and will have comments for what is covered in the space ###

###--Classes Continued, changing values in functions, manipulating values with methods--###


#Number served: Add number served attribute to restaurant clsas default at 0. Add method called set number served, and increment number served. Create a restaurant, print default number served, usr set and use increment

class restaurant:
    """Creates restaurant"""

    def __init__(self, name, cuisine):
        """Initializes attributes"""
        self.name = name
        self.cuisine = cuisine
        self.served = 0

    def describe(self):
        """Describes restaurant"""
        print(f"{self.name} serves {self.cuisine} cuisine")

    def open(self):
        """Opens restaurant"""
        print(f"{self.name} is open")

    def set_served(self, served):
        """Sets number served"""
        self.served = served

    def increment_served(self, served):
        """Increments number served"""
        self.served += served

    
southern = restaurant('Soul Shot', 'Southern')
print(southern.served)
southern.set_served(100)
print(southern.served)
southern.increment_served(15)
print(southern.served)

#Login Attempts: Add attribute called login attempts to user class. Write method called increment login that increases the login attempts by 1. Another method called reset login attempts to se it back to 0


class user:
    """Creates a user"""

    def __init__(self, first, last, location):
        self.first = first
        self.last = last
        self.location = location
        self.login_attempts = 0

    def describe(self):
        """Describes user"""
        print(f"{self.first} {self.last} is from {self.location}")

    def greet(self):
        """Greets user"""
        print(f"Welcome {self.first} {self.last}")

    def increment_login(self):
        """Increases login by 1"""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Sets logind back to 0"""
        self.login_attempts = 0

    


me = user('J', 'L', 'ATL')
print(me.login_attempts)
me.increment_login()
me.increment_login()
me.increment_login()
me.increment_login()
print(me.login_attempts)
me.reset_login_attempts()
print(me.login_attempts)


#INHERITANCE: PARENT CHILD CLASSES#
#Ice cream stand: Create a child class of restaurant add attribute called flavors that stores list of flavors. Create a method that displays these flavors

class icecream(restaurant):
    """Ice cream stand child of restaurant"""
    def __init__(self, name, cuisine='Ice Cream'):
        """inits attributes"""
        super().__init__(name, cuisine)
        self.flavors = []

    def show_flavors(self):
        """Shows all flavors"""
        print("Flavors available are:")
        for flavor in self.flavors:
            print(flavor)

IC = icecream('BnJ')
IC.flavors.append('CC')
IC.flavors.append('Rocky Road')
IC.show_flavors()



