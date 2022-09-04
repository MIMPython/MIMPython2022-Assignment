print("Bài 6: Langton’s Ant")

"""
Quy tắc mô hình Langton’s ant
+ Tại một hình vuông màu trắng, quay 90° theo chiều kim đồng hồ, lật màu của hình vuông, di chuyển về phía trước một đơn vị
+ Tại một hình vuông màu đen, quay 90° ngược chiều kim đồng hồ, lật màu của hình vuông, di chuyển về phía trước một đơn vị
"""

import turtle

# Hiển thị giao diện màn hình Turtle
DoorAnt = turtle.Screen()
DoorAnt.bgcolor('gray')             # Màu sắc của đồ họa Turtle
DoorAnt.screensize(100,100)

# Khởi tạo đối tượng Kiến Ant
ant = turtle.Turtle() 
ant.shape('circle')                 # Hình dạng của con Kiến Ant

# Khu vực chứa tọa độ màu sắc
lst = {}

# ant.speed()       --> Khởi tạo tốc độ chạy cho con kiến

# Dữ liệu tọa độ của con Kiến Ant
toaDo = (ant.xcor(), ant.ycor())      

# Hàm chuyển đổi màu sắc con kiến Ant
def changeColor(graph, ant, color): 
    # Làm tròn dữ liệu tọa độ dịch chuyển của con kiến Ant
    graph[(round(ant.xcor()), round(ant.ycor()))] = color


# Khởi tạo Hướng đối tượng class cho chương trình
class Langton:
    def __init__(self, ant, toaDo, lst):
        self.ant = ant
        self.toaDo = toaDo
        self. lst = lst
    def lang(self):
        while True:
            step = 20       # Bước dịch chuyển của con kiến

            # Xử lý các trường hợp tại nơi mà con kiến Ant đi qua
            if self.toaDo not in self.lst or self.lst[self.toaDo] == "white":
                (self.ant).fillcolor("black")          # Chuyển đổi màu sắc con kiến
                
                # Chuyển đổi lại màu sắc nơi con kiến đi qua 
                (self.ant).stamp()         # Đóng dấu màu sắc khu vực nơi con kiến đi qua
                changeColor(self.lst, self.ant, "black")     
                
                # Thay đổi vị trí hướng đi của con kiến
                (self.ant).right(90)           # Cho con kiến quay phải góc 90 
                (self.ant).forward(step)       # Tiếp tục dịch chuyển lên phía trước
                
                # Tọa độ của con kiến
                self.toaDo = (round((self.ant).xcor()), round((self.ant).ycor()))          
            
            else:
                (self.ant).fillcolor("white")              # Chuyển đổi màu sắc con kiến
                
                # Chuyển đổi màu sắc nơi mà con kiến đi qua
                (self.ant).stamp()                 # Đóng dấu lại màu sắc
                changeColor(self.lst, self.ant, "white")    
                
                # Thay đổi hướng dịch chuyển của con kiến
                (self.ant).left(90)            
                (self.ant).forward(step) 

                # Tọa độ của con kiến
                self.toaDo = (round((self.ant).xcor()), round((self.ant).ycor()))

# Gọi đối tượng để hiển thị ra chương trình
KienANT = Langton(ant, toaDo, lst)
KienANT.lang()
