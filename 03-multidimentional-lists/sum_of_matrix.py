rows, columns = [int(element) for element in input().split(', ')]

matrix = []
sum_of_elements = 0

for _ in range(rows):
    numbers = list(map(int, input().split(', ')))
    matrix.append(numbers)
    sum_of_elements += sum(numbers)

print(sum_of_elements)
print(matrix)
