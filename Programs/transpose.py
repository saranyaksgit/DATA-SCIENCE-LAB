import numpy as np

rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))

print("Enter values for the first matrix:")
matrix1 = np.zeros((rows, cols), dtype=float)

for i in range(rows):
    for j in range(cols):
        matrix1[i][j] = float(input(f"Enter the value at ({i+1}, {j+1}): "))

print("\nMatrix :")
print(matrix1)

transpose1 = np.transpose(matrix1)
print("\nTranspose of Matrix :")
print(transpose1)

