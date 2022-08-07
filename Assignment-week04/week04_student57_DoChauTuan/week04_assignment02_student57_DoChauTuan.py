# bai 2

class Point:

  def __init__(self, x: int, y: int):
    self.x_coord = x
    self.y_coord = y

  def distance(self, point, metric: str):
    if metric == 'L1':
      return abs(self.x_coord - point.x_coord) + abs(self.y_coord - point.y_coord)

    if metric == 'L2':
      return ((self.x_coord - point.x_coord) ** 2 + (self.y_coord - point.y_coord) ** 2) ** 0.5

    return 0

  def get_symmetrical_point2(self):
    return Point(-self.x_coord, -self.y_coord)

  def get_symmetrical_point3(self):
    return self.__class__(-self.x_coord, -self.y_coord)


def get_symmetrical_point1(point: Point) -> Point:
  return Point(-point.x_coord, -point.y_coord)




pointA = Point(2, 3)
pointB = Point(1, -6)
print(pointA, pointA.x_coord, pointA.y_coord) # <__main__.Point object at 0x7effee8aff50> 2 3

print(pointB, pointB.x_coord, pointB.y_coord) # <__main__.Point object at 0x7efff10f9150> 1 -6


distL1 = pointA.distance(pointB, metric = 'L1')
distL2 = pointA.distance(pointB, metric = 'L2')

print(distL1) # 10
print(distL2) # 9.055385138137417


sym_pointA1 = get_symmetrical_point1(pointA)
print(sym_pointA1, sym_pointA1.x_coord, sym_pointA1.y_coord) # <__main__.Point object at 0x7effee8afcd0> -2 -3

sym_pointB1 = get_symmetrical_point1(pointB)
print(sym_pointB1, sym_pointB1.x_coord, sym_pointB1.y_coord)  # <__main__.Point object at 0x7effee8af9d0> -1 6


sym_pointA2 = pointA.get_symmetrical_point2()
print(sym_pointA2, sym_pointA2.x_coord, sym_pointA2.y_coord)  # <__main__.Point object at 0x7effee8afe10> -2 -3

sym_pointB2 = pointB.get_symmetrical_point2()
print(sym_pointB2, sym_pointB2.x_coord, sym_pointB2.y_coord)  # <__main__.Point object at 0x7effee8af950> -1 6


sym_pointA3 = pointA.get_symmetrical_point3()
print(sym_pointA3, sym_pointA3.x_coord, sym_pointA3.y_coord)  # <__main__.Point object at 0x7effee8af8d0> -2 -3

sym_pointB3 = pointB.get_symmetrical_point3()
print(sym_pointB3, sym_pointB3.x_coord, sym_pointB3.y_coord)  # <__main__.Point object at 0x7effee8afa50> -1 6
