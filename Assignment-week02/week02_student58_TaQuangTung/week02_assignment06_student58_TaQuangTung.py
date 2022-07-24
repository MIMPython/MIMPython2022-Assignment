from math import sqrt
print("Bài 6: Viết hàm giải phương trình bậc hai")
def ptb2(a, b, c):
    tup = ()
    if a == 0:
        if b == 0:
            if c == 0:
                print("Phương trình có vô số nghiệm")
            else:
                print(tup)
        else:
            x = -c/b
            tup += (x, )
            print(tup)
    else:
        d = b**2 - 4*a*c
        if d < 0:
            print(tup)
        elif d == 0:
            x = -b/(2*a)
            tup += (x, )
            print(tup)
        else:
            x1 = (-b + sqrt(d))/(2*a)
            x2 = (-b - sqrt(d))/(2*a)
            tup += (x2, x1, )
            print(tup)

a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))
ptb2(a,b,c)    

#ptb2(1, 1, -2) = (-2, 1)
#ptb2(1, 2, 1) = (-1, )
#ptb2(1, 0, 1) = ()