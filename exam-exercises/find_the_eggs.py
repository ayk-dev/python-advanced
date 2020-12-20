from collections import deque


def find_strongest_eggs(sequence, n):
    queue = deque(sequence)
    sublists = [[] for _ in range(n)]
    while len(queue) > 0:
        for i in range(n):
            if queue:
                el = queue.popleft()
                sublists[i].append(el)

    strongest_eggs = []
    for i in range(len(sublists)):
        is_stronger = False
        j = len(sublists[i]) // 2
        middle_egg = sublists[i][j]
        if middle_egg > sublists[i][j - 1] and middle_egg > sublists[i][j + 1]:
            for k in range(1, j + 1):
                if sublists[i][j + k] > sublists[i][j - k]:
                    is_stronger = True
        if is_stronger:
            strongest_eggs.append(middle_egg)

    return strongest_eggs


test = ([-1, 7, 3, 15, 2, 12], 2)
print(find_strongest_eggs(*test))

test = ([-1, 0, 2, 5, 2, 3], 2)
print(find_strongest_eggs(*test))

test = ([51, 21, 83, 52, 55], 1)
print(find_strongest_eggs(*test))

test = ([1, 7, 2, 8, 6, 20, 4, 9, 5, 11], 2)
print(find_strongest_eggs(*test))