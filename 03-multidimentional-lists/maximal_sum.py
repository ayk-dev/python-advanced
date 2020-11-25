import sys

rows, columns = tuple(map(int, input().split()))

matrix = []
for _ in range(rows):
    row = list(map(int, input().split()))
    matrix.append(row)

squares = []
for i in range(rows):
    for j in range(columns):
        if j + 2 < rows and i + 2 < columns:
            square = [
                matrix[j][i], matrix[j][i+1], matrix[j][i+2],
                matrix[j+1][i], matrix[j+1][i+1], matrix[j+1][i+2],
                matrix[j+2][i], matrix[j+2][i+1], matrix[j+2][i+2]
            ]
        squares.append(square)

max_sum = -sys.maxsize
for r in range(len(squares)):
    sum_of_square = sum(squares[r])
    if sum_of_square >= max_sum:
        max_sum = sum_of_square
        max_square = squares[r]


print(f"Sum = {sum(max_square)}")

for i in range(len(max_square)):
    if i > 0 and i % 3 == 0:
        print()
    print(max_square[i], end=' ')