'''
Bài tập 4. (triangle area)
Một điểm nguyên trên mặt phẳng Oxy là một điểm có tung độ và hoành độ đều là các số nguyên. Cho ba điểm nguyên A,B,C trên mặt phẳng. Tính diện tích của tam giác (có thể suy biến) ABC.
'''

# Formula of triangle area = |(1/2)*(x1*(y2-y3)+x2*(y3-y1)+x3*(y1-y2))|

class TriangleArea:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getTriangleArea(self, p1, p2):
        return 0.5*abs(self.x*(p1.y-p2.y) + p1.x*(p2.y-self.y) + p2.x*(self.y-p1.y))


pointA = TriangleArea(0,0)
pointB = TriangleArea(1,2)
pointC = TriangleArea(7,10)

print(pointA.getTriangleArea(pointB, pointC)) #2.0
