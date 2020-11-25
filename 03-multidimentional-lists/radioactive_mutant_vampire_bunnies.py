from collections import deque


def find_bunnies(matrix):
    bunnies = []
    for x, row in enumerate(matrix):
        for y, value in enumerate(row):
            if value == 'B':
                bunnies.append((x, y))
    return bunnies


rows, cols = tuple(map(int, input().split()))

lair = []
for i in range(rows):
    line = list(input())
    lair.append(line)
    if 'P' in line:
        player_position = [i, line.index('P')]

moves = deque(input())
game_over = False

bunnies_spreading = [
    (0, 1),
    (0, -1),
    (1, 0),
    (-1, 0)
]

while len(moves) > 0:
    lair[player_position[0]][player_position[1]] = '.'
    next_player_position = []
    move = moves.popleft()
    if move == 'R':
        next_player_position = [player_position[0], player_position[1] + 1]

    elif move == 'L':
        next_player_position = [player_position[0], player_position[1] - 1]

    elif move == 'U':
        next_player_position = [player_position[0] - 1, player_position[1]]

    elif move == 'D':
        next_player_position = [player_position[0] + 1, player_position[1]]

    if lair[next_player_position[0]][next_player_position[1]] == 'B':
        game_over = True
        message = f'dead: {next_player_position[0]} {next_player_position[1]}'

    if (next_player_position[0] < 0 or next_player_position[0] == rows) or \
            (next_player_position[1] < 0 or next_player_position[1] == cols):
        game_over = True
        message = f'won: {player_position[0]} {player_position[1]}'

    for bunny in find_bunnies(lair):
        for delta in bunnies_spreading:
            new_bunny_position = [bunny[0] + delta[0], bunny[1] + delta[1]]
            if 0 <= new_bunny_position[0] < rows and 0 <= new_bunny_position[1] < cols:
                at_position = lair[new_bunny_position[0]][new_bunny_position[1]]
                if at_position == 'P':
                    game_over = True
                    message = f'dead: {next_player_position[0]} {next_player_position[1]}'
                lair[new_bunny_position[0]][new_bunny_position[1]] = 'B'
    if game_over:
        break

    lair[next_player_position[0]][next_player_position[1]] = 'P'
    player_position = next_player_position

for row in lair:
    print(''.join(row))
print(message)








