import numpy as np
import pandas as pd
from pandas import Series, DataFrame

# WE can randomly reorder (permutate) a Series, or the rows in a DataFrame
dframe = DataFrame(np.arange(16).reshape(4,4))
#creating random permutation
blender = np.random.permutation(4) #permutation means reorder
blender
dframe.take(blender)#this will reorder or permute dframe rows with the permutation blender
# Now what if we want permuations WITH replacement
#make a box with 3 marbles
box = np.array([1,2,3])
box
#randint takes the integer low high and return inputed size of array
# Now lets create a random permuation WITH replacement using randint
shaker = np.random.randint(0,len(box),size=5) #we will use take later and use shaker as index of box
shaker
#Now lets grab form the box
#both example are using same logic
hand_picks = box.take(shaker) #taking permutation of shaker
hand_picks #these are the marbles
