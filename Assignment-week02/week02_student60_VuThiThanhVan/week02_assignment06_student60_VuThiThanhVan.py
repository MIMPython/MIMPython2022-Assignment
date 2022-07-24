

from cmath import sqrt
def foo(a,b,c):
    if (a==0 and b==0 and c!=0): print("()")
    if (a==0 and b==0 and c==0): print("vo so nghiem")
    if (a==0 and b!=0 ): print (-c/b)
    denta=float(b*b-4*a*c)
    if denta<0: print("()")
    if denta==0: print(-b/(2*a))
    if denta>0: 
        print((-b-sqrt(denta))/2*a, end=",")
        print((-b+sqrt(denta))/2*a)
    return;
x=float(input())
y=float(input())
z=float(input())

foo(x,y,z)
    
 
