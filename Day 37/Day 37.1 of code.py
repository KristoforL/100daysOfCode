#Data visualization in the no scratch python book

#Imports pyplot because it will have functions for generating plots and charts and gives it an alias
import matplotlib.pyplot as plt

y = [1,4,9,16,25]
x = [1,2,3,4,5]

plt.style.use('dark_background')
fig, ax = plt.subplots()

#Scatter just as advertised is for scatter plot views
ax.scatter(x,y, s=200)

#Set chart title and label axes
ax.set_title("Square Numbers", fontsize = 24)
ax.set_xlabel("Values", fontsize = 14)
ax.set_ylabel("Square of Value", fontsize = 14)

#Set the size of the tick labels
ax.tick_params(axis = 'both', which = 'major', labelsize=14)

#plt.show()


#Loops through the values up to 1000 and squares each one

x = range(1,1001)
y = [i**2 for i in x]

plt.style.use('dark_background')
fig, ax = plt.subplots()

#Scatter just as advertised is for scatter plot views
ax.scatter(x, y, s=10)

#Set chart title and label axes
ax.set_title("Square Numbers", fontsize = 24)
ax.set_xlabel("Values", fontsize = 14)
ax.set_ylabel("Square of Value", fontsize = 14)

#Set the size of the tick labels
#ax.tick_params(axis = 'both', which = 'major', labelsize=14)

#Set the range for each axis
ax.axis([0, 1100, 0, 1100000])

plt.show()
