import numpy as np
my_list1 = [1, 2,3,4]

#Creating an array
my_array1 = np.array(my_list1)
my_array1

#creating multidimentional array here
my_list2 =[11,22,33,44]
my_lists =[my_list1,my_list2]
my_array2= np.array(my_lists)
my_array2

#shape of the array, get the dimention
my_array2.shape 

#datatype of the array 
my_array2.dtype

#Creating a zero matrix
np.zeros([5]) #to create multidimentional Zero Matrix Give Row And Coloums In List np.zeros([5,5])

my_zeros_array = np.zeros(5)
my_zeros_array.dtype

#creating an array of ones
np.ones([5,5])
#creating an empty array 
np.empty(5)

#creating an identity matrix
np.eye(5)


# not incluting 5 
np.arange(5)
np.arange(5,50,2)

