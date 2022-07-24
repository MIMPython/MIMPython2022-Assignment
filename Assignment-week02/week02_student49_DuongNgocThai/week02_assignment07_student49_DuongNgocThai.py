#bai7
import string
A = list(string.ascii_uppercase)
s = str(input("String: "))
lst = list(s.upper())

def encode():
    i=0
    for i1 in lst:
        for i2 in A:
            if (i2==i1):
                key = A.index(i1)
                if (key<=12):
                    lst[i] = A[key+13]
                else:
                    lst[i] = A[key+13-26]
        i += 1
    print(lst)

def decode():
    i=0
    for i1 in lst:
        for i2 in A:
            if (i2==i1):
                key = A.index(i1)
                if (key<=12):
                    lst[i] = A[key+26-13]
                else:
                    lst[i] = A[key-13]
        i += 1
    print(lst)