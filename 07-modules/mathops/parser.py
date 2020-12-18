import operator


def parse_expr(expr):
    n1, sign, n2 = expr.split()
    op = {
        '/': operator.truediv,
        '*': operator.mul,
        '+': operator.add,
        '-': operator.sub,
        '*': operator.pow,
    }[sign]
    return op, float(n1), float(n2)