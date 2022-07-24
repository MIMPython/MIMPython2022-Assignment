import math
def foo(a,b,c):
    delta = b**2 - 4*a*c
    if delta == 0:
        x = -b/(2*a)
        return (x)
    elif delta > 0:
        x1 = (-b+math.sqrt(delta))/(2*a)
        x2 = (-b-math.sqrt(delta))/(2*a)
        return (x1,x2)
    else:
        return ()


if __name__ == '__main__':
    print(foo(1,10,3))
    #(-0.30958424017657027, -9.69041575982343)
    print(foo(1,1,-2))
    #(1.0, -2.0)