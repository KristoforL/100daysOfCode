import csv
import matplotlib.pyplot as plt

from datetime import datetime


filename = 'Day 39/data/death_valley_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    for index, column_header in enumerate(header_row):
        print(index, column_header)

    #Get dates and high temperatures from this tile
    dates, highs , lows= [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        try:
            high = int(row[5])
            low = int(row[6])
        except ValueError:
            print(f"Missing data from {current_date}")
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

    #print(highs)


#plot the high temperatures and low temperatures
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red')
ax.plot(dates, lows, c='blue')

#Format plot
title = "Daily high and low tempratures - 2018\nDeath Valley, CA"
plt.title(title, fontsize =20)
plt.xlabel('',fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize = 16)
plt.tick_params(axis = 'both', which='major', labelsize = 16)

plt.show()
