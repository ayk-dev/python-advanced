from collections import deque


def check_is_task_done(pr):
    if ('Doll' in pr.keys() and 'Wooden train' in pr.keys()) or ('Teddy bear' in pr.keys() and 'Bicycle' in pr.keys()):
        return True
    else:
        return False


materials = deque([int(x) for x in input().split()])
magic_values = deque([int(x) for x in input().split()])

presents = {
    150: 'Doll',
    250: 'Wooden train',
    300: 'Teddy bear',
    400: 'Bicycle',
}

crafted_presents = {}
while materials and magic_values:
    product = materials[-1] * magic_values[0]
    if product in presents.keys():
        materials.pop()
        magic_values.popleft()
        present = presents[product]
        if present not in crafted_presents:
            crafted_presents[present] = 1
        else:
            crafted_presents[present] += 1

    elif product < 0:
        result = materials[-1] + magic_values[0]
        materials.pop()
        magic_values.popleft()
        materials.append(result)

    elif product > 0:
        magic_values.popleft()
        materials[-1] += 15

    elif product == 0:
        if materials[-1] == 0:
            materials.pop()
        if magic_values[0] == 0:
            magic_values.popleft()

if check_is_task_done(crafted_presents):
    print(f'The presents are crafted! Merry Christmas!')
else:
    print(f'No presents this Christmas!')

if materials:
    print(f'Materials left: {", ".join(list(map(str, reversed(materials))))}')

if magic_values:
    print(f'Magic left: {", ".join(list(map(str, magic_values)))}')

sorted_presents = dict(sorted(crafted_presents.items(), key=lambda x: x[0]))
for gift, amount in sorted_presents.items():
    print(f'{gift}: {amount}')

