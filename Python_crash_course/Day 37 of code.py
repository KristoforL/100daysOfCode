#Data visualization in the no scratch python book

#Imports pyplot because it will have functions for generating plots and charts and gives it an alias
import matplotlib.pyplot as plt

#Using a list of squares for plotting on table/chart
squares = [1,4,9,16,25]
roots = [1,2,3,4,5]

plt.style.use('dark_background')


#Fig represents and entire figure and ax represents a single point
fig, ax = plt.subplots()

#Plot method tries to plot this in the most meaningful way
ax.plot(roots, squares, linewidth=3)

#Sets chart title and label axis+
ax.set_title("Square Numbers", fontsize = 24)
ax.set_xlabel("Value", fontsize = 14)
ax.set_ylabel("Square of Value", fontsize = 14)


#Set size of tick labels:
ax.tick_params(axis = 'both', labelsize =14)

#The show method brings up the matplotlib viewer and displays the plot
plt.show()


#Can check the available styles by running python and checkign from your terminal or command line:
#import matplotlib.pyplot as plt
#plt.style.available

#All the styles available to me 
# ['Solarize_Light2', '_classic_test_patch', 'bmh', 'classic', 'dark_background', 'fast', 'fivethirtyeight', 'ggplot', 'grayscale', 'seaborn', 'seaborn-bright', 'seaborn-colorblind', 'seaborn-dark', 'seaborn-dark-palette', 'seaborn-darkgrid', 'seaborn-deep', 'seaborn-muted', 'seaborn-notebook', 'seaborn-paper', 'seaborn-pastel', 'seaborn-poster', 'seaborn-talk', 'seaborn-ticks', 'seaborn-white', 'seaborn-whitegrid', 'tableau-colorblind10']



