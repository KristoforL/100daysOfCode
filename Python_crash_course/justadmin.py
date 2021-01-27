from justuser import *

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
