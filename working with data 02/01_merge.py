import numpy as np
from pandas import Series,DataFrame
import pandas as pd
#keys are colums and respectives are values of key
#creating datframe using dictionery
dframe = DataFrame({"key":["X","Z","Y","Z","X","X"],"data_set1":np.arange(6)}) 
dframe

dframe2 =DataFrame({"key":["Q","Y","Z"],"data_Set_2":[1,2,3]})
dframe2

pd.merge(dframe,dframe2) #on is default set to common columns
# Merge will automatically choose overlapping columns to merge on
pd.merge(dframe,dframe2,on="key") #will give same as column column is set default in on
pd.merge(dframe,dframe2,on="key",how="left")
pd.merge(dframe,dframe2,on="key",how="right")
#for union of both dataset
pd.merge(dframe,dframe2,on="key",how="outer")

#many to many merge
dframe3 = DataFrame({'key': ['X', 'X', 'X', 'Y', 'Z', 'Z'],
                 'data_set_3': range(6)})

dframe4 = DataFrame({'key': ['Y', 'Y', 'X', 'X', 'Z'],
                 'data_set_4': range(5)})
#So what happened? A many to many merge results in the product of the rows. 
#Because there were 3 'X's in dframe3 
#and 2 'X's in dframe4 there ended up being a total of 6 'X' rows 
#in the result (2*3=6)! Note how dframe3 repeats its 0,1,2 values for 'X' and
# dframe4 repeats its '2,3' pairs throughout the key set. \
pd.merge(dframe3,dframe4,on="key",how="inner",indicator=True)
# We can also merge with multiple keys!
# Dframe on left
df_left = DataFrame({'key1': ['SF', 'SF', 'LA'],
                  'key2': ['one', 'two', 'one'],
                  'left_data': [10,20,30]})

#Dframe on right
df_right = DataFrame({'key1': ['SF', 'SF', 'LA', 'LA'],
                   'key2': ['one', 'one', 'one', 'two'],
                   'right_data': [40,50,60,70]})

pd.merge(df_left,df_right,on=["key1","key2"])
#Note that the left and right DataFrames have overlapping key names (key1 and key2).
# pandas automatically adds suffixes to them
# We can also specify what the suffix becomes
pd.merge(df_left,df_right,on=["key1"],how="outer",suffixes=("_lefty","_righty"))

# For more info on merge parameters check out:
url = 'http://pandas.pydata.org/pandas-docs/dev/generated/pandas.DataFrame.merge.html'
