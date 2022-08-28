# bai tap 2
'''
Ham mean: Tíng giá trị trung bình cuả các phần tử trong mảng: cả mảng, theo các cột hoặc theo các hàng
argmax: Trả về chỉ số của giá trị lớn nhất trong array: cả array, theo cột hoặc theo hàng
argmin: Giống argmax nhưng là chỉ số của giá trị nhỏ nhất
linespace(start, end, num, endpoint...) hàm giúp tạo ra các số cách đều nhau trong khoảng từ start đến end

Hàm numpy.all
ý nghĩa:
numpy.all([]): kiểm tra xem các phần tử trong array có = True hay không
numpy.all([], axis = 0): kiểm tra xem các phần tử trong cùng một cột có bằng True hay không
numpy.all([], axis = 1): kiểm tra xem các phần tử trong cùng một hàng có bằng True hay không

'''
import time
import numpy as np
from matplotlib import pyplot as plt


def linespaceManual(start, end, num=50, endpoint=True, restep=False):
    listSample = []
    if endpoint:
        part = num - 1
    else:
        part = num
    step = (end - start) / part
    for i in range(0, num):
        listSample.append(start + step*i)
    if restep:
        return (listSample, step)
    else:
        return listSample


if __name__ == '__main__':
    timeLinespaceManual = []
    timeLinespaceNumpy = []
    numberOfSample = [*range(5000, 100000, 500)]
    # startTime = time.time()
    # linespaceManual(0, 10000, num=50000, endpoint=True, restep=True)
    # endTime = time.time()
    # print((endTime - startTime) * 1000)
    for i in range(5000, 100000, 500):
        # time manual
        sumTimeManual = 0
        sumTimeNumpy = 0

        for k in range(0, 11):

            startTimeManual = time.time()
            linespaceManual(0, 100000, num=i, endpoint=True, restep=True)
            endTimeManual = time.time()

            # time numpy linespace
            startTimeNumpy = time.time()
            np.linspace(0, 100000, num=i, endpoint=True, retstep=True)
            endTimeNumpy = time.time()
            sumTimeManual += (endTimeManual - startTimeManual) * 1000
            sumTimeNumpy += (endTimeNumpy - startTimeNumpy) * 1000

        timeLinespaceNumpy.append(sumTimeNumpy / 10)
        timeLinespaceManual.append(sumTimeManual / 10)

    # plot 1
    plt.figure(figsize=(10, 15))  # size figure
    plt.plot(numberOfSample, timeLinespaceManual,
             '-', color='red', label='manual')
    plt.plot(numberOfSample, timeLinespaceNumpy,
             '-', color='blue', label='numpy')
    plt.xlabel('number of sample', fontsize=16)
    plt.ylabel('Time execute', fontsize=16)
    plt.title('Compare time linespace between manual vs numpy')
    plt.legend(fontsize=14)
    plt.grid()
    plt.show()
    # print(linespaceManual(0, 10, num=5, endpoint=False, restep=True))
