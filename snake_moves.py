from collections import deque

rows, cols = tuple(map(int, input().split()))
matrix = []
for row in range(rows):
    matrix.append([])
    for col in range(cols):
        matrix[row].append('')

snake = deque(input())

for i in range(rows):
    for j in range(cols):
        current = snake.popleft()
        matrix[i][j] = current
        snake.append(current)

for i in range(rows):
    if i % 2 != 0:
        print(''.join(matrix[i][::-1]))
    else:
        print(''.join(matrix[i]))
