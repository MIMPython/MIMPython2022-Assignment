import math
from matplotlib import pyplot as plt
import numpy as np


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def plot(self, marker="o", markersize=10, markeredgecolor="black", markerfacecolor="green"):
        x = [self.x]
        y = [self.y]

        plt.figure(figsize=(10, 15))  # size figure
        plt.plot(x, y, marker=marker, markersize=markersize,
                 markeredgecolor=markeredgecolor, markerfacecolor=markerfacecolor)
        plt.xlabel('x', fontsize=16)
        plt.ylabel('y', fontsize=16)
        plt.title('plot Point')
        plt.grid()
        plt.show()


class Line:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def plot(self, color='blue'):
        xValues = [self.x1, self.x2]
        yValues = [self.y1, self.y2]
        plt.figure(figsize=(10, 15))  # size figure
        plt.plot(xValues, yValues, '-', color=color)
        plt.xlabel('x', fontsize=16)
        plt.ylabel('y', fontsize=16)
        plt.title('plot Line')
        plt.grid()
        plt.show()


class Circle:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

# equation circle (x - a)^2 + (y - b)^2 = r^2, trong do (a, b) la toa do tam, r la ban kinh
# equation duoc viet lai la y = math.sqrt((x-a)^2 + r^2)+b
    def plot(self, color='red'):
        xValues = []
        yValues = []
        for i in range(self.x - self.radius, self.x + self.radius, 1):
            xValues.append(i)
            yValues.append(
                math.sqrt((i - self.x)**2 + self.radius**2) + self.y)

        plt.figure(figsize=(10, 15))  # size figure
        plt.plot(xValues, yValues, '-', color=color)
        plt.xlabel('x', fontsize=16)
        plt.ylabel('y', fontsize=16)
        plt.title('plot Circle')
        plt.grid()
        plt.show()


if __name__ == '__main__':
    point1 = Point(1, 1)
    # point1.plot(markersize=15, markerfacecolor='yellow',markeredgecolor='gray')
    line1 = Line(x1=1, y1=2, x2=3, y2=4)
    # line1.plot()
    circle1 = Circle(5, 5, 5)
    circle1.plot()
