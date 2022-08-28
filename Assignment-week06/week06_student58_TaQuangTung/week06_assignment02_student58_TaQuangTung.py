print("Bài 2: Numpy Methods")

"""
NẾU Ý NGHĨA CÁC HÀM VÀ CHO VÍ DỤ    
- mean: tìm giá trị trung bình
    numpy.mean(a, axis=None, dtype=None, out=None, keepdims=<no value>, *, where=<no value>)
- median: tìm giá trị trung vị
    numpy.median(a, axis=None, out=None, overwrite_input=False, keepdims=False)
- max, min: tìm GTLN và GTNN
    ndarray.max(axis=None, out=None, keepdims=False, initial=<no value>, where=True)
    ndarray.min(axis=None, out=None, keepdims=False, initial=<no value>, where=True)
- argmax, argmin: đối số của giá trị cực đại, cực tiểu
    numpy.argmax(a, axis=None, out=None, *, keepdims=<no value>)
    numpy.argmin(a, axis=None, out=None, *, keepdims=<no value>)
- linspace: truyền số lượng mẫu thay vì kích thước
    np.linspace(start, stop, num=50, endpoint=True, retstep=False)
- arange: tạo ra một mảng có khoảng cách đều nhau nhất định
    np.arange([start,] stop[, step,], dtype=None)
- repeat: lặp lại các phần tử của mảng
    numpy.repeat(a, repeats, axis=None)
- random: lấy giá trị ngẫu nhiên
    np.random.rand(row,column)
- all: kiểm tra xem tất cả các phần tử mảng dọc theo trục được đề cập có đánh giá
    numpy.all(a, axis=None, out=None, keepdims=<no value>, *, where=<no value>)
- any: kiểm tra xem một vài phần tử mảng dọc theo trục được đề cập có đánh giá
    numpy.any(a, axis=None, out=None, keepdims=<no value>, *, where=<no value>)
- ones, zeros: ma trận toàn các số 1 hoặc 0
    np.ones((row, column), dtype = int)
    np.zeros((row, column), dtype = int)
- savetxt: lưu trữ mảng vào file txt
    numpy.savetxt(fname, X, fmt='%.18e', delimiter=' ', newline='\n', header='', footer='', comments='# ', encoding=None)
- loadtxt: tải dữ liệu từ file txt
    numpy.loadtxt(fname, dtype=<class 'float'>, comments='#', delimiter=None, converters=None, skiprows=0, usecols=None, unpack=False, ndmin=0, encoding='bytes', max_rows=None, *, quotechar=None, like=None)
- where: trả về phần tử được chọn dựa trên điều kiện
    numpy.where(condition, [x, y, ]/)
- polyfit: đa thức bình phương phù hợp
    numpy.polyfit(x, y, deg, rcond=None, full=False, w=None, cov=False)
- polyval: tính toán đa thức dựa trên giá trị cụ thể
    numpy.polyval(p, x)
- roots: trả về nghiệm nguyên của một đa thức với hệ số đã cho
    numpy.roots(p)
"""

#Ví dụ minh họa về tạo ma trận 0 cỡ mxn
import numpy as np
from time import perf_counter
m = int(input("Nhập số hàng của ma trận: "))
n = int(input("Nhập số cột của ma trận: "))

#Cách 1: Phương pháp thủ công
start1 = perf_counter()
lst = []
for i in range(m):
    lt = []
    for j in range(n):
        lt.append(0)
    lst.append(lt)
print(f"Ma trận 0 cỡ {m}x{n} thủ công là:")
print(lst)
end1 = perf_counter()
print()

#Cách 2: Phương pháp thư viện
start2 = perf_counter()
zeroArr = np.zeros((m,n), dtype = int)
print(f"Ma trận 0 cỡ {m}x{n} thư viện là:")
print(zeroArr)
end2 = perf_counter()
print()


#So sánh tốc độ thực thi giữa hai phương pháp thủ công và thư viện
print("Tốc độ chạy theo cách thủ công là:", end1 - start1)
print("Tốc độ chạy theo cách thư viện là:", end2 - start2)
