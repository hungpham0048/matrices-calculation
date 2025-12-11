import csv  # import csv file
import numpy as np  # import numpy with the shortcut "np"

# set up matrix as a variable
matrix1 = np.loadtxt('Book1.csv', delimiter=',', skiprows=1,
                     max_rows=3)  # skiprows =  x: bo qua x lines
matrix2 = np.loadtxt('Book1.csv', delimiter=',', skiprows=5,
                     max_rows=3)  # max_rows = x: doc toi da x rows

# print the matrices
print(f"Matrix1\n{matrix1}")  # \n xuong dong
print(f"Matrix2\n{matrix2}")

# set up variables and print sum/product
sum = matrix1 + matrix2
sub = matrix1 - matrix2
product = matrix1 @ matrix2  # "@"" is different with "*""
print(f"\nSum\n{sum}")
print(f"\nSubtraction\n{sub}")
print(f"\nProduct\n{product}")

matrix2_1 = np.loadtxt('Book2.csv', delimiter=',', skiprows=1, max_rows=3)
matrix2_2 = np.loadtxt('Book2.csv', delimiter=',', skiprows=5, max_rows=3)

print(f"Matrix2.1\n{matrix2_1}")
print(f"Matrix2.2\n{matrix2_2}")
