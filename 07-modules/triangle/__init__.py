def print_triangle(size):

    for i in range(1, size + 1):
        print(*[j for j in range(1, i + 1)])

    for i in range(size-1, 0, -1):
        print(*[j for j in range(1, i+1)])