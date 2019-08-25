#concatenating along an axis
import numpy as np
import pandas as pd
from pandas import Series, DataFrame

#concatination in numpy
arr1 = np.arange(9).reshape((3,3))
arr1
np.concatenate([arr1,arr1],axis = 1) #both side by side
np.concatenate([arr1,arr1],axis = 0)#on top of each other

#using pandas
ser1 = Series([0,1,2],index=(["T","V","W"]))
ser2 = Series([3,4],index=(["X","Y"]))

pd.concat([ser1,ser2])#concatinating series using pandas

pd.concat([ser1,ser2],axis=1) #note here this make it a dataframe

pd.concat([ser1,ser2],axis=0) #note by defaul axis = 0
# We can specify which specific axes to be used
pd.concat([ser1,ser2],axis=1,join_axes=[['U','V','T']])#works only on column as its joins the respective axes

# Lets say we wanted to add markers.keys to the concatenation result
# WE can do this with a hierarchical index
pd.concat([ser1,ser2],keys=["cat1","cat2"]) #cat1 corresponds to ser1 and so on

#so everything works similarly in DataFrames

dframe1 = DataFrame(np.random.randn(4,3), columns=['X', 'Y', 'Z'])
dframe2 = DataFrame(np.random.randn(3, 3), columns=['Y', 'Q', 'X'])

pd.concat([dframe1,dframe2]) #here note the index are not contiuation of concationation
#If we dont care about the index info and 
#just awnt to make a complete DataFrame, just use ignore_index
pd.concat([dframe1,dframe2],axis=0,ignore_index=True)#concats on top of each other
pd.concat([dframe1,dframe2],axis=1,ignore_index=True)#concats on side of each other
