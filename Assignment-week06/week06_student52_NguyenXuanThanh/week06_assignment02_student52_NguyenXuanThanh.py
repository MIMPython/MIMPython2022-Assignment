
import numpy as np

data = np.asarray([1, 2, 3])

# mean : Hàm này trả về kỳ vọng của dữ liệu
# median: Hàm này trả về trung vị của dữ liệu
print(np.mean(data))
print(np.median(data))
# max : Hàm này trả về giá trị lớn nhất của dữ liệu
# min : Hàm này trả về giá trị nhỏ nhất của dữ liệu
print(np.max(data), np.min(data))
print(np.min(data))

#argmax: Hàm này trả về chỉ số giá trị lớn nhất của dữ liệu
#argmin: Hàm này trả về chỉ số giá trị bé nhất của dữ liệu
print(np.argmax(data))
print(np.argmin(data))