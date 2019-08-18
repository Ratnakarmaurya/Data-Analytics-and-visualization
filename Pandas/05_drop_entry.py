import numpy as np
from pandas import Series, DataFrame
import pandas as pd
from numpy.random import randn

#droping index in series

#making a series
ser1= Series(np.arange(3),index=["a","b","c"])
ser1

#this drops an index
ser1.drop("b")

#With a DataFrame we can drop values from either axis
dframe1= DataFrame(np.arange(9).reshape((3,3)),index=["SF","LA","NY"],columns=["pop","size","year"])

dframe1

dframe1.drop("LA")

#this doesnt afffect the orignal dataframe
dframe1

#make a new dframe to store the changes in it 
dframe2 = dframe1.drop("NY")
dframe2

#to drop a column specify axis = 1 by default axis is zero 
dframe1.drop("size",axis=1)
