import numpy as np

# Get user input for the dimensions of the array
rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))

# Get user input for the elements of the array
print("Enter the elements of the array row by row:")
arr = []
for i in range(rows):
    row_input = input(f"Enter {cols} elements for row {i + 1} separated by spaces: ")
    row_elements = [int(x) for x in row_input.split()]
    arr.append(row_elements)

# Create a NumPy array from the user input
arr = np.array(arr)

# Perform summation operations
print("Array:\n", arr)
print("Sum of all elements:", np.sum(arr))
print("Sum of all rows:", np.sum(arr, axis=1))
print("Sum of all columns:", np.sum(arr, axis=0))

