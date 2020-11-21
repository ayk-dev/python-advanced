import sys
import copy


def push(stack, elem):
    stack.append(elem)
    return stack


def delete(stack):
    if len(stack) > 0:
        stack.pop()
    return stack


def get_max_element(stack):
    max_element = -sys.maxsize
    while len(stack) > 0:
        elem = stack.pop()
        if elem > max_element:
            max_element = elem
    return max_element


def get_min_element(stack):
    min_element = sys.maxsize
    while len(stack) > 0:
        elem = stack.pop()
        if elem < min_element:
            min_element = elem
    return min_element


sequence = []

n = int(input())
for _ in range(n):
    input_line = input().split(' ')
    query = int(input_line[0])

    if query == 1:
        element = int(input_line[1])
        push(sequence, element)

    elif query == 2:
        delete(sequence)

    elif query == 3:
        if len(sequence) > 0:
            numbers = copy.deepcopy(sequence)
            print(get_max_element(numbers))

    elif query == 4:
        if len(sequence) > 0:
            numbers = copy.deepcopy(sequence)
            print(get_min_element(numbers))


while len(sequence) > 0:
    result = sequence.pop()
    if len(sequence) == 0:
        print(result)
    else:
        print(result, end=', ')