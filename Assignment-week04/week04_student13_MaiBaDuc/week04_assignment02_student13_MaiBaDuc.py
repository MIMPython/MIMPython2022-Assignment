import math 
class Point: 
    def __init__(self,x,y):
        self.x = x
        self.y = y
        return None

    def distance(self, other, metric):
        if metric == 'L2':
            x_1 = self.x - other.x
            y_1 = self.y - other.y
            return (x_1**2 + y_1**2)**0.5
        else: 
            x_1 = abs(self.x-other.x)
            y_1 = abs(self.y-other.y)
            return x_1+y_1
            
    def get_A_1(self): #nhận giá trị đối xứng qua tâm
        return -self.x, -self.y
    def __repr__(self):
        rep = 'Abscissa: ' + str(self.x) + ' Ordinate: ' + str(self.y)
        return rep

    def main():
        p1 = Point(10,4)
        p2 = Point(3,1)
        print(Point.distance(p1,p2, 'L2'))  
    
if __name__ == '__main__':
    Point.main()


