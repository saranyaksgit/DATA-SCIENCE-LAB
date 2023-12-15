import numpy as np

n = int(input('Enter the size of the array: '))

arr1 = input('Enter the elements in first array: ').split()
arr1 = [int(i) for i in arr1] 

arr2 = input('Enter the elements in second array: ').split()
arr2 = [int(i) for i in arr2] 

narr1 = np.array(arr1)
narr2 = np.array(arr2)
result_variable = (narr1 == narr2).all()

if result_variable:
	print('The given arrays are equal.')
else:
	print('The given arrays are not equal.')

