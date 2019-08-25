import numpy as np
from pandas import Series,DataFrame
import pandas as pd

"""
IMPORTANT NOTE: NEED TO HAVE xlrd AND openpyxl INSTALLED!!!
"""
# Open the excel file as an object
xlsfile =pd.ExcelFile("04_test.xlsx")
# Parse the first sheet of the excel file and set as DataFrame
dframe = xlsfile.parse("Sheet1") #this is how we use import excel files using pandas
dframe

























































