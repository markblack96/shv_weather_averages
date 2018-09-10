#!/anaconda2/bin/python

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import calendar


months = ['01','02','03','04','05','06','07','08','09','10','11','12']
month = lambda date: date[-2:]

df = pd.read_csv("weather_averages.csv", index_col="DATE")

tavgs = []
year = 1940

plt.magma()

# df.loc[str(year) + '-' + months[i]] provides values for yyyy-mm via df.loc[]
# TODO: update line color
while year <= 2016:
    for i in range(len(months)):
        tavgs.append(df.loc[str(year) + '-' + months[i]].TAVG)
    print(tavgs)
    plt.plot(months, tavgs)
    tavgs = []
    year += 1
    
# plt.axis([1,12,0,100])
plt.title('Monthly average temperatures (F) in Shreveport, LA')
plt.xlabel('Months')
plt.xticks(np.arange(12), calendar.month_name[1:13], rotation=90)
# plt.legend(loc='upper left')
from matplotlib import rcParams
rcParams.update({'figure.autolayout': True})
# plt.tight_layout()
plt.show()

#plt.plot(figures)
#plt.show()