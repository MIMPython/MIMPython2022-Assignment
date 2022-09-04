from typing_extensions import Self


class Point:
    __x__: float = 0.0
    __y__: float = 0.0

    def __init__(self,cdn: tuple = (0.0, 0.0)):
        self.__x__ ,self.__y__ = cdn
    
    def setCoordinate(self,cdn: tuple = (0.0, 0.0) ):
        self.__x__ ,self.__y__ = cdn

    def getCoordinate(self):
        return self.__x__, self.__y__

    def __sub__(self, other: Self) -> Self:
        x1, y1 = self.__x__, self.__y__
        x2, y2 = other.getCoordinate() 
        return (x2 - x1, y2 - y1)

    def distance(self, other: Self):
       x1, y1 = self.__x__, self.__y__
       x2, y2 = other.getCoordinate() 
       return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** (1 / 2)

    def __repr__(self) -> str:
        return "({}; {})".format(self.__x__, self.__y__)
