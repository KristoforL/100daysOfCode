#Day 14.1 of Code

### Blocks printed with hyphens between are seperate lessons and will have comments for what is covered in the space ###

###--Classes Continued, changing values in functions, manipulating values with methods--###


#Admin: Make admin class that inherits from user class. Add pirvileges attribute as list. Write method show privileges. Create user, call show privileges.

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

class admin(user):
    """Admin class inheriting from user class"""
    def __init__(self, first, last, location):
        """Inits the attributes"""
        super().__init__(first, last, location)
        self.privileges = ['add','delete','modify']

    def show_privs(self):
        """Shows all privileges"""
        print(f"The privileges {self.first} has are:")
        for priv in self.privileges:
            print(priv)


me = admin('J', 'L', 'ATL')
me.show_privs()

#Upgrade battery: create a car class, electric car child class from car, and a battery class to replace battery attribute with the battery class as an instance

class car:
    """Creates a car"""
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def describe(self):
        print(f"Make: {self.make}\nMode: {self.model}\nYear: {self.year}")

class battery:
    """Battery for ecar"""
    def __init__(self, battery_size=75):
        self.battery_size = battery_size
    
    def range(self):
        """get range of battery"""
        if self.battery_size == 100:
            print("Battery will get 360 miles")
        else:
            print("Battery will get about 260 miles")
    
    def up_battery(self):
        if self.battery_size != 100:
            self.battery_size = 100
        else:
            print("Your battery is at max capacity")

class ecar(car):
    """Create electric car"""
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery_size = battery()
    
j = ecar('T','M3',2021)
j.battery_size.range()
j.battery_size.up_battery()
j.battery_size.range()