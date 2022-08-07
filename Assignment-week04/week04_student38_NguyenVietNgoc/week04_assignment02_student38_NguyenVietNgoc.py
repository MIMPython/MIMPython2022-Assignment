import math
class Point:
	def __init__ (self, x, y):
		"""
		Initialie x and y attributes 
			x: length
			y: width
		"""
		self.x = x
		self.y = y
	
	
	def distance(self, x2, y2, metric):
		if metric == "L2":
			return math.sqrt((self.x - x2)**2 + (self.y - y2)**2)	# Euclid distance
		elif metric == "L1":
			return abs(self.x - x2) + abs(self.y - y2)		# Manhattan distance
		else:
			return 
	
	def symmetryPoint(self):
		return (f"Symmetry point of ({self.x},{self.y}): ({self.x * -1},{self.y * -1})")

	def __repr__(self):
		return repr(f"Point: ({self.x},{self.y})")

if __name__ == "__main__":	
	pointA = Point(4,6)
	pointB = Point(3,5)
	distance1 = pointA.distance(pointB.x, pointB.y, "L2")	# 1.4142135623730951
	distance2 = pointA.distance(pointB.x, pointB.y, "L1")	# 2
	print (f"Distance of point A and point B in Eclid: {distance1}")	
	print (f"Distance of point A and point B in Manhattan: {distance2}") 

	print (pointA.symmetryPoint())	# Symmetry point of (4,6): (-4,-6)

	print(repr(Point(3,5)))	# 'Point: (3,5)'

