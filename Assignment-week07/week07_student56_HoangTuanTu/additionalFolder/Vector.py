from typing_extensions import Self
from Point import Point

class Vector:
    __fpoint__: Point = (0, 0)
    __lPoint__: Point = (0, 0)
    __vec__: tuple = (0.0, 0.0)

    def __init__(self, alpha: tuple = (1, 1), beta: tuple = (0, 0)):
        self.__fpoint__ = Point(alpha)
        self.__lPoint__ = Point(beta)
        self.__vec__ = Point(alpha) - Point(beta)

    def setPoint(self, alpha: Point = ..., beta: Point = ...):
        if beta != ...:
            self.__lPoint__ = beta
        if alpha != ...:
            self.__fpoint__ = alpha
        if beta == ... and alpha == ...:
            self.__fpoint__: Point = Point((0, 0))
            self.__lPoint__: Point = Point((0, 0))
        self.__vec__ = self.__fpoint__ - self.__lPoint__

    def getVec(self):
        return self.__vec__

    def __sub__(self, other: Self) -> list:
        fVec = self.__vec__
        lVec = other.getVec()
        return Vector((lVec[0] - fVec[0], lVec[1] - fVec[1] ))

    def __add__(self, other: Self) -> list:
        fVec = self.__vec__
        lVec = other.getVec()
        return Vector((lVec[0] + fVec[0], lVec[1] + fVec[1]))

    def __neg__(self):
        return Vector(( - self.__vec__[0], - self.__vec__[1]))

    def __repr__(self) -> str:
        return "[{} ; {}]".format(self.__vec__[0], self.__vec__[1])

