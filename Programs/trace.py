import numpy as np

rows = int(input("Enter the number of rows: "))
columns = int(input("Enter the number of columns: "))

matrix = []
for i in range(rows):
    row = []
    for j in range(columns):
        element = float(input(f"Enter the value for element ({i+1},{j+1}): "))
        row.append(element)
    matrix.append(row)

matrix_np = np.array(matrix)

trace = np.trace(matrix_np)

print("Trace of the matrix is:", trace)

