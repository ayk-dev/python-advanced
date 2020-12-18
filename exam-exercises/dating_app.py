from collections import deque


def special_case(seq):
    current = seq[0]
    seq.popleft()
    if len(seq) > 0:
        current = seq[0]
    while len(seq) > 0 or current % 25 != 0:
        if current % 25 == 0:
            seq.popleft()
        if len(seq) > 0:
            current = seq[0]
    return current


males = deque([int(x) for x in reversed(input().split()) if int(x) > 0])
females = deque([int(x) for x in input().split() if int(x) > 0])

matches = 0
while len(males) > 0 and len(females) > 0:
    current_f = females[0]
    if current_f % 25 == 0:
        current_f = special_case(females)
        if len(females) == 0:
            break
    current_m = males[0]
    if current_m % 25 == 0:
        current_m = special_case(males)
        if len(males) == 0:
            break

    if current_f == current_m:
        matches += 1
        females.popleft()
        males.popleft()
    else:
        females.popleft()
        males[0] -= 2
        if males[0] <= 0:
            males.popleft()

print(f'Matches: {matches}')
if males:
    print(f'Males left: {", ".join(list(map(str, males)))}')
else:
    print(f'Males left: none')
if females:
    print(f'Females left: {", ".join(list(map(str, females)))}')
else:
    print('Females left: none')
