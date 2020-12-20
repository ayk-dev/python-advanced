def modify_matrix(bombs, field):
    for b in bombs:
        row = int(b[0])
        col = int(b[1])
        if col - 1 >= 0:
            if field[row][col - 1] != '*':
                field[row][col - 1] += 1
            if row - 1 >= 0:
                if field[row - 1][col - 1] != '*':
                    field[row - 1][col - 1] += 1
            if row + 1 < len(field):
                if field[row + 1][col - 1] != '*':
                    field[row + 1][col - 1] += 1
        if row - 1 >= 0:
            if field[row - 1][col] != '*':
                field[row - 1][col] += 1
            if col + 1 < len(field):
                if field[row - 1][col + 1] != '*':
                    field[row - 1][col + 1] += 1
        if col + 1 < len(field):
            if field[row][col + 1] != '*':
                field[row][col + 1] += 1
            if row + 1 < len(field):
                if field[row + 1][col + 1] != '*':
                    field[row + 1][col + 1] += 1
        if row + 1 < len(field):
            if field[row + 1][col] != '*':
                field[row + 1][col] += 1
    return field


n = int(input())
bombs_count = int(input())

field = [[0] * n for _ in range(n)]

bombs = []
for _ in range(bombs_count):
    bomb = input().split(', ')
    r = int(bomb[0].lstrip('('))
    c = int(bomb[1].rstrip(')'))
    bombs.append([r, c])
    field[r][c] = '*'

mined_field = modify_matrix(bombs, field)
for row in mined_field:
    print(' '.join(map(str, row)))
