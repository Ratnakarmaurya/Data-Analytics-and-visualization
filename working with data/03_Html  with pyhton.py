import numpy as np
from pandas import Series,DataFrame
import pandas as pd

from pandas import read_html
#Lets grab a url for list of failed banks
url ="http://www.fdic.gov/bank/individual/failed/banklist.html"

"""
IMPORTANT NOTE: NEED TO HAVE beautiful-soup INSTALLED as well as html5lib !!!!
"""
# Grab data from html and put it intop a list of DataFrame objects!
dframe_list = pd.io.html.read_html(url)
dframe_list
#Grab the first list item from the data base(list of datas) and set as a DataFrame
dframe = dframe_list[0]

dframe.columns.values
