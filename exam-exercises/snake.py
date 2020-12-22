n = int(input())

matrix = []
lair = []
for i in range(n):
    line = list(input())
    if 'S' in line:
        snake = [i, line.index('S')]
    if 'B' in line:
        hole = [i, line.index('B')]
        lair.append(hole)
    matrix.append(line)

moves = {
    'up': (-1, 0),
    'down': (1, 0),
    'right': (0, 1),
    'left': (0, -1),
}
food_eaten = 0
food_required = 10

while True:
    command = input()
    move = moves[command]
    matrix[snake[0]][snake[1]] = '.'
    new_snake_pos = [snake[0] + move[0], snake[1] + move[1]]

    if (new_snake_pos[0] < 0 or new_snake_pos[0] >= n) or (new_snake_pos[1] < 0 or new_snake_pos[1] >= n):
        lost = True
        print('Game over!')
        break

    if matrix[new_snake_pos[0]][new_snake_pos[1]] == '*':
        food_eaten += 1
        if food_eaten == food_required:
            snake = [new_snake_pos[0], new_snake_pos[1]]
            matrix[snake[0]][snake[1]] = 'S'
            won = True
            print('You won! You fed the snake.')
            break

    elif matrix[new_snake_pos[0]][new_snake_pos[1]] == 'B':
        matrix[new_snake_pos[0]][new_snake_pos[1]] = '.'
        hole_in = [new_snake_pos[0], new_snake_pos[1]]
        lair.remove(hole_in)
        new_snake_pos = lair[0]

    snake = [new_snake_pos[0], new_snake_pos[1]]
    matrix[snake[0]][snake[1]] = 'S'

print(f'Food eaten: {food_eaten}')
for row in matrix:
    print(''.join(row))
