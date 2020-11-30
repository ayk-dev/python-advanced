even_matrix = [
    [int(num) for num in input().split(', ') if int(num) % 2 == 0]
    for _ in range(int(input()))
]

print(even_matrix)