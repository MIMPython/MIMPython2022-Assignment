from cmath import inf
import math
from os import name

def ptb2(a,b,c):
    result=()
    denta=0
    if (a==0):
        if (b==0):
            if (c==0):
                result=result+(-inf,inf)
                return result
            else:
                return result
        else:
            result=result+(-b/c,)
            return result
    else:
        denta=(b*b-4*a*c)
        if (denta<0):
            return result
        elif (denta==0):
            result=result+(-b/(2*a),)
            return result
        else:
            x1=(-b-math.sqrt(denta))/(2*a)
            x2=(-b+math.sqrt(denta))/(2*a)
            if (x1<x2):
                result=result+(x1,)+(x2,)
            else:
                result=result+(x2,)+(x1,)
            return result

if __name__ == '__main__':
    print("Nhap so a")
    a= int (input())
    print("Nhap so b")
    b=int (input())
    print("Nhap so c")
    c=int (input())
    print("Nghiem cua phuong trinh ax^2+bx+c la: ")
    print(ptb2(a,b,c))



