matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for row in matrix:
    for value in row:
        print(value)

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(matrix[i][j])