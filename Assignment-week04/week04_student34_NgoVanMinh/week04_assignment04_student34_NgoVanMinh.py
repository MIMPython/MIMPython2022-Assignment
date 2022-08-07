import numpy as np

class Point:
    def __init__(self, x:int, y:int):
        self.x = x
        self.y = y

    def distance(self, other):
        dx = self.x - other.x
        dy = self.y - other.y
        return np.sqrt(dx ** 2 + dy ** 2)


if __name__ == '__main__':
    pA = Point(2, 2)
    pB = Point(3, 4)
    pC = Point(6, 7)

    S = 1/2 * np.abs((pB.x - pA.x)*(pC.y - pA.y) - (pC.x - pA.x)*(pB.y - pA.y))
    print("Diện tích tam giác ABC là " + str(S))

    #Diện tích tam giác ABC là 1.5

