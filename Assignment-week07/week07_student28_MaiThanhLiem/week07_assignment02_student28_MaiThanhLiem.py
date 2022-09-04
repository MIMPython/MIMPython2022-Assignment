import numpy as np


class Rectangle:
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def __repr__(self):
        return f"Rectangle({self.height},{self.width})"

    @property
    def perimeter(self):
        return (self.height + self.width) * 2

    @property
    def area(self):
        return self.width * self.height


class Rhombus:
    def __init__(self, length, theta):
        """Rhombus has 4 equal side length,
        and theta is one angle between two side of the shape."""
        self.length = length
        self.theta = theta

    def __repr__(self):
        return f"Rhombus({self.length},{self.theta})"

    @property
    def diagonal(self):
        diagonal1 = 2 * self.length * np.cos(self.theta / 2)
        diagonal2 = 2 * self.length * np.cos((np.pi - self.theta) / 2)
        return (diagonal1, diagonal2)

    @property
    def area(self):
        return np.rint(0.5 * self.diagonal[0] * self.diagonal[1])


class Square(Rectangle, Rhombus):
    def __init__(self, side):
        self.side = side
        Rectangle.__init__(self, side, side)
        Rhombus.__init__(self, side, np.pi / 2)

    def __repr__(self):
        return f"Square({self.side})"


class Ellipse:
    def __init__(self, a, b):
        """General equations for ellipse:
        x^2/a^2 + y^2/b^2 = 1
        - Center: (0,0)
        - c^2 = a^2 - b^2
        - Foci: (c,0), (-c,0)
        - Radius:
            + horizontal: a
            + vertical: b

        """
        self.a = a
        self.b = b

    def __repr__(self):
        return f"Ellipse with equation: x^2/{self.a}^2 + y^2/{self.b}^2 = 1"

    @property
    def area(self):
        return np.pi * self.a * self.b

    @property
    def eccentricity(self):
        return np.sqrt(1 - (self.b) ** 2 / (self.a) ** 2)

    @property
    def perimeter(self):
        func = lambda x: np.sqrt(1 - (self.eccentricity * np.sin(x)) ** 2)
        theta = np.linspace(0, np.pi / 2, 1000, endpoint=True)
        P = 4 * self.a * np.trapz(func(theta), theta)
        return P


class Circle(Ellipse):
    def __init__(self, radius):
        self.radius = radius
        super().__init__(radius, radius)

    def __repr__(self):
        return f"Circle with equation: x^2 + y^2 = {self.radius}"


if __name__ == "__main__":
    A = Square(8)
    print(A)
    print(Rectangle.__repr__(A))
    print(Rhombus.__repr__(A))
    print(A.diagonal)
    print(A.area)
    print(A.perimeter)
    B = Ellipse(3, 2)
    print(B)
    print(B.area)
    print(B.eccentricity)
    print(B.perimeter)
    C = Circle(4)
    print(C.area)
    print(C.eccentricity)
    print(C.perimeter)
