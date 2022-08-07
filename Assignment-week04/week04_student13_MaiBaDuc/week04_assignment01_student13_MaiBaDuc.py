'''
Bài tập 1. (sort a list)
Một list được gọi là ổn nếu nó chỉ chứa các số thực và có ít nhất một phần tử.
Cho một list gồm các list con ổn. Viết một chương trình sắp xếp list này theo thứ tự tăng dẫn của tổng các số trong mỗi list con. Ví dụ:

A = [[1,2], [3,0,4], [2], [4,5]] # input
B = [[2], [1,2], [3,0,4], [4,5]] # output
Yêu cầu bổ sung: đặt ra thêm tiêu chí để so sánh hai list ổn bất kỳ và áp dụng tiêu chí này để sắp xếp list đầu vào.
'''



import enum
from operator import index, indexOf

#sap xep giam dan
A = [[1,2], [3,0,4], [2], [4,5]]
sum_A = []
for i in A:
    s=0
    for j in i:
        s += j
    sum_A.insert(A.index(i),s)
b = [0,1,2,3]
c = zip(b,sum_A)
c = dict(c)
c = sorted(c.items(), key=lambda x: x[1], reverse=True)
c = dict(c)
b = []
for i in c.keys():
    for j,v in enumerate(A,start=0):
        if i==j:
            b.append(v)

print(b)
