import numpy as np

rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))

if rows == cols:
   
    matrix = np.zeros((rows, cols))

    print("Enter the values of the matrix:")
    for i in range(rows):
        for j in range(cols):
            matrix[i][j] = float(input(f"Enter the element at row {i+1}, column {j+1}: "))

    print("Matrix is:")
    print(matrix)

    det = np.linalg.det(matrix)
    print("\nDeterminant of the given matrix:")
    print(det)
else:
    print("The matrix is not square. Determinant calculation is not possible.")

