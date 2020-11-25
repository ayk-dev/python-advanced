def check_is_command_valid(r, c, line):
    tokens = line.split()
    if tokens[0] == 'swap':
        is_valid = True
    else:
        is_valid = False
    coordinates = tokens[1:]
    if len(coordinates) == 4:
        for num in coordinates:
            if not num.isdigit():
                is_valid = False
                break
        else:
            coordinates = tuple(map(int, coordinates))
            r1, c1, r2, c2 = coordinates
            if 0 <= r1 < r and 0 <= r2 < r and 0 <= c1 < c and 0 <= c2 < c:
                is_valid = True
            else:
                is_valid = False
    else:
        is_valid = False
    if is_valid:
        return coordinates
    else:
        return None


rows, columns = tuple(map(int, input().split(' ')))

matrix = []
for _ in range(rows):
    characters = input().split(' ')
    matrix.append(characters)

while True:
    line = input()
    if line == 'END':
        break

    if not check_is_command_valid(rows, columns, line):
        print('Invalid input!')
        continue

    row1, col1, row2, col2 = check_is_command_valid(rows, columns, line)
    matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]

    for i in range(rows):
        row = ' '.join(matrix[i])
        print(row, end='\n')


