# from functools import reduce
#
#
# def multiply(*args):
#     result = reduce(lambda x, y: x * y, args)
#     return result


def multiply(*args):
    numbers = list(args)
    result = 1
    while len(numbers) > 0:
        result *= numbers.pop()
    return result


print(multiply(1, 4, 5))


print(multiply(4, 5, 6, 1, 3))
print(multiply(2, 0, 1000, 5000))