#Day 20.1 of Code

### Blocks printed with hyphens between are seperate lessons and will have comments for what is covered in the space ###

###--Testing code using unit testing--###

#This code will be used for testing code in Day 20 of code

def city_country(city, country):
    formatted = f'{city.title()}, {country.title()}'
    #print(formatted)
    #Use print for in code testing and return for unittesting
    return formatted


#city_country('madrid', 'spain')

def city_country_pop(city, country, population=''):
    if population:
        formatted = f'{city.title()}, {country.title()}: {population}'
    else:
        formatted = f'{city.title()}, {country.title()}'
    #print(formatted)
    return formatted

#city_country_pop('madrid', 'spain', 50000)