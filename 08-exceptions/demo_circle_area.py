import math
import exceptions


def find_circle_area(radius):
    if type(radius) not in [int, float]:
        raise exceptions.InvalidInputError(f'Radius cannot be of type {type(radius)}')
    return math.pi * (radius ** 2)


print(find_circle_area(2))
print(find_circle_area(True))
