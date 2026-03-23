def evaluate_prefix(expression):
    stack = []
    tokens = expression.split()[::-1]

    for token in tokens:

        if token.isdigit():
            stack.append(int(token))

        else:
            if token == '!':
                a = stack.pop()
                stack.append(int(not a))
            else:
                a = stack.pop()
                b = stack.pop()

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
expr = "&& > + 3 5 2 < 4 6"
print("Prefix Result:", evaluate_prefix(expr))