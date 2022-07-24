def solveQuadraticEquation2(a, b, c):
    x = ()
    if a == 0:
        if b == 0:
            if c == 0:
                pass
        else:
            x = (-c / b, )
    else:
        delta = b**2 - 4*a*c
        if delta == 0:
            x = (-b / (2*a), )
        elif delta > 0:
            x = ((-b - delta**(1/2)) / (2*a), (-b + delta**(1/2)) / (2*a))
    return x
if __name__ == '__main__':
    print(solveQuadraticEquation2(1, 2, 1)) #(-1.0, )
