#import itertools
import math
import random

def getGCD(a, b): #Hàm tính UCLN
    if a < b:
        a, b = b, a
    while b != 0:
        r = a % b
        a = b
        b = r
    return a

def main():
    
    # Đếm số cặp số nguyên tố cùng nhau trong tất cả cặp số có thể chọn được từ tập số đã cho. (Runtime lâu quá nên bỏ :>> )
    # N = 10**6 
    # numberOfCoPrimes = 0
    # combinationList = list(itertools.combinations(list(range(1, N+1)), 2))
    # numberOfCombinations = len(combinationList)
    # for element in combinationList:
    #     if getGCD(element[0], element[1]) == 1:
    #         numberOfCoPrimes += 1
    # P = numberOfCoPrimes/numberOfCombinations
    # print (P)
    
    #Lấy ngẫu nhiên hai số trong tập hợp đã cho rồi kiểm tra tính nguyên tố cùng nhau của chúng.
    N = 10**6
    count = 0
    for i in range(10**5): #Lấy ngẫu nhiên 10^5 lần
        temp = random.sample(range(N), 2) #sinh ngẫu nhiên cặp 2 số nguyên dương khác nhau < N
        if getGCD(temp[0], temp[1]) == 1: #Kiểm tra xem 2 số có nguyên tố cùng nhau
            count += 1
    P = count/10**5
    print (P)

if __name__ == "__main__":
    main()