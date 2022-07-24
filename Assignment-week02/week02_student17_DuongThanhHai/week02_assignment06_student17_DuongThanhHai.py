
from math import sqrt

def pt_bac2(a,b,c):
    if a == 0:
        if b == 0:
            if c == 0:
                return tuple()
            else:
                return tuple()
        else:
            if c == 0:
                x=int(0)
                return (x,)
            else:
                x = int(-c / b)
                return (x,)
    else:
        delta = b ** 2 - 4 * a * c

        if delta < 0:
            return tuple()

        elif delta == 0:
            x = int(-b / (2 * a))
            return (x,)

        else:
            x1 = int((-b - sqrt(delta)) / (2 * a))
            x2 = int((-b + sqrt(delta)) / (2 * a))

            return x1, x2

result1 = tuple( pt_bac2(1,-5,6) )
result2 = tuple( pt_bac2(1,4,4) )
result3 = tuple( pt_bac2(1,0,2))

print (result1)
print (result2)
print (result3)


