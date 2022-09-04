#Ax + By + C = 0
class line:
    def __init__(self, A, B, C):
        self.A = A
        self.B = B
        self.C = C
    def func(self):
        print(f"{self.A}x + {self.B}y + {self.C} = 0")
line1 = line(A = 3, B = 4, C = 9)
line1.func()