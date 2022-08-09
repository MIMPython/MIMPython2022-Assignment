import math
class Point:
    # initial function
    def __init__(self, x, y): 
        self.x = x
        self.y = y
    # function that calculates distance
    def distance(self, PointB, metric):#hơi ảo
        if metric == "L1":
            distance = abs(PointB.x-self.x) + abs(PointB.y - self.y)
            return distance
        elif metric == "L2":
            distance = math.sqrt((PointB.x-self.x)**2 + (PointB.y - self.y)**2)
            return distance
        else: 
            print("invalid letter!")
    #câu 3
    def symmetric_point(self):
        horizontal = -1*self.x
        vertical = -1*self.y
        return str(horizontal) + ", " + str(vertical)
    def __repr__(self):
        return f'{self.x}, {self.y}'

PointA = Point(3, 4)
PointB = Point(4, 5)
print(PointA.distance(PointB, metric = "L1"))
print(PointA.symmetric_point())
print(PointA.__repr__())