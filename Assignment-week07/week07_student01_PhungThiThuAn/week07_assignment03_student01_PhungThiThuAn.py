from additionalFolder.shape import Circle, Line, Point

'''
bài toán: đường thẳng có cắt đường tròn không?
Với đường thẳng có dạng: 2x + 3y - 4 = 0
và phương trình đường tròn: (x+3)^2 + (y-2)^2 = 4
'''
line = Line(2, 3, -4)
circle = Circle(Point(-3, 2), 2)
if line.distaneToAPoint(circle.point) < circle.radius:
    print(f'Đường thẳng: {line} cắt đường tròn: {circle} tại hai điểm.')
elif line.distaneToAPoint(circle.point) == circle.radius:
    print(f'Đường thẳng: {line} tiếp xúc đường tròn: {circle}.')
else:
    print(f'Đường thẳng: {line} không cắt đường tròn: {circle}.')

# Đường thẳng: 2x + 3y - 4 = 0 cắt đường tròn: (x + 3)^2 + (y - 2)^2 = 4 tại hai điểm.