import numpy as np
from pandas import Series, DataFrame
import pandas as pd

my_ser = Series([1,2,3,4],index=["A","B","C","D"])
my_ser


my_index = my_ser.index
my_index


#Get the index
my_index[2]

#Can grab index ranges same like list indexing `

#What happens if we try to change an index value?
my_index[2:]

try:
    my_index[0]="Z"
    
except:
    print("Index values are immutable")