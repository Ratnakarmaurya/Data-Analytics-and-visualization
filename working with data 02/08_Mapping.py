import numpy as np
import pandas as pd
from pandas import Series, DataFrame

# Let's create a dframe to work with (Highest elevation cities in USA)
dframe = DataFrame({'city':['Alma','Brian Head','Fox Park'],
                    'altitude':[3158,3000,2762]})


dframe
#Now let's say we wanted to add a column for the States, we can do that with a mapping.
state = {"Alma":"Colorado","Brian Head":"Utah","Fox Park":"Wyoming"}
# Now we can map that data to our current dframe
dframe["State"]=dframe["city"].map(state)#python matches the city in state and inputs in proper place

# Mapping is a great way to do element-wise transfomations and other data cleaning operations!
dframe.columns.map(str.upper) #we can use map for various tweaks read documentation
