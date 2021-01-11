#Creating classes to make a true false game using OOP concepts


class User:
    """Creates a blueprint for Users on webpage"""
    #Constructors are part of the blueprint that specifies what should happen when object is being constructed
    #Initializing an objects attributes when created. This is done with the def __init__ function

    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        #This is not initialized so that we do not have to make it everytime and we can set a default value
        self.followers = 0
        self.following = 0

        print('new user has been created...')

    def follow(self, user):
        """Adds followers"""
        user.followers += 1
        self.following += 1


#This will not work because the arguments are missing
# user_1 = User()
# user_1.id = '001'
# user_1.username = 'My Name'
# print(user_1.username)
# print(user_1.id)

#With the init function we no longer have to create teh user and add in the attributes differently
user_1 = User('001','my_name')
user_2 = User('002','their_name')
print(user_1.id)
print(user_1.followers)

user_1.follow(user_2)
user_2.follow(user_1)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_1.following)



class Car:
    """Creating a car, attributes, and methods"""
    def __init__(self, seats):
        self.seats = seats

    def change_seats(self, ):
        """Changes the seat number of seats to 2"""
        self.seats = 2



my_car = Car(5)
print(my_car.seats)

my_car.change_seats()
print(my_car.seats)













