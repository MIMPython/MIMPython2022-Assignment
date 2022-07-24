#Bài tập 6. Viết một hàm tìm tất cả các nghiệm thực (phân biệt) của phương trình

def delta(a, b, c):
    return b**2 - 4*a*c

def solution(a, b, c):
    if delta(a, b, c) > 0:
        x1 = (-b + delta(a, b, c)**(0.5))/(2*a)
        x2=  (-b - delta(a, b, c)**(0.5))/(2*a)
        res = (x1, x2)
    elif delta(a, b, c) == 0:
        res = (b/(2*a))
    else:
        res = ()
    print(res)

if __name__ == "__main__":
    solution(1, 1, -2) # (1.0, -2.0)
    solution(1, 2, 1) # (-1.0)
    solution(1, 0, 1) # ()