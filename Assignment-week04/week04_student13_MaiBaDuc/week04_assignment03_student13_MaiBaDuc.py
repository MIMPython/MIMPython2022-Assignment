'''
Bài tập 3. (class Line)
Xây dựng class Line để biểu diễn các đường thẳng trong mặt phẳng Oxy dựa theo những câu hỏi/yêu cầu dưới đây.

(a) Vì sao phương trình đường thẳng có dạng y=ax+b với a,b là hai tham số bất kỳ 
không phải là phương trình tổng quát của một đường thẳng trong mặt phẳng Oxy? Đường thẳng nào không biểu diễn được qua phương trình này?

(b) Xét phương trình ax+by+c=0 với a,b,c là ba tham số bất kỳ.
Tìm điều kiện của ba tham số a,b,c để phương trình này là phương trình tổng quát của một đường thẳng trong mặt phẳng Oxy.

(c) Phần khởi tạo của class Line có thể được viết như sau

class Line:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
Nhận xét đoạn code trên.

(d) Viết một phương thức trong class Line để xác định (những) giao điểm của hai đường thẳng (nếu có), 
đồng thời tự quyết định kiểu dữ liệu trả về của phương thức này.
(e) Viết một method trong class Line để xác định khoảng cách giữa một điểm và một đường thẳng.
(f) Biết rằng có duy nhất một đường thẳng đi qua hai điểm phân biệt cho trước. 
Viết một method trong class Line để khởi tạo một đường thẳng (là một instance của class Line) 
với tham số đầu vào là hai instance của class Point. Gợi ý: Sử dụng @classmethod
'''
import math
class Line:

    # y=ax+b không phải phương trình tổng quát bởi nó không biểu diễn được đường thẳng x = d
    # để phương trình ax+by+c=0 là pt tổng quát thì cả a và b đều phải khác không

    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
        return None

    def intersection(self, other):
        #su dung phuong phap Cramer
        d = self.a*other.b-other.a*self.b
        dx = self.c*other.b-other.c*self.b
        dy = self.a*other.c-other.a*self.c
        if d==0:
            if dx==0 and dy==0:
                raise ValueError('Infinity roots')
            else:
                raise ValueError('No roots')
        else: 
            x=dx.d
            y=dy/d
            return (x,y)
    point = (1,2)
    def point_line(self, point):
        if self.a*point[0]+self.b*point[1] + self.c ==0:
            return 0
        else:
            result = abs(self.a*point[0]+self.b*point[1] + self.c)/(math.sqrt(self.a**2+self.b**2))
            return result

    @classmethod
    def set_point(cls,x,y):
        cls.x = x
        cls.y = y
        return cls.x, cls.y

    @classmethod
    def line_created(cls, o1, o2):
        if o1[0]==o2[0]:
            return (o1[0],0)
        elif o1[1]==o2[1]:
            return (o1[1],0)
        elif o1[1]!=o2[1] and o1[0]!=o2[0]:
            a_1 = (o1[1] - o2[1])/(o1[0] - o2[0])
            b_1 = o1[1] - a_1*o1[0]
            return (a_1,b_1)
        else:
            return None
    
    def main():
        c = Line.set_point(1,2)
        d = Line.set_point(1,3)
        print(f'y={Line.line_created(c,d)[0]}x+{Line.line_created(c,d)[1]}')

if __name__ == '__main__':
    Line.main()

