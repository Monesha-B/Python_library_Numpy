# #Numpy - Slicing arrays

# Import relevant modules

import numpy

# slicing one dimensional arrays
One_dimensional_array = numpy.array([1,2,3,4,5])
print(One_dimensional_array[1:3])
print(One_dimensional_array[0:4])
print(One_dimensional_array[1:])
print(One_dimensional_array[:1])
print(One_dimensional_array[:])
print(One_dimensional_array[:5:2])

# Slicing Two_Dimensional array
Two_dimensional_array = numpy.array([[1,2,3,4,5],[6,7,8,9,10]])
print(Two_dimensional_array[1, 0:2])

# Slicing another Two_Dimensional array
Two_dimensional_array = numpy.array([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]])
print(Two_dimensional_array[0:3, 0])
print(Two_dimensional_array[0:3, 0:2])


#Slicing Three dimensional arrays

