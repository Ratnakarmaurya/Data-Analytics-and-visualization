import numpy as np
import matplotlib.pyplot as plt

points =np.arange(-5,5,0.01)
dx,dy = np.meshgrid(points,points)
dx
dy
type(dx)
dx.shape


z = np.sin(dx) + np.sin(dy)
z
plt.imshow(z)
plt.imshow(z)
plt.colorbar()
plt.title("sin of x + sin of y")


#numpy where
A =np.array([1,2,3,4])

B = np.array([100,200,300,400])

condition =np.array([True,True,False,False])
condition

answer =[a_val if cond else b_val for a_val,b_val,cond in zip(A,B,condition)]
answer 

#so numpy where did same thing withou  list comprhension
answer2 =np.where(condition,A,B)
answer2


#Note: We can import any module specifically to avoid typing np.randn every time istead we can call randn 
from numpy.random import randn

arr=randn(5,5)
arr

np.where(arr<0,0,arr)

#sum
arr =np.array([[1,2,3],[4,5,6],[7,8,9]])

arr.sum()

arr.sum(0) 

arr.mean()

arr.var()

bool_arr = np.array([True,False,True,False])
bool_arr.any() #return if any value is true else false

bool_arr.all()#return true if all true


#sort
arr =randn(5)
arr
arr.sort()
arr

countries = np.array(["France","Germany","USA","Mexico","Germany","Russia","Germany"])
np.unique(countries)

np.in1d(["France","Sweden","USA"],countries)
























