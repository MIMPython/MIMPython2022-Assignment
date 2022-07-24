import math
def solve_quadric_eq(a,b,c):
    if a == 0:
        if b == 0:
            if c == 0:
                print("Phương trình có tập nghiệm là tất cả các số thực")
            else:
                print("()")
        else:
            print(f"({-c/b},)")
    else:
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

a = float(input("Hệ số bậc 2 = "))
b = float(input("Hệ số bậc 1 = "))
c = float(input("Hệ số tự do = "))

solve_quadric_eq(a,b,c)

# solve_quadric_eq(0,0,1) #()
# solve_quadric_eq(1,0,1) #()
# solve_quadric_eq(1,-46,529) #(23.0,)
# solve_quadric_eq(1,-35,276) #(12.0, 23.0)
        