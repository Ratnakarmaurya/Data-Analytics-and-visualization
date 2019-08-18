import numpy as np
from pandas import Series,DataFrame
import pandas as pd

from numpy.random import randn
#pandas allows you to have multiple index levels, which is very clear with this example:
ser1 = Series(randn(6),index=[[1,1,1,2,2,2],["a","b","c","a","b","c"]])
ser1
# We can check the multiple levels
ser1.index
#Now we can sleect specific subsets
ser1[1]
ser1[2]
# We can also select from an internal index level ser1[1st level,2nd level]
ser1[:,"a"]
# We can also create Data Frames from Series with multiple levels
dframe = ser1.unstack()
dframe
# We can also apply multiple level indexing to DataFrames
dframe2 =DataFrame(np.arange(16).reshape(4,4),index=[["a","a","b","b"],[1,2,1,2]]
,columns=[["NY","NY","LA","SF"],["cold","hot","hot","cold"]])
dframe2
# We can also give these index levels names

#Name the index levels
dframe2.index.names=["index_1","index_2"]
#Name the column levels
dframe2.columns.names=["Cities","Temp"]
dframe2
# We can also interchange level orders (note the axis=1 for columns)
dframe2.swaplevel("Cities","Temp",axis=1)

#We can also sort levels
dframe2.sort_index(level =1)#workaround sortlevel is removed 

#Note the change in sorting, now the Dframe index is sorted by the INDEX_2
#We can also perform operations on particular levels
dframe2.sum(level=1,axis=1) #we can use number or name in level
