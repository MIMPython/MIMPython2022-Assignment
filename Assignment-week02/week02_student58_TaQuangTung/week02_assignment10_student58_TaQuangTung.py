from math import sqrt 

print("Bài 10: Equilateral polygon - Tọa độ tam giác đều ABC")

#Tọa độ điểm ban đầu A(xA, yA) và B(xB,yB)
#Tọa độ điểm C cần tìm là C(x,y)
def tamgiacdeu(xA, yA, xB, yB):
    #Gọi I là trung điểm đoạn AB
    xI = (xA + xB)/2
    yI = (yA + yB)/2
    #Vecto CI = (x - xI, y - yI)
    #Vecto AB = (xB - xA, yB - yA)
    #Cho CI.AB = 0
    k = (yB - yA)/(xB - xA)
    # x + k*y = xI + k*yI
    # x = xI - k*(y - yI)

    #Cho AC = AB
    # (x - xA)**2 + (y - yA)**2 = (xB - xA)**2 + (yB - yA)**2
    l = (xB - xA)**2 + (yB - yA)**2
    # (x - xA)**2 + (y - yA)**2 = l
    z = xA - xI - k*yI
    # (k**2 + 1)*(y**2) + (2*k*z - 2*yA)*y + z**2 - l = 0
    a = k**2 + 1
    b = 2*k*z - 2*yA
    c = z**2 - l

    d = b**2 - 4*a*c
    if d < 0:
        print("Không có tọa độ điểm C thỏa mãn yêu cầu đề bài")
    elif d == 0:
        y = -b/(2*a)
        x = xI - k*(y - yI)
        print("Tọa độ điểm C là: (" + str(x) + ", " + str(y))
    else:
        y1 = (-b + sqrt(d))/(2*a)
        x1 = xI - k*(y1 - yI)
        print("Tọa độ điểm C1 là: (" + str(x1) + ", " + str(y1))

        y2 = (-b - sqrt(d))/(2*a)
        x2 = xI - k*(y2 - yI)
        print("Tọa độ điểm C2 là: (" + str(x2) + ", " + str(y2))
xA = float(input("Nhập hoành độ điểm A với xA = "))
yA = float(input("Nhập tung độ điểm A với yA = "))
xB = float(input("Nhập hoành độ điểm B với xB = "))
yB = float(input("Nhập tung độ điểm B với yB = "))

tamgiacdeu(xA, yA, xB, yB)