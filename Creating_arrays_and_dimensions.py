#Numpy - Creating Arrays and Dimensional Arrays

# Import relevant modules

import numpy

# Creating Simple array and one dimension arrays are same
Simple_Array = numpy.array([1,2,3,4,5])
print('Simple array :', Simple_Array)
print('Above given array size :',Simple_Array.ndim) # to print what dimension it is

# Zero dimensional Array
Zero_Dimensional_array = numpy.array(123456789)
print('Zero_Dimensional_array : ', Zero_Dimensional_array)
print('Above given array size :',Zero_Dimensional_array.ndim)

# Two Dimensional array
Two_Dimensional_array = numpy.array([[1,2,3,4],[5,6,7,8]])
print('Two_Dimensional_array : ', Two_Dimensional_array)
print('Above given array size :',Two_Dimensional_array.ndim)

# Three Dimensional array
Three_Dimensional_array = numpy.array([[[1,2,3,4],[5,6,7,8]],[[1,2,3,4],[5,6,7,8]]])
print('Three_Dimensional_array : ', Three_Dimensional_array)
print('Above given array size :',Three_Dimensional_array.ndim)

# To print three dimensional array
Print_Three_Dimensional_array = numpy.array(100, ndmin = 5)
print('Creating an array with ndmin :',Print_Three_Dimensional_array)
