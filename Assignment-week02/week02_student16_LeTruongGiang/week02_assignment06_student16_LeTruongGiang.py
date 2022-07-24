import math

print("Xét phương trình ax^2 + bx + c = 0")

print("Nhập a: ", end='')
a = int(input())
print("Nhập b: ", end='')
b = int(input())
print("Nhập c: ", end='')
c = int(input())

def tuple(a,b,c):
    if a == 0:
        if b == 0:
            result = ()
        else:
            x = -c/b
            if x.is_integer():
                x = int(x)
            result = (x)
            return result 
    else:
        delta = b**2 - 4*a*c
        if delta < 0:
            result = ()
            return result
        else:
            if delta == 0:
                x = -b/(2*a)
                if x.is_integer():
                    x = int(x)
                result = (x, )
                return result
            if delta > 0:
                x2 = (-b + math.sqrt(delta))/(2*a)
                x1 = (-b - math.sqrt(delta))/(2*a)
                if x1.is_integer():
                    x1 = int(x1)
                if x2.is_integer():
                    x2 = int(x2)
                result = (x1, x2)
                return result
    return None

print(tuple(a,b,c))
            


