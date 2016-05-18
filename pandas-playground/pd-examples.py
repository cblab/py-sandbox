import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('ggplot')
#%matplotlib inline


# create a Series with an arbitrary list
s = pd.Series([7, 'Heisenberg', 3.14, -1789710578, 'Happy Eating!'])
print (s)
print ("")


# specify an index to use when creating the Series
s = pd.Series([7, 'Heisenberg', 3.14, -1789710578, 'Happy Eating!'],
              index=['A', 'Z', 'C', 'Y', 'E'])
print (s)


# The Series constructor can convert a dictonary as well, using the keys of the dictionary as its index.
d = {'Chicago': 1000, 'New York': 1300, 'Portland': 900, 'San Francisco': 1100, 'Austin': 450, 'Boston': None}
cities = pd.Series(d)
print(cities)

# use the index to select specific items from the series
print(cities['Chicago'])
print ("")
print(cities[['Chicago', 'Portland', 'San Francisco']])
print ("")

# use boolean indexing for selection
print (cities[cities < 1000])
print ("")

#cities < 1000 returns a Series of True/False values, which we then pass to our Series cities,
#returning the corresponding True items
less_than_1000 = cities < 1000
print(less_than_1000)
print('\n')
print(cities[less_than_1000])

# Plotting some random time series
ts = pd.Series(np.random.randn(1000), index=pd.date_range('1/1/2000', periods=1000))
ts = ts.cumsum()
#ts.plot()
#plt.savefig('demo1.png', transparent=False)

