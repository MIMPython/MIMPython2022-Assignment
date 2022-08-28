'''
Bài làm tham khảo ở trang: https://numpy.org/doc/stable/reference/generated/ và một số trang khác
- mean, median: Trả về kỳ vọng và trung vị của data nhập vào.
- max, min: Trả về giá trị lớn nhất và bé nhất của data nhập vào.
- argmax, argmin: Trả về chỉ số của giá trị lớn nhất và bé nhất của data nhập vào.
- linspace: Trả về một mảng numpy có chứa các số bắt đầu từ đầu kết thúc trước khi dừng và tăng dần theo số lượng mong muốn phần tử trong mảng.
- arange: Trả về một mảng numpy có chứa các số bắt đầu từ đầu kết thúc trước khi dừng và tăng dần theo sự khác biệt của bước. Vì vậy, các con số nằm trong khoảng thời gian [bắt đầu, dừng lại).
- repeat: Trả về mảng có các giá trị lặp lại giống dữ liệu truyền vào
- random: Trả về mảng numpy với số phần tử bằng số nhập vào và các phần tử nằm trong khoảng từ 0 đến 1
- all: Trả về True khi tất cả các phần tử trong mảng đều True.
- any: Trả về True khi một trong các phần tử trong mảng True.
- ones, zeros: Trả về các mảng toàn giá trị 1 hoặc 0.
- savetxt, loadtxt: Lưu và đọc file txt.
- apply_along_axis: sử dụng 1 hàm theo axis
- where: trả về mảng giữ nguyên những giá trị thỏa mãn và thay đổi những giá trị ko thỏa mãn điều kiện.
- isclose: trả về 1 mảng bool về sự trùng khớp của 2 mảng được nhập vào.
- polyfit: trả về đa thức bình phương nhỏ nhất phù hợp.
- polyval: tính giá trị đa thức
- roots: trả về nghiệm đa thức
'''
import numpy as np

data = np.asarray([2, 4, 9, 6, 0])
print(np.mean(data), np.median(data)) # 4.2 4.0
print(np.max(data), np.min(data)) # 9 0
print(np.argmax(data), np.argmin(data)) # 2 4
print(np.linspace(1, 10, 10, endpoint=True)) # [ 1.  2.  3.  4.  5.  6.  7.  8.  9. 10.]
print(np.arange(1, 11, 1)) # [ 1  2  3  4  5  6  7  8  9 10]
print(np.repeat(data, 2)) # [2 2 4 4 9 9 6 6 0 0]
print(np.random.random(3)) # [0.09461815 0.33576429 0.90162888]
print(np.all(data)) # False
print(np.any(data)) # True
print(np.zeros((2,3))) # [[0. 0. 0.] [0. 0. 0.]]
print(np.ones(2)) # [1. 1.]
np.savetxt('additionalFolder/ex2.txt', data)
print(np.loadtxt('additionalFolder/ex2.txt')) # [2. 4. 9. 6. 0.]
print(np.where(data < 4,data, 5*data)) # [ 2 20 45 30  0]
x = np.array([0.0, 1.0, 5.0, 3.0,  4.0,  5.0])
y = np.array([0.0, 0.8, 0.9, 7.1, -0.8, -1.0])
z = np.polyfit(x, y, 3)
print(z) # [ 0.00528194 -0.78715203  3.82576731 -0.64111349]
print(np.polyval([3,-1,1], 2))  # 11
print(np.roots([1, -4, 4])) # [2.+1.3377935e-08j 2.-1.3377935e-08j]