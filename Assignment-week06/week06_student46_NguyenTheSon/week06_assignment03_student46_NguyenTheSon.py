import matplotlib.pyplot as plt


# Bài 3:
class Geometry:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def point(self):
        fig, ax = plt.subplots()
        ax.scatter(self.x, self.y)
        ax.set(xlabel = "trục hoành", ylabel = "trục tung" )
        fig.savefig('D:/MIM_Python/week06_student46_NguyenTheSon/additionalFolder/image_point.svg')
        fig.show()

    def line(self, another_point):
        fig, ax = plt.subplots()
        point_1 = [self.x, another_point.x]
        point_2 = [self.y, another_point.y]
        ax.plot(point_1, point_2)
        fig.savefig('D:/MIM_Python/week06_student46_NguyenTheSon/additionalFolder/image_line.svg')
        fig.show()

    def circle(self, radius):
        fig, ax = plt.subplots()
        ax.scatter(self.x, self.y)
        ax.scatter(self.x, self.y, s = radius * 1000)
        fig.savefig('D:/MIM_Python/week06_student46_NguyenTheSon/additionalFolder/image_circle.svg')
        fig.show()
        
if __name__ == "__main__":
    A = Geometry(14, 7)
    B = Geometry(11, 5)
    A.point()
    B.point()
    A.line(B)
    A.circle(2)
    
