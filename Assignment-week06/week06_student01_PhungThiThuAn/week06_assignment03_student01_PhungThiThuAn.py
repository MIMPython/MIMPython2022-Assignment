import matplotlib.pyplot as plt
import numpy as np

def displayCoef(number):
    if number > 0:
        if number == 1:
            return '+ '
        return f'+ {number}'
    else:
        if number == -1:
            return '- '
        return '- ' + str(number)[1:]

class Point:
    '''
    Creates a point on a coordinate plane with values x and y.
    
    '''
    def __init__(self, x, y):
        '''
        Defines x and y variables
        
        '''
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f'({self.x},{self.y})'

    def plot(self):
        plt.plot(self.x, self.y, 'o')
        plt.title(str(self))        
        # plt.show()

class Line:
    '''
    Creates a line in Oxy plane
    '''
    def __init__(self, a, b, c):
        '''
        Defines a, b, c variables
        
        '''        
        self.a = a
        self.b = b
        self.c = c

    def __str__(self) -> str:
        if self.isValidLine():
            b = displayCoef(int(self.b))
            c = displayCoef(int(self.c))
            return f'{self.a}x {b}y {c} = 0'
        else:
            return 'Error: Invalid Line.'

    @classmethod
    def isValidLine(self):
        # condition: a != 0 and b!= 0
        return self.a** 2 + self.b**2 != 0 

    @classmethod
    def initializeByPoints(cls, pointA, pointB):
        '''
        Create a Line object by 2 points.
        
        '''
        cls.a = pointA.y - pointB.y
        cls.b = pointB.x - pointA.x
        cls.c = - cls.a*pointA.x - cls.b*pointA.y
        return Line(cls.a, cls.b, cls.c)
            
    def plot(self):
        if self.isValidLine():
            if self.b == 0:
                y = np.linspace(-1, 5, 2, endpoint=True)
                x = (self.b * y + self.c)/self.a
            else:
                x = np.linspace(-1, 5, 2, endpoint=True)
                y = (self.a * x + self.c)/self.b
            plt.plot(x, y, '-b')
            plt.grid()
            plt.title(str(self))
            # plt.show()
            
        else: 
            print('Error: Invalid Line')
           
class Circle:
    '''
    Create a circle from a point and radius
    '''
    def __init__(self, point, radius) -> None:
        self.point = point
        self.radius = radius

    def __str__(self) -> str:
        x0 = displayCoef(self.point.x *-1)
        y0 = displayCoef(self.point.y *-1)
        return f'(x {x0})^2 + (y {y0})^2 = {self.radius**2}'
    
    def plot(self):
        xstart = self.point.x - self.radius
        xend = self.point.x + self.radius
        ystart = self.point.y-self.radius
        yend = self.point.y+self.radius
        x = np.linspace(xstart, xend, 1000)
        y1 = np.sqrt(self.radius**2 - (x - self.point.x)**2) + self.point.y
        y2 = -np.sqrt(self.radius**2 - (x - self.point.x)**2) + self.point.y
        plt.axis('equal')
        self.point.plot()
        plt.plot(x, y1, '-r')
        plt.plot(x, y2, '-r')
        plt.title(str(self))
        # plt.show()        

# fig, (ax1, ax2, ax3) = plt.subplots(1, 3)
path = 'additionalFolder/'
point1 = Point(2, 4)
point1.plot()
plt.savefig(path + 'Point.jpg')

fig1, ax1 = plt.subplots()
line = Line.initializeByPoints(Point(3, -1), Point(4, 1))
print(line)
ax1 = line.plot()
fig1.savefig(path + 'Line.jpg')

fig2, ax2 = plt.subplots()
cir = Circle(Point(6, 5), 3)
print(cir)
ax2 = cir.plot()
fig2.savefig(path + 'Circle.jpg')
