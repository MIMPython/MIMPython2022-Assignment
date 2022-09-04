from math import *
from typing_extensions import Self
from scipy import integrate

class Rectangle:
    __length__ = 0.0
    __width__ = 0.0
    __color__ = {"White" : (255, 255, 255)}

    def __init__(self, length: float = 1, width: float = 1, color: dict = {"White":(255, 255, 255)}):
        self.__length__ = length
        self.__width__ = width
        self.__color__ = color

    def getLenth(self) -> float:
        return self.__length__
    
    def getWidth(self) -> float:
        return self.__width__

    def getWidth(self) -> float:
        return self.__color__

    def setLength(self, length: float = 1):
        self.__length__ = length

    def setWidth(self, width: float = 1):
        self.__width__ = width
    
    def setColor(self, name: str = "Unknown", rbg: tuple = (1, 1, 1)):
        self.__color__ = {name: rbg}
    
    def area(self) -> float:
        return self.__length__ * self.__width__
    
    def perimeter(self) -> float:
        return (self.__length__ + self.__width__) * 2

    def __repr__(self) -> str:
        name = list(self.__color__.keys())[0]
        color = self.__color__[name]
        return "Rectangle [Length = {}; Width = {}; color = {}|{}]".format(
                self.__length__, self.__width__, name, color)

class Square(Rectangle):
    def __init__(self, edge :float = 1, color: dict = { "White": (255, 255, 255) }):
        super().__init__(edge, edge, color)

    def setEdge(self, edge: float = 1) -> None:
        super().__length__ = edge
        super().__width__ = edge
    
    def getEdge(self) -> float:
        return super().__width__ 

    def __repr__(self):
        name = list(super().__color__.keys())[0]
        color = super().__color__[name]
        return "Square [Edge = {}; color = {}|{}]".format(
                self.__length__, name, color)

class Rhombus(Square):
    __smallAngle__ : float = 60
    __bigAngle__: float = 120
    __smallBias__: float = 1
    __smallBias__: float = 2

    def __init__(self, smallAngle: float = ..., bigAngle: float = ..., edge: float = 1,color: dict = { "White": (255, 255, 255)}):
        super().__init__(edge, color)
        self.__smallAngle__  = smallAngle
        self.__bigAngle__ = bigAngle
        self.__caculateBias__(edge, smallAngle, bigAngle)

    def __caculateBias__(self, edge: float = ..., smallAngle: float = ..., bigAngle: float = ...) -> None:
        temp = 2 * edge
        self.__smallBias__ = (1 - cos(radians(smallAngle))) * temp
        self.__bigBias__ = (1 - cos(radians(bigAngle))) * temp
        
    def setAngle(self, small: float = ..., big: float = ...):
        if small == ... and big == ...:
            big = 180

        if small != ... and small > 180 :
            small = 360 - small
        elif small == ...:
            small = 180 - big

        if big != ... and big > 180 :
            big = 260 - big
        elif big == ...:
            big = 180 - big
        self.__smallAngle__ = small
        self.__bigAngle__ = big
    
    def getAngle(self) -> tuple:
        return self.__smallAngle__, self.__bigAngle__

    def area(self) -> float:
        return (1/2) * self.__smallBias__ * self.__bigBias__
    
    def __repr__(self):
        name = list(super().__color__.keys())[0]
        color = super().__color__[name]
        return "Rhombus [Edge = {}, Small Angle = {}, Big Angle = {}, color = {}|{}".format(
            super().__length__, self.__smallAngle__, self.__bigAngle__, name, color)


class Ellipse:
    __smallAxis__: float
    __bigAxis__: float

    def __init__(self, axis: tuple = (..., ...)) -> None:
        smallAxis, bigAxis = min(axis), max(axis)
        self.__bigAxis__ = bigAxis
        self.__smallAxis__ = smallAxis

    def setSmallAxis(self, small: float = 1) -> None:
        self.__smallAxis__ = small
    
    def setBigAxis(self, big: float = 1) -> None:
        self.__bigAxis__ = big

    def getSmallAxis(self) -> float:
        return self.__smallAxis__

    def getBigAxis(self) -> float:
        return self.__bigAxis__
        

    def area(self) -> float:
        return pi * self.__bigAxis__ * self.__smallAxis__ / 4

    def perimeter(self,) -> float:
        a = self.__bigAxis__ / 2
        b = self.__smallAxis__ / 2
        c = (a ** 2 - b ** 2) ** (1 / 2)
        f = lambda x: (1 - (c / a) ** (2) * sin(x) * sin (x)) ** (1 / 2)
        result = integrate.quad(f, 0, pi/ 2) 
        return 4 * a * result[0]

    def __repr__(self) -> str:
        return "Ellipse [Small Axis = {}, Big Axis = {}]".format(self.__smallAxis__, self.__bigAxis__)



        