from week04_assignment02_student12_TranKhanhDu import Point
import math
class Line:
    
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        
    
    #câu d
    # def find_section(self, Line):
        if (self.a == 0 and self.b == 0) or (Line.a == 0 and Line.b == 0):
            result = "It’s not a line"
            return result
        
        elif (self.a == 0 and Line.a == 0) :
            if (self.c != 0 and Line.c == 0) or (self.c == 0 and Line.c != 0):
                return "2 Lines is parallel"
            elif self.c == 0 and Line.c == 0:
                return "2 Lines is overlapped"
            elif (self.b/self.c) == (Line.b/Line.c):
                return "2 Lines is overlapped"
            else:
                return "2 Lines is parallel" 
            
        elif (self.b == 0 and Line.b == 0) :
            if (self.c != 0 and Line.c == 0) or (self.c == 0 and Line.c != 0):
                return "2 Lines is parallel"
            elif self.c == 0 and Line.c == 0:
                return "2 Lines is overlapped"
            elif (self.a/self.c) == (Line.a/Line.c):
                return "2 Lines is overlapped"
            else:
                return "2 Lines is parallel"
            
        else:
            if (self.a/self.b == Line.a/Line.b) and (self.a/self.c == Line.a/Line.c) and (self.b != 0 and Line.b != 0):
                return "2 Lines is overlapped."
            elif (self.a/self.b == Line.a/Line.b) and (self.c != Line.c) and (self.b != 0):
                return "2 LInes is parallel. "
            else:
                horizontal_section = (self.c*Line.b-Line.c*self.b)/(self.a*Line.b-Line.a*self.b)
                vertical_section = -1*self.a*horizontal_section - self.c
                return f'{horizontal_section}, {vertical_section}'
    #câu e
    def find_distance(self, Point):
        return (abs(self.a*Point.x + self.b*Point.y + self.c))/(math.sqrt(self.a**2 + self.b**2))
            

LineA = Line(4, 6, 7)
LineB = Line(4, 0, 2)
print(LineA.find_section(LineB))

PointA = Point(4,6,4)
LineA