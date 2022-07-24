from cmath import sqrt


def foo(a, b, c):
    D = b**2 - 4*a*c 
    if D<0:
        res=()
        return res
    elif D==0:
        x=-b/(2*a)
        res = (x, )
        return res
    else :
        x1= (-b - sqrt(D))/(2*a)
        x2= (-b + sqrt(D))/(2*a)
        res = (x1, x2)
        return res

print(foo(1, 1, -2)) #
print(foo(1, 2, 1)) #
print(foo(1, 0, 1)) #