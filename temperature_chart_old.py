#!/anaconda2/bin/python

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates


# month=lambda date: date[-2:]

# for loop start:
#   plt.plot(months, tavgs_for_each_month, color+i)
#   plt.label(last_line)

df = pd.read_csv("weather_averages.csv")

figures = df[['DATE', 'TAVG']]
#print(figures)
#print(figures.DATE.values, figures['TAVG'].values)

year = [figures.DATE.values[i] for i in range(len(figures.DATE.values)) if '2016' in figures.DATE.values[i]]

months = [1,2,3,4,5,6,7,8,9,10,11,12]
# months = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June', 7: 'July', 8: 'August', 9: 'September', 10: 'October', 11: 'November', 12: 'December'}

print(year)

tavgs = [figures.loc[figures['DATE'] == year[i], 'TAVG'].iloc[0] for i in range(len(year))]
print(tavgs)
plt.plot(months, tavgs, color='#ff0000', label='2016')

# repeat
year = [figures.DATE.values[i] for i in range(len(figures.DATE.values)) if '1940' in figures.DATE.values[i]]

print(year)

tavgs = [figures.loc[figures['DATE'] == year[i], 'TAVG'].iloc[0] for i in range(len(year))]
print(tavgs)
plt.plot(months, tavgs, color='#00ff00', label='1940')

# repeat
year = [figures.DATE.values[i] for i in range(len(figures.DATE.values)) if '1977' in figures.DATE.values[i]]

print(year)

tavgs = [figures.loc[figures['DATE'] == year[i], 'TAVG'].iloc[0] for i in range(len(year))]
print(tavgs)
plt.plot(months, tavgs, color='#0000ff', label='1977')

plt.axis([1,12,30,90])
plt.title('Monthly average temperatures (F) in Shreveport, LA')
plt.xlabel('Months')
plt.legend(loc='upper left')
plt.show()

#plt.plot(figures)
#plt.show()