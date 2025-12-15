import csv

print("Calculating Book1\n")
# read book1.csv
matrix1 = []
matrix2 = []
with open('Book1.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)
    for i in range(3):
        row = next(reader)
        int_row = []
        for value in row:
            int_row.append(int(value))
        matrix1.append(int_row)
    next(reader)
    for i in range(3):
        row = next(reader)
        int_row = []
        for value in row:
            int_row.append(int(value))  # convert string to integer
        matrix2.append(int_row)
print("Matrix 1:")
for row in matrix1:
    print(row)
print("\nMatrix 2:")
for row in matrix2:
    print(row)
# addition and subtraction
result1 = [[0, 0, 0],
           [0, 0, 0],
           [0, 0, 0]]
result2 = [[0, 0, 0],
           [0, 0, 0],
           [0, 0, 0]]
for i in range(len(matrix1)):
    for j in range(len(matrix2[0])):
        result1[i][j] = matrix1[i][j] + matrix2[i][j]
        result2[i][j] = matrix1[i][j] - matrix2[i][j]
print("\nSum:")
for row in result1:
    print(row)
for row in result2:
    print(row)

result3 = [[0, 0, 0],
           [0, 0, 0],
           [0, 0, 0]]
for i in range(len(matrix1)):
    for j in range(len(matrix2[0])):
        for k in range(len(matrix2)):  # k la bien so thay doi
            result3[i][j] = result3[i][j] + (matrix1[i][k] * matrix2[k][j])
print("\nProduct: ")
for row in result3:
    print(row)

# calculate book2
print("\nCalculating Book2")
# read Book2.csv
matrix2_1 = []
matrix2_2 = []
with open("Book2.csv", "r") as file2:
    reader2 = csv.reader(file2)
    next(reader2)
    for i in range(3):
        row2 = next(reader2)
        int_row1 = []
        for value in row2:
            int_row1.append(int(value))
        matrix2_1.append(int_row1)
    next(reader2)
    for i in range(3):
        row2 = next(reader2)
        int_row1 = []
        for value in row2:
            int_row1.append(int(value))
        matrix2_2.append(int_row1)
print("\nMatrix 2.1: ")
for row in matrix2_1:
    print(row)
print("\nMatrix 2.2: ")
for row in matrix2_2:
    print(row)
# sum and sub
sum1 = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]]
sub1 = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]]
if len(matrix2_1) == len(matrix2_2[0]):
    for i in range(len(matrix2_1)):
        for j in range(len(matrix2_2[0])):
            sum1[i][j] = matrix2_1[i][j] + matrix2_2[i][j]
            sub1[i][j] = matrix2_1[i][j] - matrix2_2[i][j]
    print("\nSum: ")
    for row in sum1:
        print(row)
    print("\nSubtraction: ")
    for row in sub1:
        print(row)
else:
    print("\nThe sizes of 2 matrices are invalid for addition/subtraction!\n")
# product
product = [[0, 0, 0, 0],
           [0, 0, 0, 0],
           [0, 0, 0, 0]]
if len(matrix2_1[0]) == len(matrix2_1):
    for i in range(len(matrix2_1)):
        for j in range(len(matrix2_2[0])):
            for k in range(len(matrix2_2)):
                product[i][j] = product[i][j] + \
                    (matrix2_1[i][k] * matrix2_2[k][j])
    print("\nProduct: ")
    for row in product:
        print(row)
else:
    print("The sizes of 2 matrices are invalid for multiplication!")
