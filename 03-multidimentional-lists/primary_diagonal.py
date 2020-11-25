def calculate_sum_of_main_diagonal(n):
    matrix = []
    for _ in range(n):
        row = [int(x) for x in input().split()]
        matrix.append(row)
    primary_diagonal = [matrix[i][i] for i in range(n)]
    return sum(primary_diagonal)


num = int(input())
sum_of_diagonal = calculate_sum_of_main_diagonal(num)
print(sum_of_diagonal)
