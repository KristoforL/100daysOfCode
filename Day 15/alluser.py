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


class privileges:
    """Shows privileges"""
    
    def __init__(self):
        """inits privs"""
        self.privileges = ['add', 'delete', 'modify']

    def show_privs(self):
        """Shows all privileges"""
        print(f"The privileges admin has are:")
        for priv in self.privileges:
            print(priv)


class admin(user):
    """Admin class inheriting from user class"""

    def __init__(self, first, last, location):
        """Inits the attributes"""
        super().__init__(first, last, location)
        self.privileges = privileges()
