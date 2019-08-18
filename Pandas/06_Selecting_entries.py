import numpy as np
from pandas import Series, DataFrame
import pandas as pd
from numpy.random import randn

ser1 =Series(np.arange(4),index=["a","b","c","d"])

ser1 =2*ser1

ser1


#grabing entries by index name
ser1["b"]

#by numerical default index values
ser1[0]
ser1[2]

#here we are grabbing it by index posiition (nummber) here 2 is up to 2 and not including
ser1[0:2]

#we can grab it by there names but here "c" will be included unlike numerical indexing
ser1["a":"c"]

#we can also grab it by their particular names together by passing list of index name
ser1[["a","d"]]


#usikng logic series[cond]
ser1[ser1>3]

#setting values using same method
ser1[ser1>3] = 10
ser1

#For DataFrames
#creating a dataframne
#note reshape is in tuple because if we call .shape method it returns a tupple of dimentions
dframe = DataFrame(np.arange(25).reshape((5,5)),index=["NYC","LA","Sf","DC","Chi"],
                   columns=["A","B","C","D","E"])

dframe

#grabbing B Column
dframe["B"]

#multiple column by passing list similarly in series
dframe[["A","E","D"]]


#using boolean logic like in sereis

dframe[dframe["C"]>8]

#we can futher get grab the column data with givenn condition
dframe[dframe["C"]>8]["C"]


#boolean grabs
dframe >10

#grabing with loc 
#loc is used to grab row by its name 
dframe.loc["LA"]

#iloc is used to grab row by its index number
dframe.iloc[1]
































