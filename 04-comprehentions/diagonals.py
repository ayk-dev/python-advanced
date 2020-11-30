n = int(input())
matrix = [[int(x) for x in input().split(', ')]for _ in range(n)]

first_diagonal = ", ".join([str(num) for num in [matrix[i][i] for i in range(n)]])
second_diagonal = ", ".join([str(num) for num in [matrix[i][n-i-1] for i in range(n)]])

print(f'First diagonal: {first_diagonal}. Sum: {sum([matrix[i][i] for i in range(n)])}')
print(f'Second diagonal: {second_diagonal}. Sum: {sum([matrix[i][n-i-1] for i in range(n)])}')