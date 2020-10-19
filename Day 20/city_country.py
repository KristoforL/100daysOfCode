def city_country(city, country):
    formatted = f'{city.title()}, {country.title()}'
    return formatted


#city_country('madrid', 'spain')

def city_country_pop(city, country, population=''):
    if population:
        formatted = f'{city.title()}, {country.title()}: {population}'
    else:
        formatted = f'{city.title()}, {country.title()}'
    return formatted

#city_country_pop('madrid', 'spain', 50000)
