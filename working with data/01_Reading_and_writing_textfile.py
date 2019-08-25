import numpy as np
from pandas import Series,DataFrame
import pandas as pd
#reading csv path where csv should be in the working directory
dframe = pd.read_csv("01_csv.csv")

#by using header the column is indexed with the number if the orignal csv doesnt contain index in row 0 that is column 
#If we dont want the header to be the first row
dframe = pd.read_csv("01_csv.csv",header= None)
dframe


dframe =pd.read_table("01_csv.csv",sep=",",header=None) #read_table is desprected ,use read_csv instead

pd.read_csv("01_csv.csv",header = None,nrows=2) #indicate  the number of rows you want 
dframe
#we can write DataFrames out to text files
dframe.to_csv("Mytextdata_out.csv")#saves in workind directory

#  We can also use other delimiters
#import sys to see the output
import sys
#Use sys.stdout to see the output directly and not save it
dframe.to_csv(sys.stdout)
dframe.to_csv(sys.stdout, sep="_")
dframe.to_csv(sys.stdout,sep="{")
#We can also choose to write only a specific subset of columns
dframe.to_csv(sys.stdout,columns=[0,1,2])

#You should also check out pythons built-in csv reader and writer for more info:
import webbrowser 

website = "https://docs.python.org/2/library/csv.html"
webbrowser.open(website)

    