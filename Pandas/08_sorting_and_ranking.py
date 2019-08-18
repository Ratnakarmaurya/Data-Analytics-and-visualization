import numpy as np
from pandas import Series, DataFrame
import pandas as pd
from numpy.random import randn

ser1 =Series(range(3),index=list("CAB"))
ser1

ser1.sort_index()#sort index

ser1.sort_values() #ser1.order is no more in new pandas #sorts values

#creaate random 10 floats series
ser2 = Series(randn(10))
ser2


ser3=ser2.sort_values() #sort and vazlue function are now sort_values

ser3.rank()
