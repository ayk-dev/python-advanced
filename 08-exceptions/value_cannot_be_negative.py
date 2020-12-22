from exceptions import ValueCannotBeNegative

for _ in range(5):
    n = int(input())
    if n < 0:
        raise ValueCannotBeNegative()
