import math


def quadratic_equations_solver(a, b, c):
    if a == 0:
        return (-c / b,)
    else:
        delta = b**2 - 4 * a * c
        if delta == 0:
            return (-b / (2 * a),)
        elif delta < 0:
            return ()
        else:
            return (
                (-b - math.sqrt(delta)) / (2 * a),
                (-b + math.sqrt(delta)) / (2 * a),
            )


print(quadratic_equations_solver(0, 2, 7))
print(quadratic_equations_solver(1, 2, 1))
print(quadratic_equations_solver(1, 0, 1))
print(quadratic_equations_solver(1, 1, -2))
print(quadratic_equations_solver(3, 7, -10))
