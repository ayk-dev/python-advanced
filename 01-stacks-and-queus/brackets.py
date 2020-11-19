parenthesis = input()
stack = []

pairs = {
    '{': '}',
    '[': ']',
    '(': ')'
}

open_par = '{[('
close_par = ')]}'

if len(parenthesis) % 2 == 0:
    for p in parenthesis:
        if p in open_par:
            stack.append(p)
        elif p in close_par:
            last = stack.pop()
            if pairs[last] == p:
                is_valid = True
            else:
                is_valid = False
                break
else:
    is_valid = False

if is_valid:
    print('YES')
else:
    print('NO')



