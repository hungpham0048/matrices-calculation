import csv  # import csv file
import numpy as np  # import numpy with the shortcut "np"
# Book1 calculation
print("\nCalculate matrices in Book1\n")
# set up matrix as a variable
matrix1 = np.loadtxt('Book1.csv', delimiter=',', skiprows=1,
                     max_rows=3)  # skiprows =  x: bo qua x lines
matrix2 = np.loadtxt('Book1.csv', delimiter=',', skiprows=5,
                     max_rows=3)  # max_rows = x: doc toi da x rows

# print the matrices
print(f"Matrix 1:\n{matrix1}")  # \n xuong dong
print(f"\nMatrix 2:\n{matrix2}")

# set up variables and print sum/subtraction
sum1 = matrix1 + matrix2
sub1 = matrix1 - matrix2
sub2 = matrix2 - matrix1
print(f"\nSum:\n{sum1}")
print(f"\nMatrix 1 - Matrix 2:\n{sub1}")
print(f"\nMatrix 2 - Matrix 1:\n{sub2}")

# check the condition for multiplication
if matrix1.shape[1] == matrix2.shape[0]:
    mul1_1 = matrix1 @ matrix2
    print(f"\nMatrix 1 x Matrix 2:\n {mul1_1}")
elif matrix2.shape[1] == matrix1.shape[0]:
    mul1_2 = matrix2 @ matrix1
    print(f"Matrix 2 x Matrix 1:\n {mul1_2}")
else:
    print("\nThe sizes are invalid for multiplication!")

# determinant calculation
# np.linalg.det() can find det of a matrix in numpy, .inv()
det1 = np.linalg.det(matrix1)
print(f"\nThe determinant of the matrix 1 is {round(det1, 0)}.")
det2 = np.linalg.det(matrix2)
print(f"\nThe determinant of the matrix 2 is {round(det2, 0)}.")

# Book2 calculation
print("\nCalculate matrices in Book2\n")
# set up matrix as a variable
matrix2_1 = np.loadtxt('Book2.csv', delimiter=',', skiprows=1, max_rows=3)
matrix2_2 = np.loadtxt('Book2.csv', delimiter=',', skiprows=5, max_rows=3)

print(f"Matrix 2.1:\n{matrix2_1}")
print(f"\nMatrix 2.2:\n{matrix2_2}")

# check the condition for addition/subtraction
if matrix2_1.shape == matrix2_2.shape:
    sum2 = matrix2_1 + matrix2_2
    print(f"Matrix 2.1 + Matrix 2.2:\n{sum2}")
elif matrix2_1.shape == matrix2_2.shape:
    sub2 = matrix2_1 - matrix2_2
    print(f"Matrix 2.1 - Matrix 2.2:\n{sub2}")
else:
    print("\nThe sizes are invalid for addition/subtraction!\n")

# check the condition for multiplication
# .shape[0] is the number of rows, [1] is the number of columns
if matrix2_1.shape[1] == matrix2_2.shape[0]:
    mul1 = matrix2_1 @ matrix2_2
    print(f"Matrix 2.1 x Matrix 2.2:\n {mul1}")
elif matrix2_2.shape[1] == matrix2_1.shape[0]:
    mul2 = matrix2_2 @ matrix2_1
    print(f"Matrix 2.2 x Matrix 2.1:\n {mul2}")
else:
    print("\nThe sizes are invalid for multiplication!")
# determinant calculation
det2_1 = np.linalg.det(matrix2_1)
print(f"\nThe determinant of the matrix 2.1 is {round(det2_1, 0)}.")
if matrix2_2.shape[0] == matrix2_2.shape[1]:
    det2_2 = np.linalg.det(matrix2_2)
    print(f"\nThe determinant of the matrix 2.2 is {round(det2_2, 0)}.")
else:
    print("\nThe matrix is not a square matrix to calculate determinant!")
