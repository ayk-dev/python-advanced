n = int(input())

elements = []
for _ in range(n):
    elements += input().split(' ')

print('\n'.join(set(elements)))