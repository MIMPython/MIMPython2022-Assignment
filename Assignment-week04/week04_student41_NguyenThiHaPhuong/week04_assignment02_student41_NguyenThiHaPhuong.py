class Point:
	def __init__(self, x, y):
		self.x = x
		self.y = y
		return None

	def distance(self, other, metric):
		dx = self.x - other.x
		dy = self.y - other.y
		if metric == 'L1': #The Manhattan distance
			return abs(dx) + abs(dy)
		if metric == 'L2': #The Euclid distance
			return (dx**2 + dy**2)**(1/2)

	#Method for the point symmetry
	def point_symmetry(self):
		new_x = - self.x
		new_y = - self.y
		return Point(new_x, new_y)

	# Method used to display X and Y coordinates
    # of a point
	def __repr__(self):
	    return (f'Point({self.x!r}, '
	    	    f'{self.y!r})')	

if __name__ == '__main__':
	pointA = Point(2, 5)
	pointB = Point(20, 8)
	print("The coordinates of point A is: ")
	print(pointA) #Point(2, 5)
	print("The coordinates of point B is: ")
	print(pointB) #Point(20, 8)

	distance_AB = pointA.distance(pointB, 'L2')
	print(f"The distance between point A and point B is {distance_AB}") #18.24828759089466

	pointC = pointA.point_symmetry()
	print("The coordinates of point symmetry of point A is: ")
	print(pointC) #Point(-2, -5)

	