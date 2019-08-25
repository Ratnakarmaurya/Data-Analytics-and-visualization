import numpy as np
import pandas as pd
from pandas import Series, DataFrame

years = [1990,1991,1992,2008,2012,2015,1987,1969,2013,2008,1999]

# We can seperate these years by decade 
#making a category a bucket of decades here later we will cut and sort years in this 
decade_bins = [1960,1970,1980,1990,2000,2010,2020]

#Now we'll use cut to get somethign called a Category object
decade_cat = pd.cut(years,decade_bins) #cut(X,Category or int ,precision 1)
decade_cat

# We can check the categories using .categories
decade_cat.categories
decade_cat

# Then we can check the value counts in each category
pd.value_counts(decade_cat)

# We can also pass data values to the cut.

#For instance, if we just wanted to make two bins,
#evenly spaced based on max and min year, with a 1 year precision
pd.cut(years,2,precision=1) #precision give how much it will round off 1 means no rounding off
# One last thing to note, jus tlike in standard math notation, when setting up bins:
# () means open, while [] means closed/inclusive