from cmath import sqrt

n=14
x=int(sqrt(n).real+1)

def countDigit(k):
        count = 0
        while k != 0:
            k //= 10
            count += 1
        return count

def spiral(x):
    matrix = [[0 for i in range(x)] for j in range(x)]
    a=x**2
    u=k=0
    v=p=x-1
    while (a>0):
        for i in range(u,v+1):
            matrix[i][p] = a
            a -= 1
        v -= 1
        for i in range(v,u-1,-1):
            matrix[p][i] = a
            a -= 1
        for i in range(v,u-1,-1):
            matrix[i][k] = a
            a -= 1
        u += 1
        for i in range(u,v+1,1):
            matrix[k][i] = a
            a -= 1
        p -= 1
        k += 1

    for i in range(0,x):
        for j in range(0,x):
            if matrix[i][j] > n:
                matrix[i][j] = " "
            
    return matrix

matrix = spiral(x)

n_digit=countDigit(n)

for i in range(0,x):
    for j in range(0,x):
        if isinstance(matrix[i][j], int)==True:
            if countDigit(matrix[i][j])<n_digit:
                k_1 = n_digit-countDigit(matrix[i][j])
                matrix[i][j] = str(matrix[i][j])
                matrix[i][j] = ' '*k_1 + matrix[i][j]

for i in range(0,x):
    for j in range(0,x):
        print(matrix[i][j], end=" ")
    print('\n')