import itertools


def read_matrix():
    rows, cols = [int(element) for element in input().split(', ')]
    matrix = [
        [int(number) for number in input().split(', ')]
        for _ in range(rows)
    ]
    return matrix


def get_squares(matrix):
    squares = []
    for i in range(len(matrix) - 1):
        for j in range(len(matrix[i]) - 1):
            square = [
                [matrix[i][j], matrix[i][j + 1]],
                [matrix[i + 1][j], matrix[i + 1][j + 1]]
            ]
            squares.append(square)
    return squares


def get_sum_of_matrix(matrix):
    return sum(itertools.chain(*matrix))


def get_max_square(squares):
    result = max([sum(square) for square in matrix])
    return result



matrix = read_matrix()
squares = get_squares(matrix)
print(get_max_square(squares))