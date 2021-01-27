#Day 13 of Code

### Blocks printed with hyphens between are seperate lessons and will have comments for what is covered in the space ###

###--Classes--###

#Restaurant: Makae eclass. The __init__() method for class should store 2 attritbutes called describe_rest() that these two pieces of information and a mthod called open_rest() that prints these two pieces of information indicating the restaurant is open: Make an instance called restaurant from your class. Print two attributes individually and then call both method.

class restaurant:
    """Creates restaurant"""
    def __init__(self, name, cuisine):
        """Initializes attributes"""
        self.name = name
        self.cuisine = cuisine

    def describe(self):
        """Describes restaurant"""
        print(f"{self.name} serves {self.cuisine} cuisine")

    def open(self):
        """Opens restaurant"""
        print(f"{self.name} is open")

thompson_bros = restaurant('Thompson Bros', 'BBQ')
thompson_bros.describe()
thompson_bros.open()

#Three restaurants: Create 3 different restaurants and call describe() for each

fishy =  restaurant('All Fish', 'seafood')
smokey = restaurant('Smoke J','Smokey')
southern = restaurant('Soul Shot','Southern')

fishy.describe()
smokey.describe()
southern.describe()

#Create two attribute user class. Firest and last name then create another attribute that would be associated with user information. Create describe user and greet user methods

class user:
    """Creates a user"""
    def __init__(self, first, last, location):
        self.first = first
        self.last = last
        self.location = location

    def describe(self):
        """Describes user"""
        print(f"{self.first} {self.last} is from {self.location}")

    def greet(self):
        """Greets user"""
        print(f"Welcome {self.first} {self.last}")

me = user('J','L','ATL')
me.describe()
me.greet()

