def add_value(m, r, c, v):
    m[r][c] += v


def subtract_value(m, r, c, v):
    m[r][c] -= v


rows = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(rows)]

operations = {
    'Add': add_value,
    'Subtract': subtract_value
}

while True:
    line = input()
    if line == 'END':
        break

    command, *others = line.split()
    row, col, value = [int(x) for x in others]

    if not (0 <= row < rows and 0 <= col < rows):
        print('Invalid coordinates')
        continue

    operations[command](matrix, row, col, value)

for line in matrix:
    print(" ".join([str(x) for x in line]))
