start_num = int(input())
end_num = int(input())

filtered_numbers = [
    x
    for x in range(start_num, end_num + 1)
    if any([x % y == 0 for y in range(2, 11)])
]

print(filtered_numbers)