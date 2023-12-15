import numpy as np

m1 = int(input("Enter the number of rows for the first matrix: "))
n1 = int(input("Enter the number of columns for the first matrix: "))

print("Enter the elements of the first matrix:")
matrix1 = []
for i in range(m1):
    row = []
    for j in range(n1):
        row.append(float(input(f"Enter element ({i},{j}): ")))
    matrix1.append(row)

m2 = int(input("Enter the number of rows for the second matrix: "))
n2 = int(input("Enter the number of columns for the second matrix: "))

print("Enter the elements of the second matrix:")
matrix2 = []
for i in range(m2):
    row = []
    for j in range(n2):
        row.append(float(input(f"Enter element ({i},{j}): ")))
    matrix2.append(row)

if n1 != m2:
    print("Matrix multiplication is not possible because the number of columns in the first matrix does not match the number of rows in the second matrix.")
else:
    product = np.dot(matrix1, matrix2)
    print("Product of the two matrices:")
    print(product)

