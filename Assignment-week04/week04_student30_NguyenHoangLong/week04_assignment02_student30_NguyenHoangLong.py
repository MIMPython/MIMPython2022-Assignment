"Xây dựng hai hàm tính khoảng cách L1 và L2 của R^2"
def metric_L1(x, y):
    return(abs(x[0] - y[0]) + abs(x[1] - y[1]))

def metric_L2(x, y):
    return(((x[0] - y[0])**2 + (x[1] - y[1])**2)**0.5)

"Định nghĩa class Point"
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    "Tính khoảng cách L2 thông thường"
    def euclidean_distance(self, point):
        return(metric_L2((self.x,self.y), (point.x,point.y)))
    
    "Tính khoảng cách L1 hoặc L2"
    def distance(self, point, metric):
        if metric == 'L1':
            return(metric_L1((self.x,self.y), (point.x,point.y)))
        if metric == 'L2':
            return(metric_L2((self.x,self.y), (point.x,point.y)))

    "Viết điểm đối xứng qua gốc tọa độ"
    def sym(self):
        return(Point(-self.x, -self.y))

    "Bổ sung hàm __repr__() cho class Point"
    def __repr__(self):
        return(f"({self.x}, {self.y})")

"Một vài instance"
point_A = Point(23,12)
point_B = Point(7, 1)

"Khoảng cách L1"
disL1 = point_A.distance(point_B, 'L1')
print(disL1) #27

"Khoảng cách L2"
disL2 = point_A.distance(point_B, 'L2')
print(disL2) #19.4164878389476

"In ra điểm đối xứng với point_A qua gốc tọa độ"
print(repr(point_A.sym())) #(-23, -12)


    




        