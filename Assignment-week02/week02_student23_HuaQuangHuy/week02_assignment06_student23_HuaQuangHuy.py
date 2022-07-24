# Bài tập 6: Viết hàm số giải phương trình bậc 2 với a,b,c bất kỳ
import math


def solveQuadraticEquation(a, b, c):
    if a == 0:
        if b == 0:
            if c == 0:
                return  # vô số nghiệm
            else:
                return ()
        else:
            solve = (-c / b,)
            return solve
    else:
        delta = getDelta(a, b, c)
        if delta > 0:
            x1 = (-b - math.sqrt(delta)) / (2 * a)
            x2 = (-b + math.sqrt(delta)) / (2 * a)
            if x1 >= x2:
                return (x2, x1)
            else:
                return (x1, x2)
        elif delta == 0:
            x = (-b) / (2 * a)
            return (x, )
        else:
            return ()


def getDelta(a, b, c):
    return b**2 - 4 * a * c


if __name__ == '__main__':
    # phương trình vô số nghiệm
    print(solveQuadraticEquation(0, 0, 0))
    # phương trình vô nghiệm
    print(solveQuadraticEquation(0, 0, 1))
    # phương trình có nghiệm kép
    print(solveQuadraticEquation(1, 4, 4))
    # phương trình có 2 nghiệm phân biệt
    print(solveQuadraticEquation(-3, 2, 1))
