"""
Bài tập 6. Viết một hàm tìm tất cả các nghiệm thực (phân biệt) của phương trình
ax^2+bx+c=0.
Input: ba số a, b, c bất kỳ
Output: một tuple chứa tất cả các nghiệm thực (phân biệt), xếp theo thứ tự tăng dần, 
của phương trình ax2+bx+c=0.
"""
import math

def calculate_delta(a,b,c):
    return b*b - 4*a*c

def sqrt(x):
    return math.sqrt(x)

def solve_equation(a, b, c):
    delta = calculate_delta(a, b, c)
    if a == 0:
        if b == 0:
            if c == 0:
                print("Phương trình có vô số nghiệm!")
            else:
                solution = ()
        else:
            solution = (-c / b,)
    elif delta < 0:
        solution = ()
    elif delta == 0:
        solution = (-b / (2 * a),)
    else:
        x1 = (-b - sqrt(delta)) / (2 * a)
        x2 = (-b + sqrt(delta)) / (2 * a)
        solution = (x1, x2)
    return solution

a = float(input("Nhập a = "))
b = float(input("Nhập b = "))
c = float(input("Nhập c = "))

print(f"Tập nghiệm của phương trình là", solve_equation(a, b, c))

            