from math import floor
#Ta sử dụng tính chất sau để tìm ước nguyên tố của một số nguyên b cho trước:
#Nếu b không phải là một số nguyên tố thì p sẽ có ước nguyên tố nhỏ hơn sqrt(b)

def smallest_prime_factor(x):
    P = []
    for i in range(2, floor(x**(0.5)) + 1 ):
        if x%i == 0:
            P.append(i)
    if P == []:
        return(x)
    else:
        return(P[0])

b = 600851475143
while smallest_prime_factor(b) != b:
    b = b/smallest_prime_factor(b)

print(b)