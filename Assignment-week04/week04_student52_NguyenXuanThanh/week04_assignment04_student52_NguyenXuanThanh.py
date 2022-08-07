class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

A = Point(5,6)
B = Point(3,5)
C = Point(8,9)

triangleArea =0.5 * abs((B.x - A.x)*(C.y - A.y) - (C.x - A.x)*(B.y - A.y))
# triangle area
print(triangleArea) # 1.5