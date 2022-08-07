from math import sqrt


class Point:
    """
    biểu diễn các điểm trong mặt phẳng xOy
    """

    def __init__(self, x, y):
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        _x = value

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        _y = value

    def distanceTo(self, metric: str, *p: tuple) -> float:
        if metric == 'L2':
            return sqrt(pow(self._x - p[0], 2) + pow(self._y - p[1], 2))
        elif metric == 'L1':
            return abs(p[0] - self._x) + abs(p[1] - self._y)

    def getSymmetricPoint(self):
        return Point(-self._x, -self._y)

    def getSymmetric(self):
        p = self.__class__.__new__(Point)
        p.__init__(-self._x, -self._y)
        return p

    def __str__(self):
        return '(' + str(self._x) + ', ' + str(self._y) + ')'

    def __repr__(self):
        return '(' + str(self._x) + ', ' + str(self._y) + ')'


def symmetricPoint(a: Point) -> Point:
    return Point(-a.x, -a.y)


if __name__ == '__main__':
    a = Point(3, 4)
    b = a.getSymmetric()
    print(b)
