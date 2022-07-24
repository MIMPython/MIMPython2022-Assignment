import math
def solveEquation(a, b, c):
    delta = b**2 - 4*a*c
    if delta < 0:
        return()
    elif delta == 0:
        x = -b/(2*a)
        return(x,)
    else:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        return(x1,x2)

def main():
    print(solveEquation(1,2,1))
    print(solveEquation(-2,-3,5))
    print(solveEquation(1,0,1))

if __name__ == '__main__':
    main()