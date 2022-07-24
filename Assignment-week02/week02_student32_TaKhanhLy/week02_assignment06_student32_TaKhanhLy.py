
from math import sqrt

def pt_bac2(a,b,c):
    if a == 0:
        if b == 0:
            if c == 0:
                return ('Vo so nghiem',)
            else:
                return ('Vo nghiem',)
        else:
            if c == 0:
                return ('Nghiem duy nhat la 0',)
            else:
                x = int(-c / b)
                return (x,)
    else:
        delta = b ** 2 - 4 * a * c

        if delta < 0:
            return('Vo nghiem',)

        elif delta == 0:
            x = int(-b / (2 * a))
            return (x,)

        else:
            x1 = int((-b - sqrt(delta)) / (2 * a))
            x2 = int((-b + sqrt(delta)) / (2 * a))

            return x1, x2


print(pt_bac2(2,5,7))
print(pt_bac2(3,3,-3))
print(pt_bac2(-1,0,0))


