#Bài 4
from math import sqrt
xA = int(input("xA = "))
xB = int(input("xB = "))
xC = int(input("xC = "))
yA = int(input("yA = "))
yB = int(input("yB = "))
yC = int(input("yC = "))

c = AB = sqrt((xA - xB)**2 + (yA - yB)**2)
b = AC = sqrt((xA - xC)**2 + (yA - yC)**2)
a = BC = sqrt((xB - xC)**2 + (yB - yC)**2)
p = (a + b + c)*(1/2)
S = sqrt(p*(p-a)*(p-b)*(p-c))
print("Diện tích tam giác ABC là" ,S)

# A(3,2)
# B(0,1)
# C(1,5)