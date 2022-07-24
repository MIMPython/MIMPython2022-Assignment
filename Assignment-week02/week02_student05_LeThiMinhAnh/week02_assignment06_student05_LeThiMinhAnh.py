from math import sqrt


def foo(a, b, c):
    delta = b**2 - 4*a*c
    if delta < 0:
        result = ()
    elif delta == 0:
        result = (-b/(2*a),)
    else:
        result = tuple(
            sorted(((-b+sqrt(delta))/(2*a), (-b-sqrt(delta))/(2*a))))
    print(result)


foo(1, 2, 1)
foo(2, 8, -10)
foo(1, 0, 1)
