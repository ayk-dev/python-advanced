from collections import deque
from functools import reduce

expression = deque(input().split())

numbers = []
operations = {
    '*': lambda x, y: x * y,
    '/': lambda x, y: x / y,
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
}

temp_result = 0
while len(expression) > 0:
    element = expression.popleft()
    if element.isdigit() or (len(element) >= 2 and element.startswith('-')):
        numbers.append(int(element))
    else:
        op = element
        temp_result = reduce(operations[op], numbers)
        numbers.clear()
        numbers.append(int(temp_result))

evaluated = int(temp_result)
print(evaluated)

