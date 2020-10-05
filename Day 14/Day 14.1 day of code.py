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
