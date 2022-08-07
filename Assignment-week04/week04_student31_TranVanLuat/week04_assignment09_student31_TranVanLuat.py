#Cho n là một số tự nhiên, ta định nghĩa n! là tích của n số nguyên dương đầu tiên với quy ước 0!=1. Ví dụ 5!=120.
#a) Hỏi n! có bao nhiêu chữ số 0 ở tận cùng bên phải?
#b) Tạo một số mới bằng cách bỏ tất cả chữ số 0 ở tận cùng bên phải của n!. Hỏi chữ số tận cùng bên phải của số mới này bằng bao nhiêu?


def countZeroNumber(n):
    result = 0
    if n < 5: return result
    #Để n! có số 0 ở cuối thì bắt buộc tối thiểu phải có 1 lần xuất hiện tích của 2 và 5 do đó ở đây ta bắt đầu xuất phát từ 5 tương ứng 5!
    i = 5
    while i <= n:
        temp = i
        while(temp % 5 == 0):
            result += 1
            temp /= 5
        i += 5
    return result

def newFactorial(n, zeroNumber):
    newNum = n / (10**zeroNumber)
    return int(newNum)
        
    
def factorial(n):
    if n == 0: return 1
    result = 1
    elem = 2
    while elem <= n:
        result *= elem
        elem += 1
    return result


if __name__ == '__main__':
    n = int(input("Input n: "))
    while n < 0:
        n = int(input("Input n: "))
    factorialOfN = factorial(n)
    print(f'The factorial of {n} is: {factorialOfN}')
    zeroNumber = countZeroNumber(n)
    print(f'There are {zeroNumber} zero numbers in the end of {n}!') 
    newNum = str(newFactorial(factorialOfN, zeroNumber))
    print(f'The new result, which is deleted 0 in the end: {newNum} and the last number of it is: {newNum[len(newNum)-1]}') 


    
    
    