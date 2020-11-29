matrix_info = input().split(', ')
rows = int(matrix_info[0])
columns = int(matrix_info[1])

matrix = []

for _ in range(rows):
    numbers = list(map(int, input().split(' ')))
    matrix.append(numbers)

for j in range(columns):
    sum_of_columns = 0
    sum_of_columns += sum([matrix[i][j] for i in range(rows)])
    print(sum_of_columns)


