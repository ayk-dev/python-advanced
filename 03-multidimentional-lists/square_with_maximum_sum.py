import sys

matrix_info = input().split(', ')
rows = int(matrix_info[0])
columns = int(matrix_info[1])

matrix = []

for _ in range(rows):
    numbers = list(map(int, input().split(', ')))
    matrix.append(numbers)

squares = []

for i in range(rows - 1):
    for j in range(columns - 1):
        square = [matrix[i][j], matrix[i][j+1], matrix[i+1][j], matrix[i+1][j+1]]
        squares.append(square)

max_sum = -sys.maxsize
for r in range(len(squares)):
    sum_of_square = sum(squares[r])
    if sum_of_square >= max_sum:
        max_sum = sum_of_square
        max_square = squares[r]

print(max_square[0], max_square[1])
print(max_square[2], max_square[3])
print(max_sum)
