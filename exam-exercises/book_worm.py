def search_matrix(matrix, searched):
    for i in range(len(matrix)):
        row = matrix[i]
        if searched in row:
            pos = [i, row.index(searched)]
    return pos


def check_if_outside_of_field(matrix, y, x):
    if (y < 0 or y >= len(matrix)) or (x < 0 or x >= len(matrix)):
        return True
    else:
        return False


string = input()
n = int(input())
field = [list(input()) for _ in range(n)]

temp_str = list(string)

player = search_matrix(field, 'P')
moves = {
    'up': (-1, 0),
    'down': (1, 0),
    'right': (0, 1),
    'left': (0, -1),
}

m = int(input())
for _ in range(m):
    cmd = input()
    move = moves[cmd]
    new_position = [player[0] + move[0], player[1] + move[1]]

    if check_if_outside_of_field(field, new_position[0], new_position[1]):
        temp_str.pop()
        continue

    field[player[0]][player[1]] = '-'
    player = [new_position[0], new_position[1]]
    if field[player[0]][player[1]] != '-':
        temp_str.append(field[player[0]][player[1]])
        field[player[0]][player[1]] = 'P'

result = ''.join(temp_str)
print(result)
for row in field:
    print(''.join(row))
