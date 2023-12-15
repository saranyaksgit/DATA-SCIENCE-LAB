import numpy as np

def main():
    matrix = []
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))

    print("Enter the elements of the matrix row by row:")
    for i in range(rows):
        row = list(map(float, input().split()))
        matrix.append(row)

    matrix = np.array(matrix)

    try:
        matrix_pseudo_inverse = np.linalg.pinv(matrix)
        
        print("Inverse of the matrix:")
        print(matrix_pseudo_inverse)
    except np.linalg.LinAlgError:
        print("The matrix is not invertible.")

if __name__ == "__main__":
    main()

