from math import log

number = int(input())
base = input()

if base == 'natural':
    result = log(number)
else:
    result = log(number, int(base))

print(f'{result:.2f}')