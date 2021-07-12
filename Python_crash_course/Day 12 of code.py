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

#User Profile user code with arbitrary keyword value to describe myself

def profile(first, last, **user_info):
    """Build profile with extra info"""
    user_info['first_name']= first
    user_info['last_name']= last
    return user_info

user_pro= profile('J','K', Birth='Dec')
print(user_pro)

#Cars: Function that always accepts  model, manufacturer and arbitrary info: return info

def car(manufacturer, model, **info):
    """returns car info"""
    info['manufacturer']= manufacturer
    info['model']= model
    return info

Jeep = car('Jeep','Patriot',color='White')
print(Jeep)