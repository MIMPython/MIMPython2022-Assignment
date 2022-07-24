import math
import numpy as np 
import matplotlib.pyplot as plt

print("Nhập xA:", end='')
a = float(input())
print("Nhập yA:", end='')
b = float(input())
print("Nhập xB:", end='')
c = float(input())
print("Nhập yB:", end='')
d = float(input())

if a.is_integer():
    a = int(a)
if b.is_integer():
    b = int(b)
if c.is_integer():
    c = int(c)
if d.is_integer():
    d = int(d)

tuple_A = (a,b)
tuple_B = (c,d)
print(f"A{tuple_A} \nB{tuple_B}")

#Ham draw() dung de ve tam giac
def draw(x1, y1, x2, y2):
        X = np.array([[a,b], [c,d], [x1, y1], [a, b], [c, d], [x2, y2]])
        Y = ['red', 'red', 'red', 'blue', 'blue', 'blue']  

        plt.figure()
        plt.scatter(X[:, 0], X[:, 1], s = 170, color = Y[:])

        t1 = plt.Polygon(X[:3,:], color=Y[0])
        plt.gca().add_patch(t1)

        t2 = plt.Polygon(X[3:6,:], color=Y[3])
        plt.gca().add_patch(t2)

        plt.show()

if a==c and b==d:
    print("Không tồn tại tam giác ABC.")
else:
    if b==d:
        x1 = (a+c)/2
        x2 = (a+c)/2
        
        y1 = b - ((math.sqrt(3))/2) * (math.sqrt((a-c)**2 + (b-d)**2))
        y2 = b + ((math.sqrt(3))/2) * (math.sqrt((a-c)**2 + (b-d)**2))
        
        if x1.is_integer():
            x1 = int(x1)
        if x2.is_integer():
            x2 = int(x2)
        if y1.is_integer():
            y1 = int(y1)
        
        #isinstance(y2, int) kiem tra xem y2 co phai so nguyen hay khong
        if isinstance(y2, int)==False:
            y2 = b + ((math.sqrt(3))/2) * (math.sqrt((a-c)**2 + (b-d)**2))
        
        c1 = (x1,y1)
        c2 = (x2,y2)
        
        print(f"Với C{c1} hoặc C{c2} thì tam giác ABC đều.")
    
        draw(x1, y1, x2, y2)
        
    
    else:
        #Giải phương trình bậc 2 (mx^2 + nx + p = 0) sao cho AC = AB (C là điểm cần tìm) bằng cách gọi điểm C theo phương trình đường thẳng đi qua trung điểm O của AB và vuông góc với AB. Nghiệm của phương trình chính là toạ độ x của điểm C trong tam giác ABC.
        m = 1 + ((c-a)/(b-d))**2
        n = -2*a + (2*(c-a)*(a**2 - c**2 - (b-d)**2))/((b-d)*2*(b-d))
        p = ((a**2 - c**2 - (b-d)**2)/(2*(b-d)))**2 - (a-c)**2 - (b-d)**2 + a**2
        
        delta = n**2 - 4*m*p
        
        print(delta)
        
        x1 = (-n + math.sqrt(delta))/(2*m)
        x2 = (-n - math.sqrt(delta))/(2*m)
        
        y1 = ((c-a)*x1)/(b-d) + (a**2 - c**2 + b**2 - d**2)/(2*(b-d))
        y2 = ((c-a)*x2)/(b-d) + (a**2 - c**2 + b**2 - d**2)/(2*(b-d))
        
        if x1.is_integer():
            x1 = int(x1)
        if x2.is_integer():
            x2 = int(x2)
        if y1.is_integer():
            y1 = int(y1)
        if y2.is_integer():
            y2 = int(y2)
        
        c1 = (x1,y1)
        c2 = (x2,y2)
        
        print(f"Với C{c1} hoặc C{c2} thì tam giác ABC đều.")
            
        draw(x1, y1, x2, y2)
    
    
    


