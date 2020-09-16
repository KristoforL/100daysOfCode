#Day 2 of 100 days of code

### Blocks printed with hyphens between are seperate lessons and will have comments for what is covered in the space ###

###--Continuation of list and modifying them. Sorting them, adding them, deleting from them--###

#Seeing the world: Make a list of 5 places. Print the list, use sorted(), print again, used sorted to reverse the list
locations = ["Spain", "Egypt", "Canada", "Asia"]
print(locations)
print(sorted(locations))
print(locations)
print(sorted(locations, reverse=True))
print(locations)
locations.reverse()
print(locations)
locations.reverse()
print(locations)
locations.sort()
print(locations)

#Dinner Guest: The list from above  exercise use len
print(len(locations))

#Every function from the chapter needs to be used with a custom list:
random = ["Waldo", "Dog", "Jeep", "Earth", "Anime"]
print(random)
random.append("Pie")
print(random)
random.pop()
random.remove("Dog")
print(random)
print(sorted(random))
print(sorted(random, reverse=True))
random.sort()
print(random)
random.reverse()
print(random)
print(len(random))
random.sort()
print(random)
random.insert(0,"Fish")
print(random)
del(random[0])
print(random)
