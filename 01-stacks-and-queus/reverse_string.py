def reverse_string(s):
    result = []
    while len(s) > 0:
        result.append(s.pop())
    return result


string = list(input()) # this is stack
reversed_string = reverse_string(string)
print(''.join(reversed_string))