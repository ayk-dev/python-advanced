
# file = open('numbers.txt', 'r')
#
# numbers = []
# for line in file:
#     numbers.append(int(line.strip()))
#
# print(sum(numbers))

print(sum(int(line.strip()) for line in open('numbers.txt')))

