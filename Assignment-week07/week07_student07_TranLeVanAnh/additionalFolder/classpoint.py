class point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def func(self):
        pointx = self.x
        pointy = self.y
        print((pointx,pointy))
point1 = point(x=3,y=4)
point1.func()