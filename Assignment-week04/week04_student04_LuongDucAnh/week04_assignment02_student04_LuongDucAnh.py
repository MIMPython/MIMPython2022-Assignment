import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        return None
    
    def distance(self, other, metric):
        if metric == "L1":
            return abs(self.x - other.x) + abs(self.y - other.y)
        elif metric == "L2":
            return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)
    
    def getSymmetric(self):
        return Point(-self.x, -self.y)
    
    def __repr__(self):
        return f"Point({self.x}, {self.y})"


def main():
    A = Point(3, 4)
    B = Point(5, 6)
    print(A.distance(B, "L1"))
    print(A.distance(B, "L2"))
    symmetricA = A.getSymmetric()
    print(symmetricA)
    
if __name__ == "__main__":
    main()