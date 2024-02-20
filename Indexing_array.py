#Numpy - Creating Arrays and Dimensional Arrays

# Import relevant modules

import numpy

# # Creating Simple array and one dimension arrays are same
# Simple_Array = numpy.array([1,2,3,4,5])
# print('Simple array :', Simple_Array)
# print('Above given array size :',Simple_Array.ndim) # to print what dimension it is
# print('one-dimensional array with index of 0:', Simple_Array[0])

# # Zero dimensional Array
# Zero_Dimensional_array = numpy.array(123456789)
# print('Zero_Dimensional_array : ', Zero_Dimensional_array)
# print('Above given array size :',Zero_Dimensional_array.ndim)
# print('Zero-dimensional array with index of 0:', Zero_Dimensional_array[0])

# # Two Dimensional array
# Two_Dimensional_array = numpy.array([[1,2,3,4],[5,6,7,8]])
# print('Two_Dimensional_array : ', Two_Dimensional_array)
# print('Above given array size :',Two_Dimensional_array.ndim)
# print('Two-dimensional array with index of 12:', Two_Dimensional_array[1,2])

# Three Dimensional array
Three_Dimensional_array = numpy.array([[[1,2,3,4],[5,6,7,8]],[[9,10,11,12],[13,14,15,16]]])
print('Three_Dimensional_array : ', Three_Dimensional_array)
print('Above given array size :',Three_Dimensional_array.ndim)
print('Three-dimensional array with index of 110:', Three_Dimensional_array[1,1,0]) # works exactly like a math matrics
print('Three-dimensional array to return [13,14,15,16]:', Three_Dimensional_array[1,1])
print('Three-dimensional array to return [[1,2,3,4],[5,6,7,8]]:', Three_Dimensional_array[0])


# # To print three dimensional array
# Print_Three_Dimensional_array = numpy.array(100, ndmin = 5)
# print('Creating an array with ndmin :',Print_Three_Dimensional_array)