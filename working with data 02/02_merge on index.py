# how to merge data sets by linking rows by keys.
import numpy as np
import pandas as pd
from pandas import Series, DataFrame

df_left = DataFrame({'key': ['X','Y','Z','X','Y'],
                  'data': range(5)})
df_right = DataFrame({'group_data': [10, 20]}, index=['X', 'Y'])
#now we will use key for the left DF and index for the Right

pd.merge(df_left,df_right,left_on="key",right_index=True)
# We can also get a union by using outer
 #note z is null because index doesnt has z
pd.merge(df_left,df_right,left_on="key",right_index=True,how="outer")

#using index hirarcy to understand this much better 
df_left_hr = DataFrame({'key1': ['SF','SF','SF','LA','LA'],
                   'key2': [10, 20, 30, 20, 30],
                   'data_set': np.arange(5.)})

df_right_hr = DataFrame(np.arange(10).reshape((5, 2)),
                   index=[['LA','LA','SF','SF','SF'],
                          [20, 10, 10, 10, 20]],
                   columns=['col_1', 'col_2'])
# Now we can merge the left by using keys and the right by its index
pd.merge(df_left_hr,df_right_hr,left_on=["key1","key2"],right_index=True)
# We can alo keep a union by choosing 'outer' method
pd.merge(df_left_hr,df_right_hr,left_on=["key1","key2"],right_index=True,how="outer")

# WE can also you .join()

df_left.join(df_right)
