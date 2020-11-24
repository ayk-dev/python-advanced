r, c = [int(x) for x in input().split()]

matrix = [[chr(97 + i) + chr(97 + i + j) + chr(97 + i) for j in range(c)] for i in range(r)]

for row in matrix:
    print(' '.join(row))
