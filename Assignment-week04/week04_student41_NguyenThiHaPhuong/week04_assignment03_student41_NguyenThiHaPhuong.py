"""(a) Phương trình đường thẳng có dạng y = ax + b với 2 tham số bất kỳ không phải là phương trình tổng quát của 1 đường thẳng trong mặt phẳng 
   Oxy vì phương trình này có vô số nghiệm khi b bằng 0 và khi a = 0, thì phương trình trên trở thành phương trình bậc 0 (b = 0)
   (b) Xét phương trình ax+by+c=0 với a,b,c là ba tham số bất kỳ, trong đó a và b không đồng thời bằng 0, tức là a^2 + b^2 khác 0, là phương 
   trình tổng quát của đường thẳng trong mặt phẳng Oxy"""
from week04_assignment02_student41_NguyenThiHaPhuong import Point

class Line:
	def __init__(self, x1, y1, x2, y2):
		self.x1 = x1
		self.y1 = y1
		self.x2 = x2
		self.y2 = y2

	def __repr__(self):
		return (f'Line(({self.x1!r}, {self.y1!r}), ({self.x2!r}, {self.y2!r}))')

	def get_intersection (self, other):
		# First line represented as a1x + b1y = c1
		a1 = self.y2 - self.y1
		b1 = self.x1 - self.x2
		c1 = a1*(self.x1) + b1*(self.y1) 

		# Second line represented as a2x + b2y = c2
		a2 = other.y2 - other.y1
		b2 = other.x1 - other.x2
		c2 = a2*(other.x1) + b2*(other.y1)

		determinant = a1*b2 - a2*b1

		if (determinant == 0):
			#lying in the same straight line or linear sequence
			return Point(10**9, 10**9)
		if (a1 == a2) and (b1 != b2):
			return Point(0, 0) 
		else: 
			x = (b2*c1 - b1*c2)/determinant
			y = (a1*c2 - a2*c1)/determinant
			return Point(x, y)

	def distance_from_point_to_line (line, point):
		#Line represented as ax + by = c
		a = line.y2 - line.y1
		b = line.x1 - line.x2
		c = a*(line.x1) + b*(line.y1) 

		#Distance from one point to line
		distance = abs(a*point.x + b*point.y - c)/(a*a + b*b)**(1/2)
		return distance

	@classmethod
	def initializeTwoPoints(cls, p1, p2):
		#Creat a Line object by two given points
		return cls(p1.x, p1.y, p2.x, p2.y)

if __name__ == '__main__':
	line1 = Line(-3, 1, -9, -3)
	line2 = Line(-6, 0, -2, 4)
	line = Line(1, 5, 3, 1)
	pointA = Point (3, -4)
	pointB = Point (5, -9)

	intersection_point = Line.get_intersection(line1, line2)
	if (intersection_point.x == 10**9 and intersection_point.y == 10**9):
		print("Two given lines are coincident.")
	else:
		print("The intersection of two given lines is: ")
		print(intersection_point) #Point(-9.0, -3.0)

	print("The distance from point A to line is: ")
	print(Line.distance_from_point_to_line(line, pointA)) #2.23606797749979 or sqrt(5)

	line3 = Line.initializeTwoPoints(pointA, pointB)
	print(line3) #Line((3, -4), (5, -9))
