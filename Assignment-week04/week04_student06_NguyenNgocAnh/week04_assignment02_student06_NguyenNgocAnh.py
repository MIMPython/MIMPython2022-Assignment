import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, other, metric):
        if metric == 'L2':
            return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)
        elif metric == 'L1':
            return abs(self.x - other.x) + abs(self.y - other.y)
        else:
            return False

    def lay_doi_xung(self):
        return Point(0 - self.x, 0 - self.y)

    def __repr__(self):
        return f'({self.x}, {self.y})'


if __name__ == '__main__':
    A = Point(4, 2)
    B = Point(0, 0)
    print('A', A)
    print('B', B)

    doi_xung_A = A.lay_doi_xung()
    print('doi_xung_A', doi_xung_A)

    metric_try = input('Nhập metric: ').upper()
    distance = A.distance(B, metric=metric_try)
    print(distance)
