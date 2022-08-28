import numpy as np
from time import perf_counter


# ham np.zeros khoi tao 1 array voi cac phan tu deu = 0
t1_start = perf_counter()
zeros_array = np.zeros((4, 5), dtype=int)
t1_end = perf_counter()
time1_executed = t1_end - t1_start


t2_start = perf_counter()
a = []
for i in range(4):
    b = []
    for j in range(5):
        b += [0]
    a += [b]
t2_end = perf_counter()
time2_executed = t2_end - t2_start

print(time1_executed)  # 4.300000000012627e-06

print(time2_executed)  # 6.0000000000060005e-06
