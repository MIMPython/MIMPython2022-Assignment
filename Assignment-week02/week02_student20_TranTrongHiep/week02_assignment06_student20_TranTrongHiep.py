def foo(x)
    return x**2

def equa(a,b,c)
    dt = foo(b) - 4*a*c

    import math
    if dt > 0
        x1 = (-b - math.sqrt(dt)) / (2*a)
    else if dt = 0
        x1 = x2 = -b / (2*a)
    else
        x1 = 'Phương trình vô nghiệm'

    return x1,x2

equa(1,1,-2)
