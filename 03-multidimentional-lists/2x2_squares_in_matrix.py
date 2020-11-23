rows, columns = tuple(map(int, input().split(' ')))

matrix = []
for _ in range(rows):
    characters = input().split(' ')
    matrix.append(characters)

counter = 0
for j in range(rows - 1):
    for i in range(columns - 1):
        if j + 1 < rows and i + 1 < columns:
            square = [matrix[j][i], matrix[j][i+1], matrix[j+1][i], matrix[j+1][i+1]]
            if len(set(square)) == 1:
                counter += 1

# print(squares)


print(counter)