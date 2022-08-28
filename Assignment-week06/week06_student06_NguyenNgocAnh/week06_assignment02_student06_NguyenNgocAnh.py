import numpy as np

"""
mean(arr, axis): tính trung bình cộng của arr
axis = 0: dọc
axis = 1: ngang
cách làm thủ công => dùng vòng for
"""
arr = np.array([6, 2, 6, 9, 3, 7, 2, 12, 26, 7, 3, 11, 11, 6, 13, 29, 1])

print(np.mean(arr))

"""
median(arr, axis): tìm trung vị
axis = 0: dọc
axis = 1: ngang
"""
print(np.median(arr))

"""
max(arr, axis): tìm giá trị lớn nhất dọc theo trục đã cho
min(arr, axis): tìm giá trị nhỏ nhất dọc theo trục đã cho
axis = 0: dọc
axis = 1: ngang
"""
print(np.max(arr))
print(np.min(arr))
"""
linspace() trả về một số lượng số cách đều nhau trong khoảng
"""
print(np.linspace(0, 10, 5))
"""
arange() trả về một số lượng số cách đều nhau một khoảng cố định trong khoảng
"""
print(np.arange(0, 10, 2))

"""
argmax, argmin: Trả về chỉ số của các giá trị lớn/nhỏ nhất dọc theo trục.
"""
print(np.argmax(arr))
print(np.argmin(arr))
"""
repeat: Lặp lại các phần tử của mảng
"""
print(np.repeat(arr,2))

#random: Giá trị ngẫu nhiên với kích thước cho trước.
print(np.random.rand(3, 2)) #giá trị chạy trong khoảng [0, 1)
print(np.random.randint(0, 10, (2, 2))) #giá trị chạy trong khoảng [low, high)

#all: kiểm tra tất các phần tử trong arr có True không
print(np.all(arr))
print(np.all([[0, 1], [0, 1]],axis=0))
#any: kiểm tra bất kì phần tử nào trong mảng có True không
print(np.any([0, 0, 0, 0]))
print(np.any([0, 0, 0, 1]))
#ones: trả về mảng có kích thước cho trước toàn 1
#zeros: trả về mảng có kích thước cho trước toàn 0
print(np.ones((3,3)))
print(np.zeros((3, 3)))
#savetxt: lưu mảng dạng txt
np.savetxt('additionalFolder/week06_assignment02_student06_NguyenNgocAnh_savetxt.txt', np.random.randint(0, 20, (10, 10)), fmt='%d')