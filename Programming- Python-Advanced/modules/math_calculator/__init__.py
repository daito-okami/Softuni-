from modules.math_calculator.operations import add, subtract, divide, multiply, power


def calculate_expressions(expression):
    x, sign, y = expression.split(' ')
    x = float(x)
    y = float(y)
    if sign == "+":
        result = add(x, y)
    elif sign == "-":
        result = subtract(x, y)
    elif sign == "/":
        result = divide(x, y)
    elif sign == "*":
        result = multiply(x, y)
    elif sign == "^":
        result = power(x, y)
    else:
        raise Exception(f'INVALID SIGN{sign}')
    return result