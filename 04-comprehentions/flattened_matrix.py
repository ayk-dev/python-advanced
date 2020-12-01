n = int(input())
matrix = [
    [int(num) for num in input().split(', ')]
    for _ in range(n)
]

flattened_matrix = [num for row in matrix for num in row]
print(flattened_matrix)