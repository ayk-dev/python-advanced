integers_stack = list(map(int, input().split()))

reversed_stack = []
while len(integers_stack) > 0:
    num = integers_stack.pop()
    reversed_stack.append(num)


print(' '.join(list(map(str, reversed_stack))))
