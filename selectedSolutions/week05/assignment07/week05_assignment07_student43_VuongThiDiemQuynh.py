'''
Bài tập 7. (palindrome number)
Số xuôi ngược là một số tự nhiên không thay đổi khi được viết theo chiều ngược lại. Có tồn tại vô hạn số xuôi ngược đồng thời là một số chính phương hay không?
'''
import numpy
def isPalindromeNumber(n):
    temp = n
    reversedNumber = 0
    while temp > 0:
        reversedNumber = (reversedNumber * 10) + (temp % 10)
        temp = temp // 10
    return reversedNumber == n

def isSquareNumber(n):
    for i in range(1,n):
        if n == i**2:
            return True

def isPalindromeAndSquareNumber(n):
    if isPalindromeNumber(n) and isSquareNumber(n):
        return n

def countPalindromeAndSquareNumber(start, end):
    start, end = int(start), int(end)
    count = 0
    for i in range(start, end):
        if isPalindromeAndSquareNumber(i):
            count += 1
    return count

if __name__ == '__main__':
    print(countPalindromeAndSquareNumber(4,1000)) # 5
    print(countPalindromeAndSquareNumber(1000, 100000)) # 7
    # print(countPalindromeAndSquareNumber(1,numpy.inf)) # Mình định chạy từ 1 -> vô cùng để thử nhưng không được do inf là float 

# Có tồn tại vô hạn số xuôi ngược đồng thời là một số chính phương
