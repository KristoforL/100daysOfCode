#Data visualization in the no scratch python book


from random import choice

class Randomwalk():
    """A class to genrate random walks"""

    def __init__(self, num_points=5000):
        """Initiliaze attributes of a walk"""
        self.num_points = num_points

        #All walks start at (0,0)
        self.x_values = [0]
        self.y_values = [0]


    def fill_walk(self):
        """Calculate all the points in the walk