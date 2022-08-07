from week04_assignment02_student41_NguyenThiHaPhuong import Point
from week04_assignment03_student41_NguyenThiHaPhuong import Line

class Triangle(object):
	def __init__(self, pA, pB, pC):
		self.pA = pA
		self.pB = pB 
		self.pC = pC 
		self.lineBC = Line.initializeTwoPoints(pB, pC)
		self.base = Point.distance(pointB, pointC, 'L2')
		self.height = Line.distance_from_point_to_line(self.lineBC, pA)

	def get_triangle_area(self):
		triangle_area = (int) ((1/2)*self.base*self.height)
		return triangle_area

if __name__ == '__main__':
	pointA = Point(0, 5)
	pointB = Point(0, 0)
	pointC = Point(8, 0)

	triangleABC_area = Triangle(pointA, pointB, pointC).get_triangle_area()
	print(f"The area of the triangle is {triangleABC_area}") #20
