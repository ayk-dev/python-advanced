from collections import deque

effects = deque([int(x) for x in input().split(', ')])
casings = deque([int(x) for x in reversed(input().split(', '))])

bombs = {
    40: 'Datura Bombs',
    60: 'Cherry Bombs',
    120: 'Smoke Decoy Bombs',
}

created_bombs = {
    'Cherry Bombs': 0,
    'Datura Bombs': 0,
    'Smoke Decoy Bombs': 0,
}


def is_bomb_pouch_full(pouch):
    return all([value >= 3 for value in pouch.values()])


while effects and casings:
    sum = effects[0] + casings[0]
    if sum in bombs.keys():
        effects.popleft()
        casings.popleft()
        bomb = bombs[sum]
        created_bombs[bomb] += 1

        if is_bomb_pouch_full(created_bombs):
            break
    else:
        casings[0] -= 5

if is_bomb_pouch_full(created_bombs):
    print('Bene! You have successfully filled the bomb pouch!')
else:
    print("You don't have enough materials to fill the bomb pouch.")

if effects:
    print(f'Bomb Effects: {", ".join(list(map(str, effects)))}')
else:
    print('Bomb Effects: empty')

if casings:
    print(f'Bomb Casings: {", ".join(list(map(str, casings)))}')
else:
    print('Bomb Casings: empty')

for b, count in created_bombs.items():
    print(f'{b}: {count}')
