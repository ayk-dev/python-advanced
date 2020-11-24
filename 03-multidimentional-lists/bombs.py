from collections import deque


def explosion(mat, r, c):
    size = len(mat)
    bomb = mat[r][c]
    if bomb > 0:
        if c - 1 >= 0:
            if mat[r][c - 1] > 0:
                mat[r][c - 1] -= bomb
            if r - 1 >= 0:
                if mat[r - 1][c - 1] > 0:
                    mat[r - 1][c - 1] -= bomb
        if r - 1 >= 0:
            if mat[r - 1][c] > 0:
                mat[r - 1][c] -= bomb
            if c + 1 < size:
                if mat[r - 1][c + 1] > 0:
                    mat[r - 1][c + 1] -= bomb
        if c + 1 < size:
            if mat[r][c + 1] > 0:
                mat[r][c + 1] -= bomb
            if r + 1 < size:
                if mat[r + 1][c + 1] > 0:
                    mat[r + 1][c + 1] -= bomb
        if r + 1 < size:
            if mat[r + 1][c] > 0:
                mat[r + 1][c] -= bomb
            if c - 1 >= 0:
                if mat[r + 1][c - 1] > 0:
                    mat[r + 1][c - 1] -= bomb
        mat[r][c] = 0
    return mat


n = int(input())

matrix = []
for _ in range(n):
    line = list(map(int, input().split()))
    matrix.append(line)

bombs = deque(input().split())
while len(bombs) > 0:
    bomb_coordinates = bombs.popleft()
    row, col = tuple(map(int, bomb_coordinates.split(',')))
    explosion(matrix, row, col)

active_cells_count = 0
sum_of_active = 0
for i in range(n):
    current_row = matrix[i]
    for cell in current_row:
        if cell > 0:
            active_cells_count += 1
            sum_of_active += cell

print(f"Alive cells: {active_cells_count}")
print(f"Sum: {sum_of_active}")
for i in range(n):
    row = list(map(str, matrix[i]))
    print(' '.join(row))

