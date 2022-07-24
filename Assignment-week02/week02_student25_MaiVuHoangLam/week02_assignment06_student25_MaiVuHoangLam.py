import math


def foo(a, b, c):
    x = test1(a, b, c)
    y = test2(a, b, c)
    if x > y:
        result = (y, x)
    else:
        result = (x, y)
    return result


# calculate first case
def test1(a, b, c):
    x = (- b + math.sqrt(delta)) / (2 * a)
    return x


# calculate second case
def test2(a, b, c):
    y = (-b - math.sqrt(delta)) / (2 * a)
    return y


a = float(input())
b = float(input())
c = float(input())
delta = b * b - 4 * a * c
if delta == 0:
    result = (test1(a, b, c), )
elif delta < 0:
    result = ()
else:
    result = foo(a, b, c)

print(result)