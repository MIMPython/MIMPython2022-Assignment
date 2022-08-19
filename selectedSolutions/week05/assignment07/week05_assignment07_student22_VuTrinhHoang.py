import math
def checkPalindrome(x):
    numIn=x
    temp=numIn
    numOut=0
    while(temp>0):
        numOut+=temp%10
        temp//=10
        numOut*=10
    numOut//=10
    if(numIn==numOut):
        return 1
    return 0

# def checkSquare(x):
#     if int(math.sqrt(x))*int(math.sqrt(x))==x:
#         return 1
#     return 0
def checkPalinSquare(x):
    if int(math.sqrt(x))*int(math.sqrt(x))==x:
       if checkPalindrome(x) == 1:
           return 1
    return 0

ans=0
LIMIT = 1000000001
for i in range(LIMIT):
    if(checkPalinSquare(i)) :
        ans+=1
        print(i)
print(ans)
"""
sau khi print các số Palindrome & Perfect Square thì ta nhận thấy luôn xuất hiện các số có dạng 10...020...01 (với n số 0 ở mỗi bên của 2)
Và các số này đều là bình phương của các số có dạng 10..01 (với n số 0)
Vậy ta có thể suy ra số các số Palindrome & Perfect Square là vô hạn
"""