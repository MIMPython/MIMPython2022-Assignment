import numpy as np
import time
# Bài 10:


def det_matrix(array):
    if np.shape(array) == (1, 1):
        return array[0][0]
    else:    
        det = 0
        for row in range(len(array)):
            for column in range(len(array[0])):
                if row == 0:
                    array_del = np.delete(np.delete(array, 0, axis = 0), column, axis = 1)
                    det += (- 1) ** (row + column) * array[0][column] * det_matrix(array_del)
        return det 

if __name__ == "__main__":
    list_time_calc_det = []
    list_time_calc_det_by_numpy = []
    result_det = []
    result_det_by_numpy = []

    for i in range(5, 11):
        array = np.random.randint(1, 10, (i, i))
        start_1 = time.time()
        det = det_matrix(array)
        end_1 = time.time()
        list_time_calc_det.append(end_1 - start_1)
        result_det.append(det)

        start_2 = time.time()
        det_by_numpy = np.linalg.det(array)
        end_2 = time.time()
        list_time_calc_det_by_numpy.append(end_2 - start_2)
        result_det_by_numpy.append(det_by_numpy)
    print("-" * 80)
    print("|" + "time for calculate".center(20) +  "|" + "time for calculator".center(20) + \
            "|" + "result calculate".center(20) + "|" + "result calculate by numpy".center(25), "|")
    for i in range(len(result_det)):
        print("|{: <19f}".format(list_time_calc_det[i]), "|{: <19f}".format(list_time_calc_det_by_numpy[i]), \
            "|{: <19f}".format(result_det[i]), "|{: <25f}".format(result_det_by_numpy[i]), "|")
    print("-" * 80)
        