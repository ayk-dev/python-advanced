from mathops import parser, executer

expr = input()
result = executer.exec(*parser.parse_expr(expr))
print(result)


