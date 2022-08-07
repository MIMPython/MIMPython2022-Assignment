# Bài 9

n = int(input("n = "))
factorialn = 1
for i in range(1,n+1):
    factorialn *= i
print("n! =",factorialn)

b = list(str(factorialn))
c = 0
for i in range(len(b)-1,-1,-1):
    if b[i] == '0':
        c += 1
    else:
        break
print("Số chữ số 0 ở tận cùng bên phải là",c)