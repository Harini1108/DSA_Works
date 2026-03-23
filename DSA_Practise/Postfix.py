def evaluate_postfix(expression):
    stack = []

    for token in expression.split():

        if token.isdigit():
            stack.append(int(token))

        else:
            if token == '!':   # unary
                a = stack.pop()
                stack.append(int(not a))
            else:
                b = stack.pop()
                a = stack.pop()

                if token == '+':
                    stack.append(a + b)
                elif token == '-':
                    stack.append(a - b)
                elif token == '*':
                    stack.append(a * b)
                elif token == '/':
                    stack.append(a // b)
                elif token == '^':
                    stack.append(a ** b)

                # Comparison
                elif token == '>':
                    stack.append(int(a > b))
                elif token == '<':
                    stack.append(int(a < b))
                elif token == '>=':
                    stack.append(int(a >= b))
                elif token == '<=':
                    stack.append(int(a <= b))
                elif token == '==':
                    stack.append(int(a == b))
                elif token == '!=':
                    stack.append(int(a != b))

                # Logical
                elif token == '&&':
                    stack.append(int(a and b))
                elif token == '||':
                    stack.append(int(a or b))

    return stack.pop()

expr = "3 5 + 2 > 4 6 < &&"
print("Result:", evaluate_postfix(expr))