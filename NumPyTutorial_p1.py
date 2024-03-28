# My NumPy notes + some exercies for absolute beginners 
    
# --> NumPy arrays are stored in memeory consecutively
#       i.e. arr = np.array([1,2,3]) is stored [1],[2],[3] in memory without any gaps 
#       So, accessing and manipulating array elemnts in np is more efficent


# First import numpy to the project
import numpy

# Create an array 
arr = numpy.array([1])

# Use np alias by convention
import numpy as np

# To check numpy version use
np.__version__

# Arrays in numpy are called ndarray
# Create ndarrays using np.array() function
arr = np.array([1, 2, 3, 4, 5])

# Create 0D array:
arr = np.array(10)
# Output: 10 --> Without any curly brackets 

# Create 1D array from List:
arr = np.array([1])
# Output: [1]

# Create 1D array from List:
list_data = [1, 2, 3, 4, 5]
arr = np.array(list_data)
# Output: [1 2 3 4 5]

# Create 1D array from Tuple:
tuple_data = (1, 2, 3, 4, 5)
arr = np.array(tuple_data)
# Output: [1 2 3 4 5]

# Create 2D array from Nested List:
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
arr_2d = np.array(nested_list)
# Output:
# [[1 2 3]
#  [4 5 6]
#  [7 8 9]]

# Create 2D array from Nested Tuple:
tuple_data = ((1, 2, 3),
              (4, 5, 6),
              (7, 8, 9))

# Create a 2D NumPy array from the tuple
arr_2d = np.array(tuple_data)

# Output:
# [[1 2 3]
#  [4 5 6]
#  [7 8 9]]

# So any array-like object can be used in np.array() method
# We can specify other properties of nparray while creating the array

# dytpe specficies the data type of array element
arr_float = np.array(list_data, dtype=np.float64)

# You can specify the data type of the  elements in the array 
# after initialization using the .astype() method:
arr = np.array([1, 2, 3, 4, 5]) # dytpe is int by default
# Convert the array to float data type
arr_float = arr.astype(np.float64)
