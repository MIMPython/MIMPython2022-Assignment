'''
Bài tập 4. (triangle area)
Một điểm nguyên trên mặt phẳng Oxy là một điểm có tung độ và hoành độ đều là các số nguyên. 
Cho ba điểm nguyên A,B,C trên mặt phẳng. Tính diện tích của tam giác (có thể suy biến) ABC.
'''

import math
from week04_assignment02_student13_MaiBaDuc import Point

class Triangle_area:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        return None
    
    def area(self, a, b):
        if self.x == a.x and self.y == a.y: return None
        elif self.x == b.x and self.y == b.y: return None
        elif a.x == b.x and a.y == b.y: return None
        else:
            m = Point.distance(self,a,'L2')
            n = Point.distance(self,b,'L2')
            p = Point.distance(a,b,'L2')
            e = (m+n+p)/2 #nua chu vi
            if m+n>p and n+p>m and m+p>n:
                return math.sqrt((e-m)*(e-n)*(e-n)*e) #cong thuc heron
            else: return None
    def main():
        a = Triangle_area(1,2)
        b = Triangle_area(2,4)
        c = Triangle_area(3,6)
        print(Triangle_area.area(a,b,c))

if __name__ == '__main__':
    Triangle_area.main()


