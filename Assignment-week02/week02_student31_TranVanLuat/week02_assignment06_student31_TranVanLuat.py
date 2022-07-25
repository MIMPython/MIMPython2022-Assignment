def solve_equation(a, b, c):
    answer = ()
    if a == 0:
        if b == 0:
            if c == 0:
                pass
        else:
            answer= (-c / b, )
    else:
        delta = b**2 - 4*a*c
        if delta == 0:
            answer = (-b / (2*a), )
        elif delta > 0:
            answer = ((-b - delta**(1/2)) / (2*a), (-b + delta**(1/2)) / (2*a))
    return answer

if __name__ == '__main__':
    print(solve_equation(4,-2,-6)) # (-1, 1.5)
    print(solve_equation(1, 2, 1))  # (-1.0,)
    print(solve_equation(1, 2, 3))  # ()
    print(solve_equation(1, 0, 0))  # (0.0)