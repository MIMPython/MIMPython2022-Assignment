from additionalFolder import Point, Line, Circle

pointA = Point(1, 3)
pointB = Point(4, 2)
lineD = Line.lineFromPoints(pointA, pointB)
circleC = Circle(Point(0, 0), 5)
print (lineD.getDistance(circleC.center))
print (circleC.getArea())