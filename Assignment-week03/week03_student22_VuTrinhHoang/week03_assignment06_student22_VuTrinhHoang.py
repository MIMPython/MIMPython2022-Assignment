from ast import Num
import random
import array as arr
# # a)
# a=int(input())
# b=int(input())
# GCD=0
# while(a!=b):
#     if a<b:
#         b=b-a
#     else:
#         a=a-b
# GCD=a
# print(GCD)
# # b)
def check(a,b):
    if(a==b&a!=1):
        return 0
    GCD=0
    while(a!=b):
        if a<b:
            b=b-a
        else:
            a=a-b
    GCD=a
    if a==1:
        return 1
    else:
        return 0
count = 0
Numbers= arr.array('i',[1,2,3,4,5,6,7,8,9])
for i in Numbers:
    for j in Numbers:
        if check(i,j)==1:
            count +=1
P=count/ (len(Numbers)*len(Numbers))*100
print(P)
# c)
# theo như em tìm hiểu trên mạng thì có a=6, b=2
# Vậy xác suất để hai số tự nhiên bất kì thuộc khoảng [1,10^6] nguyên tố cùng nhau sẽ rơi vào khoảng 58%-60%. Và xác suất đó
# sấp sỉ bằng 6/(pi^2)