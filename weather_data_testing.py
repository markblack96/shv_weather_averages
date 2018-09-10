#!/anaconda2/bin/python

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import calendar


months = ["%02d" % i for i in range(1,13)]
full_months = calendar.month_name[1:13]
month = lambda date: date[-2:]

df = pd.read_csv("weather_averages.csv", index_col="DATE")

tavgs = []
year = 1940

# df.loc[str(year) + '-' + months[i]] provides values for yyyy-mm via df.loc[]
# TODO: update line color

while year <= 2016:
    for date in df.index:
        if str(year) in date:
            tavgs.append(df.loc[str(year) + '-' + month(date)].TAVG)
    #for i in range(len(months)):
    #    tavgs.append(df.loc[str(year) + '-' + months[i]].TAVG)
    tavgs = np.array(tavgs)
    plt.plot(months, tavgs)
    tavgs = []
    year += 1
    
# plt.axis([1,12,0,100])
plt.title('Monthly average temperatures (F) in Shreveport, LA')
plt.xlabel('Months')
plt.xticks(np.arange(1, 13), full_months, rotation=45)

# plt.legend(loc='upper left')
plt.grid()
plt.show()

#plt.plot(figures)
#plt.show()
