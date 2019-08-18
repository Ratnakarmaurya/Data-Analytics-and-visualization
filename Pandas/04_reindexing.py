import numpy as np

from pandas import Series,DataFrame

import pandas as pd

ser1 =Series([1,2,3,4],index=["A","B","C","D"])
ser1

#Call reindex to rearrange the data to a new index
ser2 = ser1.reindex(['A','B','C','D','E','F'])
ser2

# We can alos fill in values for new indexes
ser2.reindex(['A','B','C','D','E','F','G'],fill_value = 0)

#Using a particular method for filling values
ser3 = Series(['USA','Mexico','Canada'],index=[0,5,10])
ser3

ranger =range(15)
ranger
# and the method is ffill 
#Can use a forward fill for interploating values vetween indices 
ser3.reindex(ranger,method ="ffill" )

#Reindexing rows, columns or both
#making a dataframe and reshaping it to avoid one dimentional dframe
#Notice we forgot 'C' , lets reindex it into dframe
dframe = DataFrame(np.random.randn(25).reshape((5,5)),
                   index=['A','B','D','E','F'],columns=["col1","col2","col3","col4","col5"])
dframe

#reindexing "C" in dframe
dframe2 = dframe.reindex(['A','B','C','D','E','F'])
dframe2

#Can also explicitly reindex columns
new_columns =["col1","col2","col3","col4","col5","col6"]


dframe.reindex(columns=new_columns)

#Reindex quickly using the label-indexing with ix (we'll see this more in the future)

#ix is deprecated in new version of pandas , hEnce use dframe.loc

dframe.loc[['A','B','C','D','E','F'],new_columns]
