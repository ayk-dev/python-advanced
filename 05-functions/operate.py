from functools import reduce


def operate(op, *args):
    ops = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x / y
    }
    result = reduce(ops[op], args)
    return result

# math.prod

print(operate("+", 10, 10))
print(operate("*", 3, 4))
print(operate("*", 20, 11, -5, -7, 3, 4))