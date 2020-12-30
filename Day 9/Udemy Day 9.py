#This is to focus dictionaries, list, and nesting them

#Dictionaries are similar to actual dictionaries where there is a kay and value or word and definition


programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected",
    "Functions": "A piece of code that you can easily call over and over again",
    "Loop": "The action of doing something over and over again",
    1: "The first number when counting"
}

#Retrieving the elements in the dictionary will need the square brackets and the key(The name or leading information for an entry)

print(programming_dictionary["Bug"])
print(programming_dictionary[1])

#Adding entries to a dictionary. Dictionaries can be empty and then added to later or you can set an existing dictionary to empty

programming_dictionary[2] = "The second number in sequence when counting"
print(programming_dictionary)

empty_dictionary = {}

#You can edit items in a dictionary
programming_dictionary["Bug"] = "A moth in your computer"
print(programming_dictionary)

#Looping through dictionaries. I fyou use a traditional loop you will just get the key value and you would have to specify to get the value for that key

for thing in programming_dictionary:
    print(f'{thing}: {programming_dictionary[thing]}')


#Day 9 Challenge 1 is to create a grading program

student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

#TODO-2: Write your code below to add the grades to student_grades.👇
for student in student_scores:
    if student_scores[student] <= 70:
        student_grades[student] = "Fail"
    elif student_scores[student] <= 80:
        student_grades[student] = "Acceptable"
    elif student_scores[student] <= 90:
        student_grades[student] = "Exceeds!"
    elif student_scores[student] <= 100:
        student_grades[student] = "Outstanding!!"
    

# 🚨 Don't change the code below 👇
print(student_grades)

#Nesting dictionaries and list

list = [1,2,3,4,5]
nested = {
    "pie": "scumptious",
    "Cake": "It's okay"
}
nesting = {
    "list":list,
    "nested":nested
}

travel_log = {
    "France": {"cities_visited":["Paris","Lille","Dijon"], "Total_visits": 12},
    "Germany": ["Berlin", "Hamburg", "Stuttgart"],"Total_visits": 5
}

list_of_dictionaries = [
    {
        "country": "France", 
        "cities_visited":["Paris","Lille","Dijon"], 
        "Total_visits": 12
    },
    {
        "Country": "Germany",
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],"Total_visits": 5
    }
]


#Day 9 Challenge 2 wants me to put dictionaries in list

travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
#🚨 Do NOT change the code above

#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇
def add_new_country(country, visits, cities):
    #Could've made a new dictionary before adding the dictionary to the list
    travel_log.append({"country": country, "visits": visits, "cities": cities})


#🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)

