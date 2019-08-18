import numpy as np
import pandas as pd

from pandas import Series, DataFrame

#making a series
obj = Series([3,6,9,12]) #returns  indexing too
obj

obj.index
obj.values

#we can input indexing in series function by passing its parameter
ww2_cas =Series([8700000,4300000,2020000,400000],index=["USSR","Germany","japan","USA"])
ww2_cas

ww2_cas.values

#it works like dictionery calling values by key
ww2_cas["USA"]


#check which countries had cas greater than 4 mill
ww2_cas[ww2_cas > 4000000]

#we can treat series as ordered dictionary 
"USSR" in ww2_cas


#typecasting series to dictionary or converting
ww2_dict =ww2_cas.to_dict()
ww2_dict

#and vice versa
ww2_series = Series(ww2_dict)
ww2_series


#we can add list of index in in dictionary key and convert them in series
countries =["China","Germany","Japan","USA","India","USSR"]

obj2 = Series(ww2_dict,countries)
obj2

#returns true if null in series
pd.isnull(obj2)

#returns false if not null in series
pd.notnull(obj2)


ww2_series

#adding series to series
obj2


#here USSR becomes Null Because obj doesnt have that index
#after adding USSR in countries index and running obj2 we can now see addition has ussr 
ww2_series + obj2 

#naming the sereis
obj2.name="World War 2 Casualties"
obj2

#naming the index

obj2.index.name="Country"
obj2





















