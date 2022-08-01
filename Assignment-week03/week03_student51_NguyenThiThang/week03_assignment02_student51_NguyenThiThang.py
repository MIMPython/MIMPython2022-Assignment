import re
from unittest import result


def largeSum(a,b):
    result=""
    nho = 0
    if (a<b):
        t=a
        a=b
        b=t
    while (len(a) != 0):
        if (len(b) !=0):
            x= int(a[len(a)-1]) + int(b[len(b)-1])
        else:
            x= int(a[len(a)-1])

        result = str((x+nho)%10) + result
        if (x>9):
            nho = x // 10
        else:
            nho=0
        a=a[:-1]
        b=b[:-1]
    return result

if __name__=='__main__':
    path = '.\Desktop\python\cacSo.txt' # copy cach so trong de bai vao file cacSo.txt
    with open(path,'r') as f:
        allNumbers = f.read().splitlines()
    
    sum=allNumbers[0]
    for i in range(1,len(allNumbers)):
        sum = largeSum(allNumbers[i],sum)
    
    print(sum) # tong cua cac so
    for i in range(10):
        print(sum[i],end="") # 10 chu so dau
 
    




