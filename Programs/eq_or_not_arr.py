import numpy as np

arr1 = np.array([1, 3, 5])
arr2 = np.array([5, 3, 5])

print("Array1:", arr1)
print("Array2:", arr2)

if np.array_equal(arr1, arr2):
    print("The two arrays are equal.")
else:
    print("The two arrays are not equal.")

