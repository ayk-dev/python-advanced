set_lengths = input().split(' ')
n = int(set_lengths[0])
m = int(set_lengths[1])

first_set = set([int(input()) for _ in range(n)])
second_set = set([int(input()) for _ in range(m)])

common_elements = first_set.intersection(second_set)
print('\n'.join(map(str, common_elements)))