import math
class Point:
    def __init__(self,x,y):
        self.x =x
        self.y =y

    def __repr__(self):
        return 'Point({}, {})'.format(self.x, self.y)

    def distance(self,pointB,metric):
        if (metric=="L2"):
            return math.sqrt((self.x-pointB.x)**2+(self.y-pointB.y)**2)
        if (metric=="L1"):
            return abs(self.x-pointB.x) + abs(self.y-pointB.y)
    
    def diemDoiXung(self):
        diemDX= Point(0,0)
        diemDX.x = -self.x
        diemDX.y = -self.y
        return diemDX
   
if __name__=="__main__":
    pA=Point(1,1)
    pB=Point(2,1)
    print("Khoang cach cua A va B theo L1 la:")
    print(pA.distance(pB,"L1"))
    print("Khoang cach cua A va B theo L2 la:")
    print(pA.distance(pB,"L2"))
    print("Diem doi xung cua A la:")
    t=pA.diemDoiXung()
    print(t.__repr__())
    
    
    

    



