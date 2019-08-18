import numpy as np
arr = np.arange(0,11)
arr

#indexing
arr[8]
arr[1:5]

arr[0:5]


#setting value using indexing
arr[0:5]=100
arr[0:5]
arr[:]

arr = np.arange(0,11)
arr

#slicing
slice_of_arr = arr[0:6]
slice_of_arr

slice_of_arr[:] = 99
slice_of_arr
arr #in array the data isnt copied it is just view of the orirgnal arrray thats y we see change in arr too

#so for copying
arr_copy = arr.copy()
arr_copy

#indexing in 2d Array 
arr_2d = np.array([[5,10,15],[20,25,30],[35,40,45]])
type(arr_2d)
arr_2d
arr_2d.shape

#indexing in  2d matrix
arr_2d[1] #1 is the row index
arr_2d[0]
arr_2d[1][0] # [row][column]
arr_2d[1]=0
arr_2d
#2d array slicing
arr_2d
arr_2d[:2,1:] # all the way upto 2 that is 0 and 1 row , beyond 1 that is 1 and 2 colomn

arr_2d[-1] #works like list gives bottom row


#fancy indexing

arr2d =np.zeros((10,10))
arr2d
arr_length = arr2d.shape[1]
arr_length

for i in range(arr_length):
    arr2d[i]=i
    
arr2d
#here is fancy indexing
arr2d[[2,4,5,6]]
arr2d[[3,4,5,6],[2]
arr2d[8:,1:3]










