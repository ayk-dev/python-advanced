def even_odd(*args):
    cmd = args[-1]
    numbers = [int(x) for x in args[:-1]]
    commands = {
        'odd': [x for x in numbers if x % 2 != 0],
        'even': [x for x in numbers if x % 2 == 0]
    }
    return commands[cmd]


print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))