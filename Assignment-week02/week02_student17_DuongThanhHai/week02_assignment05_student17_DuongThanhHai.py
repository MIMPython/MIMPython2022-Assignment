
print ('cau a')
def a():
    A = [70, 43, 7, 46, 34, 77, 80, 35, 49, 3, 1, 5, 53, 3, 53]
    x = A[2]*A[2]
    A[2] = x
    print (A)
a()
print ('cau b')

def b1():
    A = [70, 43, 7, 46, 34, 77, 80, 35, 49, 3, 1, 5, 53, 3, 53]
    A.pop(2)
    print (A)
b1()

def b2():
    A = [70, 43, 7, 46, 34, 77, 80, 35, 49, 3, 1, 5, 53, 3, 53]
    del A[2]
    print (A)
b2()
print('cau c')

def c():
    A = [70, 43, 7, 46, 34, 77, 80, 35, 49, 3, 1, 5, 53, 3, 53]
    x = A[-1]*A[-1]
    A.append(x)
    print (A)
c()
print('cau d')

def d():
    A = [70, 43, 7, 46, 34, 77, 80, 35, 49, 3, 1, 5, 53, 3, 53]
    print (len(A))
d()
print('cau e')

def e():
    A = [70, 43, 7, 46, 34, 77, 80, 35, 49, 3, 1, 5, 53, 3, 53]
    print(sum(A))
e()
print('cau f')

def f():
    A = [70, 43, 7, 46, 34, 77, 80, 35, 49, 3, 1, 5, 53, 3, 53]
    sum = A[1] + A[2] + A[3] + A[5]
    print (sum)
f()
print ('cau g')

def g1():
    A = [70, 43, 7, 46, 34, 77, 80, 35, 49, 3, 1, 5, 53, 3, 53]
    A.reverse()
    print(A)
g1()

def g2():
    A = [70, 43, 7, 46, 34, 77, 80, 35, 49, 3, 1, 5, 53, 3, 53]
    A1=A[:]
    length = len(A)
    i=0
    while i < length:
        A1[i] = A[length-1-i]
        i+=1
    print(A1)
g2()
print ('cau h')

def h():
    A = [70, 43, 7, 46, 34, 77, 80, 35, 49, 3, 1, 5, 53, 3, 53]

    A_even = []
    A_odd = []
    for i in A:
        if i % 2 == 0:
            A_even.append(i)
        else:
            A_odd.append(i)
    print('A_even = ' + str(A_even))
    print('A_odd = ' + str(A_odd))
h()
print ('cau i j k')

def i_j_k():
    A = [70, 43, 7, 46, 34, 77, 80, 35, 49, 3, 1, 5, 53, 3, 53]
    B = A[:]
    B.sort(reverse=True)
    print('B= ' + str(B))

    if len(A) == len(B):
        print("do dai 2 list bang nhau")
    else:
        print("do dai 2 list khong bang nhau")

    C = A + B  
    print('C = ' + str(C))  
i_j_k()    








    