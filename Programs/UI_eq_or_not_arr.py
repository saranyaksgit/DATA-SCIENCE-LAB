import numpy as np

# Get user input for the elements of the first array
arr1_input = input("Enter elements for Array 1 separated by spaces: ")
arr1 = np.array([int(x) for x in arr1_input.split()])

# Get user input for the elements of the second array
arr2_input = input("Enter elements for Array 2 separated by spaces: ")
arr2 = np.array([int(x) for x in arr2_input.split()])

# Print the user input arrays
print("Array1:", arr1)
print("Array2:", arr2)

# Compare the arrays for equality
if np.array_equal(arr1, arr2):
    print("The two arrays are equal.")
else:
    print("The two arrays are not equal.")

