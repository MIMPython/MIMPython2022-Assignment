import math
def giai_phuong_trinh(a,b,c):
    if a != 0:
        delta = b**2 - 4*a*c
        if delta < 0:
            print("()")
        else:
            if delta == 0:
                print(f"({-b/(2*a)},)")
            else:
                x_1 = (-b + math.sqrt(delta))/(2*a)
                x_2 = (-b - math.sqrt(delta))/(2*a)
                if x_1 < x_2:
                    solution = (x_1, x_2)
                else:
                    solution = (x_2, x_1)
                print(solution)

       
    else:
        if b == 0:
            if c == 0:
                print("Phương trình có tập nghiệm là tất cả các số thực")
            else:
                print("()")
        else:
            print(f"({-c/b},)")
        

a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

giai_phuong_trinh(a,b,c)

#giai_phuong_trinh(1, -21, 108) # (9.0, 12.0)
#giai_phuong_trinh(1, -24, 144) # (12.0,)
#giai_phuong_trinh(1, 0 , 2003) # ()