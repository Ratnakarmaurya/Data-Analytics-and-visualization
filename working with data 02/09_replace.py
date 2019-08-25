import numpy as np
import pandas as pd
from pandas import Series, DataFrame

ser1= Series([1,2,3,4,1,2,3,4])

# Using replace we can select --> .replace(value to be replaced, new_value)
ser1.replace(1,np.nan)

#Can also input lists
ser1.replace([2,3],[200,300])#2 and 3 replace with 200 300 respectively

ser1 #note origanal data has not changed

#Can also input dictionary
ser1.replace({4:np.nan})


