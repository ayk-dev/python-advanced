numbers = [int(x) for x in input().split()]

min_value = min(numbers)
max_value = max(numbers)
total_sum = sum(numbers)

print(f'The minimum number is {min_value}')
print(f"The maximum number is {max_value}")
print(f"The sum number is: {total_sum}")