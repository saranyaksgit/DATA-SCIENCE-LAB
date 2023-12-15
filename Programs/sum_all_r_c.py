import numpy as np

arr = np.array([[3, 5],
                [2, 4]])

print("Array:\n", arr)
print("Sum of all elements:", np.sum(arr))
print("Sum of all rows:", np.sum(arr, axis=1))
print("Sum of all columns:", np.sum(arr, axis=0))

