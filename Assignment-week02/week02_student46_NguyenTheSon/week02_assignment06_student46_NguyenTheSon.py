import math

def foo(a,b,c):
    delta = b ** 2 - 4*a*c
    result = ()
    if delta > 0:
        x_1 = (- b + math.sqrt(delta)) / (2 * a)
        x_2 = (- b - math.sqrt(delta)) / (2 * a)
        result = (x_2, x_1)
    elif delta == 0:
        x = - b / (2 * a)
        result = (x, )
    else:
        result = ()
    print(result)

if __name__ == '__main__':
    foo(1, -4, 3) #(1.0, 3.0)
    foo(2, 4, 2) # (-1.0,)
    foo(1, 1, 1) #()