def subexpression_printer(expr):
    stack_indexes = []

    for index, char in enumerate(expr):
        if char == '(':
            stack_indexes.append(index)
        elif char == ')':
            end_index = index
            start_index = stack_indexes.pop()
            subexpr = expr[start_index:end_index + 1]
            print(subexpr)


subexpression_printer(input())