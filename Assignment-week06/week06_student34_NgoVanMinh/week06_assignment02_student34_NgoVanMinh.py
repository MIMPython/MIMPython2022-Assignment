import numpy as np

if __name__ == '__main__':

    arr = np.array([[1, 2], [3, 10]])

    # np.mean tính trung bình dữ liệu theo chiều xác định
    print(np.mean(arr)) #4.0

    #np.meidan đưa về giá trị trung vị của mảng
    print(np.median(arr))   #2.5

    # np.max trả về giá trị lớn nhất của mảng
    print(np.max(arr))  #10.0

    #np.min trả về giá trị nhỏ nhất của mảng
    print(np.min(arr))  # 1.0

    #np.argmax trả về chỉ số của giá trị lớn nhất của mảng
    print(np.argmax(arr))   #3 chỉ số của 10

    #np.argmin trả về chỉ số của giá trị nhỏ nhất của mảng
    print(np.argmin(arr))   #0 chỉ số của 1

    #np.linspace trả về các giá trị cách đều nhau theo lượng mẫu (num)
    print(np.linspace(1,10,num=10)) #[ 1.  2.  3.  4.  5.  6.  7.  8.  9. 10.]

    #np.arrange trả về các giá trị cách đều nhau theo bước nhảy
    print(np.arange(0, 5, 0.5))     #[0.  0.5 1.  1.5 2.  2.5 3.  3.5 4.  4.5]

    #np.repeat lặp lại toàn bộ các giá trị của mảng theo số lần truyền vào
    print(np.repeat(arr, 2))        #[ 1  1  2  2  3  3 10 10]

    #np.random.rand(m,n) trả về một mảng giá trị ngẫu nhiêu trong khoảng giá trị từ m tới n
    print(np.random.rand(1,2))      #[[0.64624146 0.56326717]]

    #np.ones((m,n)) trả về ma trận cấp m x n chúa toàn các phần tử là 1
    print(np.ones((2,1)))

    #np.zeros((m,n) trả về ma trận cấp m x n chứa toàn bộ phần tử 0
    print(np.zeros((2,1)))