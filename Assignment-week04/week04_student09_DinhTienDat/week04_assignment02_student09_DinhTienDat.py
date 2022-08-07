import math

class Point:
#initializing a class
    def __init__(self, name, x, y):
        self.x = x
        self.y = y
        self.name = name
#Function to read the coordinates
    def read_coordinate(self):
        print(f"The coordinate of point {self.name} is ({self.x},{self.y})")

#Call out the x-coordinate
    def read_x(self):
        return self.x
#Call out the y-coordinate
    def read_y(self):
        return self.y

#Distance function
    def distance(self, other, metric):
        x_distance = self.x - other.x
        y_distance = self.y - other.y
        L2 =  math.sqrt((x_distance)**2 + (y_distance)**2)
        L1 = abs(x_distance + y_distance)

        if metric == 'L1':
            print(f'The {metric} distance between {self.name}',\
                 f'and {other.name} is {L1}')

        elif metric == 'L2':
            print(f'The {metric} distance between {self.name}',\
                 f'and {other.name} is {L2}')

#Origin-to-origin symmetry function that depends on the defined class 'Point' 
    def point_symmetry(self):
        print(f'The image of the origin-to-origin symmetry of {self.name}',\
            f'is ({- self.x},{- self.y})')

#Origin-to-origin symmetry function that is not depends on the defined class 'Point'
def symmetry(a,b):
    print(f"The image of the origin-to-origin symmetry of",\
        f"({a},{b}) is ({-a},{-b})")

#Code testing 



