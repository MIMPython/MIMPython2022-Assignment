#Bài 5
#a
while True:
    a = float(input("a="))
    if a != 0:
        print(a)
        break
#b
A = [0]
for i in A:
    A.append(i+1)
    print(A)
#c
for i in iter(int,7):
    print(i)