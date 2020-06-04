#NUMPY ARRAYS FOR RANKING...

import numpy as np

# Create Array of Rank 1'

my_l1 = np.array([1,2,3,4])
print(my_l1)
print(my_l1.ndim)
print(my_l1 [3])
print ("")

# Create Array of Rank 2'

my_ra2 = np.array([[1,2,3,4], [5,6,7,8]])
print(my_ra2)
print(my_ra2.ndim)
print(my_ra2 [1, 3])
print ("")

# Create Array of Rank 3

my_arr = np.array([[[1,2,3,4], [5,6,7,8], [9,10,11,12]]])
print(my_arr)
print(my_arr.ndim)
print(my_arr [0, 2, 3])
print(my_arr.shape)
print ("")

# Create Array of Rank 4

my_arr1 = np.array([[[[2,4,6,8], [10,12,14,16], [18,20,22,24], [26,28,30,32]]]])

print(my_arr1)
print(my_arr1.ndim)
print(my_arr1 [0, 0, 3, 3])
print(my_arr1.shape)
print(my_arr1.size)
print(type(my_arr1))
print ("")

# Create Array of Rank 5
my_arr2 = np.array([[[[[10,20,30,40], [50,60,70,80], [90,100,110,120], [130,140,150,160], [170,180,190,200]]]]])

print(my_arr2) 
print(my_arr2.ndim)
print(my_arr2 [0, 0, 0, 4, 3])
print(my_arr2.shape)
print(my_arr2.size)
print(type(my_arr2))
print ("")
