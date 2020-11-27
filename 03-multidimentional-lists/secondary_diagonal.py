def calculate_sum_of_secondary_diagonal(n):
    matrix = []
    for _ in range(n):
        row = [int(x) for x in input().split()]
        matrix.append(row)
    secondary_diagonal = [matrix[i][n-i-1] for i in range(n)]
    return sum(secondary_diagonal)


num = int(input())
sum_of_diagonal = calculate_sum_of_secondary_diagonal(num)
print(sum_of_diagonal)