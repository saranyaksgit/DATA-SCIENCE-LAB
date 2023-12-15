import numpy as np

def mat():
    while True:
        r = int(input("Enter the number of rows: "))
        c = int(input("Enter the number of cols: "))

        if r == c:
            break
        else:
            print("Not a square matrix. Please enter the same number of rows and columns.")

    matrix = np.empty((r, c), dtype=float)
    for i in range(r):
        for j in range(c):
            matrix[i, j] = float(input(f"Enter the elements at({i+1},{j+1}):"))

    return matrix

print("Matrix Details")
matrix1 = mat()

print("\nMatrix:")
print(matrix1)

detr = np.linalg.det(matrix1)
if detr == 0:
    print("\nMatrix is singular. It does not have an inverse.")
else:
    inverse = np.linalg.inv(matrix1)
    print("\nInverse:")
    print(inverse)

print("\nTrace:")
trace = np.trace(matrix1)
print(trace)

print("\nDeterminant:")
print(detr)

print("\nTranspose:")
trs = np.transpose(matrix1)
print(trs)

