import math

FUNCTION = lambda x: x * x * x - 10 - math.sqrt(x - 2)
EPSILON = 0.000001


def half_divide_method(a, b, f):
    iterations = 0
    x = (a + b) / 2
    while math.fabs(f(x)) >= EPSILON:
        iterations += 1
        x = (a + b) / 2
        a, b = (a, x) if f(a) * f(x) < 0 else (x, b)
    result = (a + b) / 2
    return (a + b) / 2, iterations


if __name__ == '__main__':
    a = float(input("Enter start point:"))
    b = float(input("Enter end point:"))
    try:
        result, iterations = half_divide_method(a, b, FUNCTION)
    except ValueError:
        result, iterations = None, None
        print("Function are not defined on this space")
    print(f"Root: {result}\nIterations: {iterations}")
