"""Viết một hàm tìm tất cả các nghiệm thực (phân biệt) của phương trình ax2+bx+c=0."""
import imp


import math 

def foo(a, b, c):
    if ( a == 0):
        if(b == 0):
            return()
        else:
            return(-c/b)
    delta = float(b**2 - 4*a*c)
    if delta == 0:
        return(-b / (2*a))
    elif delta == 0:
        return(-b / (2*a))
    else:
        x1 = (float)((-b - math.sqrt(delta))/2*a)
        x2 = (float)((-b + math.sqrt(delta))/2*a)
        return(x1, x2)
    
a,b,c = map(float,(input("Nhập a,b,c: ").split()))
print(foo(a, b, c))