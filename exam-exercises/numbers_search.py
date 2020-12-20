def numbers_searching(*args):
    numbers = list(sorted(args))
    dubl = {}
    dubl_list = []
    for num in args:
        if num in dubl:
            dubl[num] += 1
            dubl_list.append(num)
        else:
            dubl[num] = 1
    dubl_list = list(sorted(set(dubl_list)))
    start = numbers[0]
    end = numbers[-1]
    missing_numbers = [n for n in range(start, end) if n not in numbers]
    return [min(missing_numbers), dubl_list]


print(numbers_searching(1, 2, 4, 2, 5, 4))
print(numbers_searching(5, 5, 9, 10, 7, 8, 7, 9))
print(numbers_searching(50, 50, 47, 47, 48, 45, 49, 44, 47, 45, 44, 44, 48, 44, 48))

