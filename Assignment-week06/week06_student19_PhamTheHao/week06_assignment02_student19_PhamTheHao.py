"""
Bài tập 2. (numpy methods)

Hãy tìm hiểu một số hàm trong thư viện numpy và thực hiện những yêu cầu sau:
Nêu ý nghĩa của hàm, cho ví dụ.
Viết chương trình thực hiện đúng ý nghĩa đó mà hạn chế sử dụng thư viện numpy. 
Có thể sử dụng thư viện để khởi tạo mảng số nếu cần thiết.
So sánh tốc độ thực thi giữa hai cách làm: phương pháp thủ công và phương pháp sử dụng numpy.
"""

# Hàm mean: trả về giá trị trung bình của các phần tử trong mảng
import time
import numpy as np
a = np.array([1, 2, 3, 4])
a= [1, 2,3, 4]
average = sum(a)/len(a)
print(average)
np.mean(a) # 2.5

# Hàm median: trả về median của mảng
a = np.array([[10, 7, 4], [3, 2, 1]])
np.median(a)

