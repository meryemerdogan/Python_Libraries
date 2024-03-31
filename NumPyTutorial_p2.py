import numpy as np

arr = a.view() # like a pointer, arr is same as a 
arr2 = a.copy() # deep copy, another array with same contents

arr.base # returns a
arr2.base #returns none since its own objects

# Addition, subtraciton, multiplication and division
array_1 = np.array([[1,2],[3,4]])
array_2 = np.array([[5,6],[7,8]])

# Simple matrix addition
addition  = np.add(array_1, array_2)
'''
Result:
    [[ 6  8]
     [10 12]]
'''
# Simple matrix subtraction
addition  = np.subtract(array_1, array_2)
'''
Result:
    [[-4 -4]
     [-4 -4]]
'''

# Multiplies ij th element of array_1 to ij th element of array_2
multiplicaiton = np.multiply(array_1, array_2)
'''
Result:
    [[ 5 12]
     [21 32]]
'''
# Divides ij th element of array_1 to ij th element of array_2

division = np.divide(array1, array2)
'''
Result:
    [[0.2        0.33333333]
     [0.42857143 0.5       ]]
'''

# NumPy arrays are iteratble objects, so we can pass it to python for loop directly
arr = np.array([[1, 2, 3], [4, 5, 6],[7, 8, 9] ])

for x in arr:
  print(x)

'''
Result:
    [1 2 3]
    [4 5 6]
    [7 8 9]
'''
# Since all numpy arrays are iterable, all rows are iterable to so,
for x in arr:
  for i in x:
    print(i)

'''
Result:
    1
    2
    3
    4
    5
    6
    7
    8
    9
'''
# reshape methods returns a view of the object

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
arr.reshape(4,2) 
# You can also pass -1 as an argument when the last dimension is not determined
arr.reshape(4,2,-1)
#shape is (8,)

#to turn an array to 1d array, use 
arr.reshape(-1)

# Concatenating and splitting ndarrays

# Concatenating can be done in 2 ways: along existing dimensions and along a new axis
array1 = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
array2 = np.array([[[9, 10], [11, 12]], [[13, 14], [15, 16]]])

# Concatenating along existing dimensions
concatenated_axis0 = np.concatenate((array1, array2), axis=0) # axis can be 0 - 1 -2 since its a 3d array

# Concatenating along new axis
stacked_arrays = np.stack((array1, array2), axis=3) # we add a new dim


arr = np.array([1, 2, 3])

newarr = np.array_split(arr, 2)
print(newarr[0]) # [1 2]
print(newarr[1]) # [3]