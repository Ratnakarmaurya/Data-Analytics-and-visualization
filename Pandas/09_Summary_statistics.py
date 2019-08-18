import numpy as np
from pandas import Series, DataFrame
import pandas as pd
from numpy.random import randn
import matplotlib.pyplot as plt

arr = np.array([[1,2,np.nan],[np.nan,3,4]])
dframe1 =  DataFrame(arr,columns=["One","Two","Three"],index=["A","B"] )
dframe1

#Let's see the sum() method in action
dframe1.sum()
#Notice how it ignores NaN values

#Notice how it ignores NaN values
dframe1.sum(axis=1)

#Can also grab min and max values of dataframe
dframe1.min()

#As well as there index
dframe1.idxmin()

dframe1.idxmax()

dframe1.max()

dframe1
#Can also do an accumulation sum
dframe1.cumsum()

#A very useful feature is describe, which provides summary statistics
describe=dframe1.describe()

# We can also get information on correlation and covariance

#For more info on correlation and covariance, check out the videos below!
from IPython.display import YouTubeVideo
YouTubeVideo('xGbpuFNR1ME')

#Now lets check correlation and covariance on some stock prices!

#Pandas can get info off the web
import pandas_datareader as pdweb #workaround pandas ver 0.24.2
import datetime
pd.show_versions()

#Get the closing prices
prices = pdweb.DataReader(["CVX","BP","XOM"],"yahoo",start=datetime.datetime(2015,1,1)
,end=datetime.datetime(2018,1,1))["Adj Close"]
prices

#Show preview
prices.head()

#getting volume
volume = pdweb.DataReader(["CVX","BP","XOM"],"yahoo",start=datetime.datetime(2015,1,1)
,end=datetime.datetime(2018,1,1))["Volume"]

volume
volume.head()

#getting returns
rets = prices.pct_change()

#getting correlation
corr = rets.corr

#Lets see the prices over time to get a very rough idea of the correlation between the stock prices
prices.plot()

import seaborn as sns #for mapping corr
#As expected pretty strong correlations with eachother
sns.heatmap(rets.corr())

# We can also check for unique values and their counts 

ser1 = Series([1,2,3,4,53,33,4,2,55,3,1,1,1,12,2,2,23,3,4])

ser1

#Grab the unique values

ser1.unique()

#Now get the count of the unique values

ser1.value_counts()















