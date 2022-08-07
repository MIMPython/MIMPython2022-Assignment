class Point():
    __x = 0.0
    __y = 0.0

    def __init__(this,x,y):
        this.__x = x
        this.__y = y

    def getX(this)->float:
        return this.__x
        
    def getY(self)->float:
        return self.__y
        
    def setX(self,x):
        self.__x = x
        
    def setY(self,y):
        self.__y = y

    def getXY(self):
        return self.__x,self.__y

    def setXY(self,x,y):
        self.__x,self.__y = map(float, x,y)

    def toString(this):
        return "({} ; {})".format(this.__x,this.__y)

    def __repr__(this):
        return "({} ; {})".format(this.__x,this.__y)

    def distance(self, point2, metric = "L2"):
        x1 = self.__x
        y1 = self.__y
        x2,y2 = map(float,point2.getXY())
        if metric == "L2":
            return ((x2-x1)**2 + (y2-y1)**2)**(1/2)
        return (abs(x1-x2) + abs(y1-y2))

    def symmetricalPoint(self):
        x = self.getX()
        y = self.getY()
        return Point(-x,-y)
    
if __name__ == "__main__":
    point1 = Point(0,0)
    point2 = Point(-1,1)
    print(point2.__repr__())
    print("Eculid distance:",point1.distance(point2,metric="L2"))
    print("Manhattan distance:",point1.distance(point2,metric="L1"))
    print("Symmetrical point of {} is {}".format(point2.toString(),point2.symmetricalPoint()))
            
