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
#ax.scatter(x, y, c='green', s=10)
ax.scatter(x, y, c=y, cmap=plt.cm.plasma, s=10)


#Set chart title and label axes
ax.set_title("Square Numbers", fontsize = 24)
ax.set_xlabel("Values", fontsize = 14)
ax.set_ylabel("Square of Value", fontsize = 14)

#Set the size of the tick labels
#ax.tick_params(axis = 'both', which = 'major', labelsize=14)

#Set the range for each axis
ax.axis([0, 1100, 0, 1100000])



#Saves the graph in the same directory as a png file
#plt.savefig('Day 37/squares_plots.png', bbox_inches='tight')



x = range(1,5001)
y = [i**3 for i in x]

plt.style.use('dark_background')
fig, ax = plt.subplots()


ax.scatter(x, y, c=y, cmap=plt.cm.plasma, s=10)

ax.set_title("Cubed Numbers", fontsize = 24)
ax.set_xlabel("Values", fontsize = 14)
ax.set_ylabel("Cubed of Value", fontsize = 14)

ax.axis([0,7000, 0, 200000000000])




#Shows the graph as soon as it is created
plt.show()


#Colors for Cmap

# cmaps = [('Perceptually Uniform Sequential', [
#             'viridis', 'plasma', 'inferno', 'magma', 'cividis']),
#          ('Sequential', [
#             'Greys', 'Purples', 'Blues', 'Greens', 'Oranges', 'Reds',
#             'YlOrBr', 'YlOrRd', 'OrRd', 'PuRd', 'RdPu', 'BuPu',
#             'GnBu', 'PuBu', 'YlGnBu', 'PuBuGn', 'BuGn', 'YlGn']),
#          ('Sequential (2)', [
#             'binary', 'gist_yarg', 'gist_gray', 'gray', 'bone', 'pink',
#             'spring', 'summer', 'autumn', 'winter', 'cool', 'Wistia',
#             'hot', 'afmhot', 'gist_heat', 'copper']),
#          ('Diverging', [
#             'PiYG', 'PRGn', 'BrBG', 'PuOr', 'RdGy', 'RdBu',
#             'RdYlBu', 'RdYlGn', 'Spectral', 'coolwarm', 'bwr', 'seismic']),
#          ('Cyclic', ['twilight', 'twilight_shifted', 'hsv']),
#          ('Qualitative', [
#             'Pastel1', 'Pastel2', 'Paired', 'Accent',
#             'Dark2', 'Set1', 'Set2', 'Set3',
#             'tab10', 'tab20', 'tab20b', 'tab20c']),
#          ('Miscellaneous', [
#             'flag', 'prism', 'ocean', 'gist_earth', 'terrain', 'gist_stern',
#             'gnuplot', 'gnuplot2', 'CMRmap', 'cubehelix', 'brg',
#             'gist_rainbow', 'rainbow', 'jet', 'turbo', 'nipy_spectral',
#             'gist_ncar'])]