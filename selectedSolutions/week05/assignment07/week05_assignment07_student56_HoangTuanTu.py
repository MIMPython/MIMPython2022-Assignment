"""
Số xuôi ngược là một số tự nhiên không thay đổi khi được viết theo chiều ngược lại. 
Có tồn tại vô hạn số xuôi ngược đồng thời là một số chính phương hay không?
-> Trả lời: Có tồn tại vô hạn số xuôi ngược và đồng thời là số chính phương
Khi đếm chay thì số lượng số thỏa mãn vẫn sẽ tiếp tục tăng trong thời gian dài
Theo phương pháp toán học xem kỹ hơn trong file SpecialNumber.pdf ở mục addtionalFolder
Có thể thấy số ((10**n)+1)**2 và số (2(10**n)+ 2)**2 đều là số palindrome chính phương có 2n + 1 chữ số
Suy ra tồn tại vô hạn số palindrome chính phương
"""

def palindromeNumber(number):
    if number < 0 : return False
    number = str(number)
    length = len(number)
    for i in range(1,(length//2)+1):
        if number[i-1] != number[-i]:
            return False
    return True

def countNumber():
    index = 0  
    count = 0
    bound = 100000000000000
    while True:
        number = index**2
        if (number>bound):
            print("Have Reach:{} and have {} number valid".format(bound,count))
            bound+= 100000000000000
        if(palindromeNumber(number)):
            count+=1
            print("{} is the {}-th Palindrome Number and Square Number ({})".format(number,count,index))
        index+= 1

def math():
    n = int(input("Input number: "))
    temp = (10**n + 1)**2
    print("Palindrome number:",temp)
    print("Number digit of palendrome number:",len(str(temp)))
    print("square root of Palindrime number:",int(temp**(1/2)))
if __name__ == "__main__":
    math()
