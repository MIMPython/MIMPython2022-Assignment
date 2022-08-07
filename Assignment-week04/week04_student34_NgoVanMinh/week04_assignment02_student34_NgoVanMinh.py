import numpy as np


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, other):
        dx = self.x - other.x
        dy = self.y - other.y
        return np.sqrt(dx ** 2 + dy ** 2)

    def distance(self, other, metric: str):
        dx = self.x - other.x
        dy = self.y - other.y
        distance = 0
        if metric == 'L1':
            distance = np.abs(dx) + np.abs(dy)
        elif metric == 'L2':
            distance = np.sqrt(dx ** 2 + dy ** 2)
        return distance

    def symmetry(self):
        return f'{-self.x, -self.y}'

    def __repr__(self):
        rep = 'Point(' + str(self.x) + ',' + str(self.y) + ')'
        return rep


if __name__ == '__main__':
    pointA = Point(4, 2)
    pointB = Point(3, 4)

    #In ra thông tin các điểm
    print(pointA.__repr__())    #Point(4,2)
    print(pointB.__repr__())    #Point(3,4)

    #Tính theo chuẩn 1 và chuẩn 2
    print(pointA.distance(pointB,'L1'))     #3
    print(pointA.distance(pointB,'L2'))     #2.23606797749979

    #Điểm đối xứng
    print(pointA.symmetry())                #(-4, -2)





