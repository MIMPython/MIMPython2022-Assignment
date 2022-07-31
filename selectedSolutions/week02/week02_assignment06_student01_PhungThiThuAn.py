from math import sqrt

def solve_quadratic(a, b, c):
    delta = b**2 - 4*a*c
    if delta >= 0:
        x1 = (-b - sqrt(delta))/2/a
        x2 = (-b + sqrt(delta))/2/a
        if x1 < x2:
            return (x1, x2)
        elif x1 > x2:
            return (x2, x1)
        return (x1, )
    if delta < 0:
        return ()

print(solve_quadratic(1, 1, -2))  # (-2.0, 1.0)
print(solve_quadratic(1, -4, 3))  # (1.0, 3.0)
print(solve_quadratic(1, 2, 1))  # (-1.0, )
print(solve_quadratic(1, 0, 1))  # ()
