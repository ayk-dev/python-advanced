rows, cols = [int(element) for element in input().split(', ')]
matrix = [[int(number) for number in input().split(' ')]for _ in range(rows)]

for col in zip(*matrix):
    print(sum(col))