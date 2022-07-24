import math


def foo(a, b, c):
    delta = b**2 - 4 * a * c
    if delta < 0:
        print(tuple([]))
    else:
        if delta == 0:
            print(tuple([-b/(2*a)]))
        else:
            x1 = (-b + math.sqrt(delta)) / (2 * a)
            x2 = (-b - math.sqrt(delta)) / (2 * a)
            print(tuple([x2, x1]))


if __name__ == '__main__':
    foo(1, 1, -2)
    foo(1, 2, 1)
    foo(1, 0, 1)
