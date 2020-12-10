from die import Die


#Create a D6
die = Die()

#Make some rolls, and store results i a list
results = []
for roll_num in range(1000):
    result =  die.roll()
    results.append(result)

#Analyze the results
frequncies = []
for value in range(1, die.num_sides+1):
    frequncy = results.count(value)
    frequncies.append(frequncy)

print(frequncies)