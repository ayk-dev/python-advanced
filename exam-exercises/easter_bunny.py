def go_up(m, b):
    collected = 0
    positions = []
    row = b[0]
    col = b[1]
    while row > 0:
        row -= 1
        field = m[row][col]
        if field == 'X':
            break
        else:
            collected += int(field)
            positions.append([row, col])
    return [positions, collected]


def go_down(m, b):
    collected = 0
    positions = []
    size = len(m)
    row = b[0]
    col = b[1]
    while row < size - 1:
        row += 1
        field = m[row][col]
        if field == 'X':
            break
        else:
            collected += int(field)
            positions.append([row, col])
    return [positions, collected]


def go_right(m, b):
    collected = 0
    positions = []
    size = len(m)
    row = b[0]
    col = b[1]
    while col < size - 1:
        col += 1
        field = m[row][col]
        if field == 'X':
            break
        else:
            collected += int(field)
            positions.append([row, col])
    return [positions, collected]


def go_left(m, b):
    collected = 0
    positions = []
    row = b[0]
    col = b[1]
    while col > 0:
        col -= 1
        field = m[row][col]
        if field == 'X':
            break
        else:
            collected += int(field)
            positions.append([row, col])
    return [positions, collected]


n = int(input())
matrix = []
for i in range(n):
    field_row = input().split()
    if 'B' in field_row:
        bunny = [i, field_row.index('B')]
    matrix.append(field_row)

collectable_eggs = {
    'up': go_up(matrix, bunny),
    'down': go_down(matrix, bunny),
    'right': go_right(matrix, bunny),
    'left': go_left(matrix, bunny),
}

sorted_collectable_eggs = dict(sorted(collectable_eggs.items(), key=lambda x: -x[1][1]))

for direction, values in sorted_collectable_eggs.items():
    print(direction)
    for item in values[0]:
        print(item)
    print(values[1])
    break