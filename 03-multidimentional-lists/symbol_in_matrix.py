n = int(input())
# square matrix rows * rows

matrix = []
for _ in range(n):
    row = list(input())
    matrix.append(row)

searched_symbol = input()


for i in range(n):
    is_found = False
    for j in range(n):
        if matrix[i][j] == searched_symbol:
            print(f'({i}, {j})')
            is_found = True
            break
    if is_found:
        break
else:
    print(f'{searched_symbol} does not occur in the matrix')