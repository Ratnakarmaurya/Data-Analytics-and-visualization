import numpy as np
import pandas as pd
from pandas import Series, DataFrame

# Making a DataFrame
dframe= DataFrame(np.arange(12).reshape((3, 4)),
                 index=['NY', 'LA', 'SF'],
                 columns=['A', 'B', 'C', 'D'])

dframe
# Just like a Series, axis indexes can also use map

#Let's use map to lowercase the city initials
dframe.index.map(str.lower)
dframe

# If you want to assign this to the actual index, you can use index
#we can save it 
dframe.index = dframe.index.map(str.lower)
dframe

# Use rename if you want to create a transformed version withour modifying the original!

#str.title will capitalize the first letter, lowercasing the columns
dframe.rename(index=str.title,columns = str.lower)

# We can also use rename to insert dictionaries providing new values for indexes or columns!
dframe.rename(columns={"A":"Alpha"},index={"ny":"NEW YORK"})
dframe #note orignal is not changed

# If you would like to actually edit the data set in place, set inplace=True
dframe.rename(columns={"A":"Alpha"},index={"ny":"NEW YORK"},inplace=True)
dframe
