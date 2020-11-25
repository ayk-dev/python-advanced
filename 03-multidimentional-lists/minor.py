from collections import deque

size = int(input())
commands = deque(input().split())

field = []
total_coals_count = 0
for row in range(size):
    field_row = input().split()
    field.append(field_row)
    if 's' in field_row:
        col = field_row.index('s')
        start = [row, col]
    if 'c' in field_row:
        total_coals_count += field_row.count('c')

coals_found = 0
game_over = False
current = start
while len(commands) > 0:
    next_position = []
    cmd = commands.popleft()
    if cmd == 'up':
        next_position = [current[0] - 1, current[1]]

    elif cmd == 'right':
        next_position = [current[0], current[1] + 1]

    elif cmd == 'left':
        next_position = [current[0], current[1] - 1]

    elif cmd == 'down':
        next_position = [current[0] + 1, current[1]]

    if 0 <= next_position[0] < size and 0 <= next_position[1] < size:
        r = next_position[0]
        c = next_position[1]
        if field[r][c] == '*':
            field[current[0]][current[1]] = '*'
            field[r][c] = 's'
            current = next_position

        elif field[r][c] == 'e':
            print(f'Game over! ({r}, {c})')
            game_over = True
            break

        elif field[r][c] == 'c':
            coals_found += 1
            if coals_found == total_coals_count:
                print(f'You collected all coals! ({r}, {c})')
                game_over = True
                break

            field[current[0]][current[1]] = '*'
            field[r][c] = 's'
            current = next_position

if not game_over:
    print(f'{total_coals_count - coals_found} coals left. ({r}, {c})')
