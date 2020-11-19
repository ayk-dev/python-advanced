from collections import deque

cups = deque(map(int, input().split()))
bottles = list(map(int, input().split()))

wasted = 0
while len(cups) > 0 and len(bottles) > 0:
    bottle = bottles.pop()
    cup = cups.popleft()
    while cup > 0:
        if cup <= bottle:
            wasted += abs(cup - bottle)
            cup -= bottle
        else:
            cup -= bottle
            if bottles:
                bottle = bottles.pop()
            else:
                break

if len(cups) == 0:
    bottles = ' '.join(map(str, bottles[::-1]))
    print(f'Bottles: {bottles}')
else:
    cups = ' '.join(map(str, cups))
    print(f'Cups: {cups}')

print(f'Wasted litters of water: {wasted}')
