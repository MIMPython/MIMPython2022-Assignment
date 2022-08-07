#a) 
'''
Phương trình đường thằng y = ax + b với a,b bất kì không phải là 
phương trình tổng quát của 1 đường thẳng trong mặt phằng Oxy.
Vì nó không biểu diễn được tất cả các đường thẳng trong mặt phẳng Oxy.
Ví dụ như x = c.
'''
# b)
'''
Điều kiện để phương trình ax + by + c = 0 với a, b, c là ba tham số bất kỳ 
là a ^ 2 + b ^ 2 != 0 (a và b không đồng thời bằng 0).
'''
# c)
class Line:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
'''
Nhận xét nếu đặt tên các thuộc tính là a ,b , c thì sẽ người đọc sẽ không hiểu được 
hết ý nghĩa của 3 thuộc tính này.
'''
    def intersection(self, coefficient):
        self.coefficient = coefficient
        
