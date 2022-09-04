from Vector import Vector
from Point import Point

class Line:
    __point__: Point 
    __vector__: Vector

    def __init__(self, point: Point, vector: Vector):
        self.__point__: Point = point
        self.__vector__: Vector = vector
    
    def getNormalVector(self):
        return self.__vector__

    def setNomarlVector(self, vector: Vector):
        self.__vector__ = vector
    
    def getDirectionVector(self):
        vec = self.__vector__.getVec()
        return Vector(( vec[1], -vec[0]))
    
    def __repr__(self) -> str:
        a, b = self.__vector__.getVec()
        x, y = self.__point__.getCoordinate()
        line = ""
        if a != 0:
            if a != 1 and a!= -1:
                line += str(a)
            elif a == -1:
                line += "-"
            line += "x "

        if b != 0:
            if b != 1 and b!= -1:
                line += str(b)
            elif b == -1:
                line += "-"
            line += "y "
        
        c = - a * x - b * y
        if c != 0:
            if c < 0: line += "-"
            else: line  += "-"
            line += str(c)

        return line

