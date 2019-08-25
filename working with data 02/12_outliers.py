# Let's see how we would find outliers in a dataset
import numpy as np
import pandas as pd
from pandas import Series, DataFrame
# First we'll seed the numpy generator
np.random.seed(12345)
#Next we'll create the dataframe
dframe = DataFrame(np.random.randn(1000,4))
dframe.head()

# Lets describe the data
dframe.describe()

# Lets select the first column
col = dframe[0]

# NOw we can check which values in the column are greater than 3, for instance.
col[np.abs(col)>3]

# So we now know in column[0], rows 523 and 900 have values with abs > 3

#How about all the columns?

# We can use the "any" method
dframe[(np.abs(dframe)>3).any(1)]
#any method just look for 3 in any column and return any containg row 

#we could also cap the data at 3
dframe[(np.abs(dframe)>3)] = np.sign(dframe)*3 #this fetches num > 3 with any sign and caps it with 3
dframe.describe() #note min and max is now changed to -3 and 3 respectively