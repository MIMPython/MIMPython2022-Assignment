#bài 6
from cmath import sqrt
def giaiphuongtrinhb2(a,b,c):
    delta = b**2-4*a*c

    if (delta>0):
        x1 = (-b+sqrt(delta))/(2*a)
        x2 = (-b-sqrt(delta))/(2*a)
        result = (x1.real,x2.real)
        result = sorted(result)
        result = tuple(result)
        print(result)
    elif(delta==0):
        x = (-b)/(2*a)
        result = (x.real,)
        result = tuple(result)
        print(result)
    else:
        result = ()
        result = tuple(result)
        print(result)
giaiphuongtrinhb2(1,3,2) #(-2.0, -1.0)
giaiphuongtrinhb2(1,2,1) #(-1.0,)
giaiphuongtrinhb2(3,4,5) #()