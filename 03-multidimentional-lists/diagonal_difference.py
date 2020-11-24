def calculate_sum_of_main_diagonal(n, mat):
    primary_diagonal = [mat[i][i] for i in range(n)]
    return sum(primary_diagonal)


def calculate_sum_of_secondary_diagonal(n, mat):
    secondary_diagonal = [mat[i][n-i-1] for i in range(n)]
    return sum(secondary_diagonal)


num = int(input())
matrix = []
for _ in range(num):
    row = [int(x) for x in input().split()]
    matrix.append(row)
sum_of_main_diag = calculate_sum_of_main_diagonal(num, matrix)
sum_of_secondary_diag = calculate_sum_of_secondary_diagonal(num, matrix)

difference = abs(sum_of_main_diag - sum_of_secondary_diag)
print(difference)