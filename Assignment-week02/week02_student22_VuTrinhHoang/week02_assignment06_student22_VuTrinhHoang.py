def SolveEquation(a, b, c):
    AnswerTuple = ()
    if a == 0:
        if b == 0:
            if c == 0:
                pass
        else:
            AnswerTuple = (-c / b, )
    else:
        delta = b**2 - 4*a*c
        if delta == 0:
            AnswerTuple = (-b / (2*a), )
        elif delta > 0:
            AnswerTuple = ((-b - delta**(1/2)) / (2*a), (-b + delta**(1/2)) / (2*a))
    return AnswerTuple

if __name__ == '__main__':
    print(SolveEquation(1, 1, -2)) # (-2.0, 1.0)
    print(SolveEquation(1, 2, 1))  # (-1.0,)
    print(SolveEquation(1, 0, 1))  # ()
