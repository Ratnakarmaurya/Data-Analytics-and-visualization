import numpy as np
from pandas import Series, DataFrame
import pandas as pd
from numpy.random import randn

#creating series
data = Series(["one","two",np.nan,"four"])
data

#Find the missing values
data.isnull()
#We can simply drop the NAN 
data.dropna()

#data frame
# In a DataFrame we need to be a little more careful!
dframe = DataFrame([[1,2,3],[np.nan,5,6],[7,np.nan,9],[np.nan,np.nan,np.nan]])
dframe
#drops severy nan row
clean_dframe = dframe.dropna()
clean_dframe
#We can also specify to only drop rows that are complete missing all data
dframe.dropna(how="all")
#Or we can specify to drop columns with missing data
dframe.dropna(axis=1)#This should drop all columns out since every column contains at least 1 NAN


npn = np.nan
dframe2 = DataFrame([[1,2,3,npn],[2,npn,5,6],[npn,7,npn,9],[1,npn,npn,npn]])
dframe2

#threshhold drops row with the less nan then parameter
#Droppin any rows tht dont have at least 2 data points

dframe2.dropna(thresh=2)
#For example if we only want rows with at least 3 data points
dframe2.dropna(thresh=3)


dframe2
#We can also fill any NAN
dframe2.fillna(1)

#diffrent values for diffrenet columns using dictonary
dframe2.fillna({0:"a",1:1,2:"4e",3:0})
#Note that we still have access to the original dframe

dframe2
#If we want to modify the exsisting object, use inplace
dframe2.fillna(999,inplace = True)
dframe2
5