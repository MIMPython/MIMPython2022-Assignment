import math
class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def distance(self,diem_A):
        return math.sqrt((diem_A.x - self.x)**2 + (diem_A.y - self.y)**2)

diem_A = Point(2,3)
diem_B = Point(4,8)   
diem_C = Point(3,4)

p = (float)( ( diem_A.distance(diem_B) + diem_B.distance(diem_C) + diem_C.distance(diem_A) ) / 2 ) 
area = math.sqrt(p * ( p - diem_A.distance(diem_B) ) * ( p - diem_B.distance(diem_C) ) * ( p - diem_C.distance(diem_A) ))

print('Diện tích là: ', area)

