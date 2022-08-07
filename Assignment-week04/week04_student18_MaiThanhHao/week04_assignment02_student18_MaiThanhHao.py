import math
class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def distance(self,diem_B):
        return math.sqrt((diem_B.x - self.x)**2 + (diem_B.y - self.y)**2)
    def getSymmetry(self):
        return ( 0 - self.x, 0 - self.y )
    
diem_A = Point(2,3)
diem_B = Point(1,2)       

print('Khoảng cách A và B là: ', diem_B.distance(diem_A))
print( 'Điểm đối xứng của A là: ',diem_A.getSymmetry())

        