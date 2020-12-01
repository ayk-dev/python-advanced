numbers_lists = [num_list.split() for num_list in input().split('|')]

new_list = []
while len(numbers_lists) > 0:
    new_list += numbers_lists.pop()

print(' '.join([str(num) for num in new_list]))
