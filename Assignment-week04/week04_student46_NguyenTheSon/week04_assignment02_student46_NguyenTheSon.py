import math
# 1,2)
class Point:
    def __init__(self, x_cordinate, y_coordinate):
        self.x_coordinate = x_cordinate
        self.y_coordinate = y_coordinate
        
    def distance(self, other_point):
        self.other_point = other_point
        distance_euclid = math.sqrt((self.other_point.x_coordinate - self.x_coordinate) ** 2 + (self.other_point.y_coordinate - self.y_coordinate) ** 2)
        return distance_euclid
if __name__ == '__main__':        
    point_A = Point(8, 8)
    point_B = Point(3, 4)
    print(point_A)  
    print(point_B)
    print(point_A.distance(point_B))
#3,4)
class Point:
    def __init__(self, x_cordinate, y_coordinate):
        self.x_coordinate = x_cordinate
        self.y_coordinate = y_coordinate
    def __str__(self):
        return f"{self.x_cordinate}, {self.y_coordinate}"   
    def distance(self, other_point, metric = 'L2'):
        self.other_point = other_point
        self.metric = metric
        if self.metric.upper() == 'L2':
            distance_Euclid = math.sqrt((self.other_point.x_coordinate - self.x_coordinate) ** 2 + (self.other_point.y_coordinate - self.y_coordinate) ** 2)
            return distance_euclid
        elif self.metric.upper() == 'L1':
            distance_Manhattan = abs(self.other_point.x_coordinate - self.x_coordinate) + abs(self.other_point.y_coordinate - self.y_coordinate) 
            return distance_Manhattan



point_A = Point(8, 8)
point_B = Point(3, 4)
print(point_A.distance(point_B, 'L1'))








