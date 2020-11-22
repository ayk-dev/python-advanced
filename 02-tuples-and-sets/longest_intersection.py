n = int(input())

intersections = []
for _ in range(n):
    first_pair, second_pair = input().split('-')

    x, y = first_pair.split(',')
    first_interval = set([num for num in range(int(x), int(y) + 1)])

    m, z = second_pair.split(',')
    second_interval = set([num for num in range(int(m), int(z) + 1)])

    intrs = first_interval.intersection(second_interval)
    intersections.append(intrs)

intersections = sorted(intersections, key=lambda x: -len(x))
longest_intersection = ', '.join(map(str, intersections[0]))
length = len(intersections[0])
print(f'Longest intersection is [{longest_intersection}] with length {length}')
