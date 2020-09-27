#Day 10 of Code

### Blocks printed with hyphens between are seperate lessons and will have comments for what is covered in the space ###

###--Users input, manipulating user input, loops with user input, storing user input--###

#Tshirt: function- make_tshirts that accepts size and text to put on shirt. Prints out summary of shirt. Use positional and keyword calling

def make_tshirt(size, message):
    """Prints summary of shirt order"""
    print(f"Size: {size}\nText: {message}")

make_tshirt('large', 'lift mafia')
make_tshirt(message='I like to lift', size='L')

#Large Tshirts: modify above code so its a large shirt by default and message is I love python. Make a default shirt, one with default message and one with different size and message

def make_tshirt(size='large', text='I love python'):
    """Makes shirt with default size and message"""
    print(f"Size: {size}\nText: {text}")
make_tshirt()
make_tshirt('M')
make_tshirt('S','Big Gains')

#Cities: function desc_city that accepts city and country it is in as parameters. Prints city is in country

def cities(city, country):
    """Prints city and country it is in"""
    print(f"{city} is in {country}")

cities('Atlanta','usa')
cities('Toronto', 'Canada')
cities('Sydney', 'Australia')

#City Names: FUnction calle city_country: