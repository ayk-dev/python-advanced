import itertools

numbers = input().split(', ')
n = len(numbers)

permutations = set(itertools.permutations(['-'] * n + ['+'] * n, n))

for perm in permutations:
    expr = ''.join(itertools.chain(*zip(perm, numbers)))
    print(f"{expr}={eval(expr)}")
