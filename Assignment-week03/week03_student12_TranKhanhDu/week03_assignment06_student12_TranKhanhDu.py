#function that calculate gcd of a and b
def cal_gcd(a, b):
    if a > b:
        remainder = a % b
        while remainder != 0 :
            a = b
            b = remainder
            remainder = a % b
        return b
    elif a == b:
        return b
    else: 
        remainder = b % a
        while remainder != 0:
            b = a
            a = remainder
            remainder = b % a
        return a

#test function
print(cal_gcd(150, 50))
print(cal_gcd(50, 175))
print(cal_gcd(100, 100))

#calulate probablity of coprime of two intergers
count = 0
for i in range(2, 1000):
    for j in range(i + 1, 1000):
        if cal_gcd(i, j) == 1:
            count += 1
probablity = count/(10**12)
print(str(probablity))

#1000000 is an enormous number, so my computer can't calculate 
#the coprime probablity of two numbers in 1000000 numberss
          

