def santa_becomes_generous(neighborhood, santa, presents, good_kids, moves):
    i = santa[0]
    j = santa[1]
    for move in moves.values():
        x, y = i + move[0], j + move[1]
        if neighborhood[x][y] != '-':
            presents -= 1
            if neighborhood[x][y] == 'V':
                good_kids -= 1
            neighborhood[x][y] = '-'

    return presents, good_kids


m = int(input())  # the count of presents Santa has
n = int(input())  # size of the neighborhood with a square shape

neighborhood = []
good_kids_count = 0
for i in range(n):
    line = input().split()
    if 'S' in line:
        santa = [i, line.index('S')]
    if 'V' in line:
        count = line.count('V')
        good_kids_count += count
    neighborhood.append(line)

received = good_kids_count

moves = {
    'up': (-1, 0),
    'down': (1, 0),
    'right': (0, 1),
    'left': (0, -1),
}

while m > 0 and good_kids_count > 0:
    command = input()
    if command == 'Christmas morning':
        break

    new_position = [santa[0] + moves[command][0], santa[1] + moves[command][1]]

    neighborhood[santa[0]][santa[1]] = '-'
    santa = [new_position[0], new_position[1]]

    if neighborhood[new_position[0]][new_position[1]] == 'V':
        neighborhood[new_position[0]][new_position[1]] = '-'
        m -= 1
        good_kids_count -= 1
    elif neighborhood[new_position[0]][new_position[1]] == 'C':
        m, good_kids_count = santa_becomes_generous(neighborhood, santa, m, good_kids_count, moves)

    neighborhood[new_position[0]][new_position[1]] = 'S'


if m == 0 and good_kids_count > 0:
    print(f'Santa ran out of presents!')

for row in neighborhood:
    print(' '.join(row))

if good_kids_count == 0:
    print(f'Good job, Santa! {received} happy nice kid/s.')
else:
    print(f'No presents for {good_kids_count} nice kid/s.')


