import numpy as np
import pandas as pd
from pandas import Series,DataFrame 

dframe = DataFrame({"key1":["A"]*2 + ["B"]*3,
                    "key2":[2,2,2,3,3]})

#We can use duplicated to find duplicates
dframe.duplicated()

#we can get rid of duplicates by droping them
dframe.drop_duplicates()
#You can filter which duplicates to drop by a single column
#we can also drop duplicate only from a specific column
dframe.drop_duplicates("key1")#this will drop the row where the letter is duplicated in key1 column
#By default the first value was taken for the duplicates, we can also take the last value instead
#this will take the last duplicate instance or obj
dframe.drop_duplicates(["key1"],keep="last")#take_last replaced by keep in python 3
