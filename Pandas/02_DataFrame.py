import numpy as np
import pandas as pd
#SERIES is A one dimentional Column or data frame
#data frames are 2 d
from pandas import Series, DataFrame #imported DataFrame And series to avoid typing pd. everytime
#Webbrowser lets us browse internet from the ide itself
import webbrowser
website = "http://en.wikipedia.org/wiki/NFL_win-loss_records"
webbrowser.open(website) #this will open browser

#reading the clip board by making dataframe of copied sheets on website or from any where.
#Stupendous feature
nfl_frame = pd.read_clipboard()
nfl_frame

#grabing all column names
nfl_frame.columns

#we can grab a particuallar column by the_frame.name_of_column
nfl_frame.Rank
nfl_frame.Team



#the above method can be used only of the columns which has single word 
#for more than single word we use:
nfl_frame["First NFL Season"]

#grab Multiple Columns
DataFrame(nfl_frame,columns=["Team","First NFL Season","Rank"])

#Pandas fills the column which is not exisiting with NaN
DataFrame(nfl_frame,columns=["Team","First NFL Season","Rank","Score"])

#We can retrieve rows through indexing
nfl_frame.ix[3]

#for retriving any number of row data from top (Default is 5rows)
nfl_frame.head(1)

#same from bottom we can use 
nfl_frame.tail(3)

#assisnging values to entire columns

nfl_frame["Score"]=9800
nfl_frame

##Putting numbers for score

nfl_frame["Score"]=np.arange(5)
nfl_frame

#Adding a Series to a DataFrame
score = Series(["Good","Bad Score"],index=[4,0])

#Now input into the nfl DataFrame
nfl_frame["Score"]= score
nfl_frame

#deleting column
del nfl_frame["Score"]
nfl_frame

#DataFrames can be constructed many ways. Another way is from a dictionary of equal length lists
data = {"City":["SF","LA","NYC"],"Population":[837000,334233,4500000]}
city_frame =DataFrame(data)
city_frame
