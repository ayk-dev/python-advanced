numbers_input = tuple(map(float, input().split()))

numbers = {}
for num in numbers_input:
    if num not in numbers:
        numbers[num] = 0
    numbers[num] += 1

for number, times in numbers.items():
    print(f'{number} - {times} times')

