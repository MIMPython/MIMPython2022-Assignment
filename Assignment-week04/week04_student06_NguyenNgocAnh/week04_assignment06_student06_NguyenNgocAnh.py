from sympy.geometry import Circle, Point
from sympy.abc import x, y


def Circle_1():
    P = Point(float(input('x = ')), float(input('y = ')))
    rad = float(input('Bán kính = '))
    C1 = Circle(P, rad)
    print('đường tròn')
    print(C1)


def Circle_2():
    print('Nhập điểm 1: P1')
    P1 = Point(float(input('x = ')), float(input('y = ')))
    print('Nhập điểm 2: P2')
    P2 = Point(float(input('x = ')), float(input('y = ')))
    print('Nhập điểm 3: P3')
    P3 = Point(float(input('x = ')), float(input('y = ')))
    C2 = Circle(P1, P2, P3)
    print('đường tròn')
    print(C2)


def Circle_3():
    C3 = Circle(x ** 2 + y ** 2 - 5.6 * x + 7.2 * y - 184)
    print('đường tròn')
    print(C3)


if __name__ == '__main__':
    Circle_1()
    Circle_2()
    Circle_3()
