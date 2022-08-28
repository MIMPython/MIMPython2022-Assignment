from venv import create
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def draw(self):
        sns.lineplot(x = [self.x], y = [self.y], marker = 'o', markersize= 10, color = 'r')
        plt.show()

class Line():
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
    def draw(self):
        plt.plot([self.x1, self.x2], [self.y1, self.y2]) #vẽ theo mảng
        plt.show()

class Circle():
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color        
    def draw(self):
        plt.Circle((self.x, self.y), self.radius, color = self.color)
        fig, ax = plt.subplots()
        ax.add_artist(plt.Circle((self.x, self.y), self.radius, color = self.color))
        plt.show()

