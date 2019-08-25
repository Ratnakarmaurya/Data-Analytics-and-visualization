import numpy as np
import pandas as pd
from pandas import Series,DataFrame #note D and F are Capital in DataFrame
from numpy.random import randn


# Create DataFrame
#reason why we used pd.Index is because we cane name it along with indexing in same line
dframe1 = DataFrame(np.arange(8).reshape((2, 4)),
                 index=pd.Index(['LA', 'SF'], name='city'),
                 columns=pd.Index(['A', 'B', 'C','D'], name='letter'))
#Show
dframe1
# Use stack to pivot the columns into the rows
dframe_st=dframe1.stack()
dframe_st
#We can always rearrange back into a DataFrame
dframe_st.unstack()
#We can choose which level to unstack by levels zero is row level 1 and 1 is row level 2
#as stuck rotate columns to row there fore no columns values are in  dframe_St
dframe_st.unstack(1) 
# Also by which name to unstack(row rotates to columns here letter is row in dframe_stuck) by 
dframe_st.unstack("letter") 

dframe_st.unstack("city")

# Let's see how stack and unstack handle NAN

#Make two series
ser1 = Series([0, 1, 2], index=['Q', 'X', 'Y'])
ser2 = Series([4, 5, 6], index=['X', 'Y', 'Z'])

#Concat to make a dframe
dframe = pd.concat([ser1, ser2], keys=['Alpha', 'Beta'])

type(dframe) #as we see this a still a series packed or stacked together
#to convert it to dataframe we need to unstack it

unstacked_df=dframe.unstack()
unstacked_df #now it is a data frame note we have nan values 

#if we stack back the unstacked dataframe it stacks back to series with no null values
# Now stack will filter out NAN by default
unstacked_df.stack() 

#if we want to include the nan
unstacked_df.stack(dropna = False)







 
