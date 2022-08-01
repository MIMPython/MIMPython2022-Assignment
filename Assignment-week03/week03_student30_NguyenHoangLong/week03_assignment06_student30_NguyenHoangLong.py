import itertools
#a)



def gcd(a,b):
    c = [a, b]
    x = a
    y = b
    
    while  a%b != 0:
        
        a = c[1]
        b = c[0]%c[1]
        c = [a, b]
    return(b)

#b)
#Cách 2: Xét tất cả các cặp có thể


N = 10**6

S = []
for i in range(1, N + 1):
    S += [(i,j) for j in range(i, N + 1)]

t = 0

for i in S:
    if gcd(i[0], i[1]) == 1:
        t += 1

P = t/(N*(N + 1)/2)
print(P)


#c) P xấp xỉ 6/pi^2
