import numpy as np

# Get user input for array 1
arr1_input = input("Enter elements for Array 1 separated by spaces: ")
arr1 = np.array([int(x) for x in arr1_input.split()])

# Get user input for array 2
arr2_input = input("Enter elements for Array 2 separated by spaces: ")
arr2 = np.array([int(x) for x in arr2_input.split()])

# Perform element-wise addition
arr3 = np.add(arr1, arr2)

# Print the arrays and the result
print("Array 1:", arr1)
print("Array 2:", arr2)
print("Added array:", arr3)

