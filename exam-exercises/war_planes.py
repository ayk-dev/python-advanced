n = int(input())

battlefield = []
targets_count = 0
for i in range(n):
    line = input().split()
    if 'p' in line:
        plane = [i, line.index('p')]
    if 't' in line:
        count = line.count('t')
        targets_count += count
    battlefield.append(line)

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'right': (0, 1),
    'left': (0, -1),
}

is_successful = False
targets_destroyed = 0
m = int(input())
for _ in range(m):
    command, direction, count = input().split()
    steps = int(count)
    dir = directions[direction]
    target_pos = [plane[0] + (dir[0] * steps), plane[1] + (dir[1] * steps)]
    if 0 <= target_pos[0] < n and 0 <= target_pos[1] < n:

        if command == 'move':
            if battlefield[target_pos[0]][target_pos[1]] == '.':
                battlefield[plane[0]][plane[1]] = '.'
                plane = [target_pos[0], target_pos[1]]
                battlefield[plane[0]][plane[1]] = 'p'

        elif command == 'shoot':
            if battlefield[target_pos[0]][target_pos[1]] == 't':
                targets_count -= 1
                targets_destroyed += 1
            battlefield[target_pos[0]][target_pos[1]] = 'x'
            if targets_count == 0:
                is_successful = True
                break

if is_successful:
    print(f'Mission accomplished! All {targets_destroyed} targets destroyed.')
else:
    print(f'Mission failed! {targets_count} targets left.')

for row in battlefield:
    print(' '.join(row))

