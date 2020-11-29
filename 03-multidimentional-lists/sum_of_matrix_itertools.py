import itertools

rows, cols = [int(element) for element in input().split(', ')]
matrix = [
    [int(number) for number in input().split(', ')]
    for _ in range(rows)
]
sum_of_matrix = sum(itertools.chain(*matrix))

print(sum_of_matrix)
print(matrix)