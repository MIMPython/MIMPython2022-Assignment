from random import uniform
import numpy as np
import pandas as pd

print("Bài 4: DataFrame Groupby Tricks")

# name = 'Tùng'
# classed = 'K66A2'
# scored = round(uniform(1, 10), 2)
# print(scored)

name = ["An", "Bình", "Chi", "Dung", "Giang"]
classs = ["K64", "K65", "K65", "K66", "K67"]
score = [7.2, 7.3, 7.4, 7.5, 7.6]

dataframeA = pd.DataFrame({'name': name, 'class': classs, 'score': score})
print(dataframeA)
print()

# Thống kê số điểm sinh viên theo từng lớp
K64 = []
K65 = []
K66 = []
K67 = []
K = []          # Sinh viên thuộc những khóa khác

# Đếm số sinh viên thuộc cùng khóa
d4 = 0
d5 = 0
d6 = 0
d7 = 0
d = 0

for i in range(len(dataframeA)):
    if dataframeA['class'].iloc[i] == "K64":
        K64.append(dataframeA["score"].iloc[i])
        d4 += 1
    elif dataframeA['class'].iloc[i] == "K65":
        K65.append(dataframeA["score"].iloc[i])
        d5 += 1
    elif dataframeA['class'].iloc[i] == "K66":
        K66.append(dataframeA["score"].iloc[i])
        d6 += 1
    elif dataframeA['class'].iloc[i] == "K67":
        K67.append(dataframeA["score"].iloc[i])
        d7 += 1
    else:
        K.append(dataframeA["score"].iloc[i])
        d += 1

# Xử lý dữ liệu từ danh sách
name = ["K64", "K65", "K66", "K67"]
mangD = [d4, d5, d6, d7]
gtTB = [np.mean(K64), np.mean(K65), np.mean(K66), np.mean(K67)]
dataframeB = pd.DataFrame({'class': name, 'nStudent': mangD, 'meanScore': gtTB})
print(dataframeB)