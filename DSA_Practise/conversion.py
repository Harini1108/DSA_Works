def precedence(op):
    if op == '||':
        return 1
    elif op == '&&':
        return 2
    elif op in ['==', '!=']:
        return 3
    elif op in ['>', '<', '>=', '<=']:
        return 4
    elif op in ['+', '-']:
        return 5
    elif op in ['*', '/']:
        return 6
    elif op == '^':
        return 7
    elif op == '!':   # unary operator
        return 8
    return 0


def infix_to_postfix(expression):
    stack = []
    output = []
    
    tokens = expression.split()

    for char in tokens:

        # Operand
        if char.isalnum():
            output.append(char)

        # (
        elif char == '(':
            stack.append(char)

        # )
        elif char == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()

        # Operator
        else:
            while (stack and stack[-1] != '(' and
                   precedence(stack[-1]) >= precedence(char)):
                output.append(stack.pop())
            stack.append(char)

    # Remaining operators
    while stack:
        output.append(stack.pop())

    return " ".join(output)


expression = "3 + 5 > 2 && 4 < 6"
postfix = infix_to_postfix(expression)

print("Postfix:", postfix)
