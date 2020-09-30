#Day 12 of Code

### Blocks printed with hyphens between are seperate lessons and will have comments for what is covered in the space ###

###--Users input, manipulating user input, loops with user input, storing user input, modifying list and dictionaries in functions--###

#Sandwichs: function that accepts list for sandwich, prints summary of the sandwich . Call 3x with multiple items

one = ['a']
two = ['a', 'b']
three = ['a', 'b', 'c']

def sandwiches(items):
    """Prints items on sandwich"""
    print("You want the following on a sandwich:")
    for item in items:
        print(item)


sandwiches(one)
sandwiches(two)
sandwiches(three)
