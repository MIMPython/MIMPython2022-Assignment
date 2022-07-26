'''
Viết một hàm tìm tất cả các nghiệm thực (phân biệt) của phương trình
ax2+bx+c=0.
Input: ba số a, b, c bất kỳ
Output: một tuple chứa tất cả các nghiệm thực (phân biệt), xếp theo thứ tự tăng dần, của phương trình ax2+bx+c=0.
'''
import math
def solve(a,b,c):
    if ( a == 0 ):
        if ( b == 0 ):
            if ( c == 0 ):
                return tuple()
            else:
                return tuple()
        else:
            if c == 0:
                x = (int)(0)
                return (x,)
            else:
                x = (float)(-c/b)
                return (x,)
    else:
         delta = (b * b - 4*a*c)
         if (delta < 0):
             return tuple()
         elif(delta == 0):
         
             x = (float) (-b/2*a)
             return (x,)
         else:
    
             x1 = ( -b + math.sqrt(delta))/(2*a)
             x2 = ( -b - math.sqrt(delta))/(2*a)
             return x1,x2
example1 = tuple(solve(1,2,-3))
example2 = tuple(solve(1,2,1))
print(example1)
print(example2)

    