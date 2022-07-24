print("Bài 8: Viết chương trình in ra các tam giác")
print()

print("1. Half Pyramid")
n = int(input("Nhập cạnh tam giác: "))
for i in range(1,n+1):
    print("*"*i)
print()

print("2. Inverted Half Pyramid")
n = int(input("Nhập cạnh tam giác: "))
for i in range(n, 0, -1):
    print("*"*i)
print()

print("3. Hollow Inverted Half Pyramid")
n = int(input("Nhập cạnh tam giác: "))
for i in range(n, 0, -1):
    if i == n or i == 1 or i == 2:
        print("*"*i)
    else:
        print("*" + " "*(i-2) + "*")
print()

print("4. Full Pyramid")
n = int(input("Nhập cạnh tam giác: "))
for i in range(1, n+1):
    print(" "*(n-i) + " *"*i)
print()

print("5. Inverted Full Pyramid")
n = int(input("Nhập cạnh tam giác: "))
for i in range(n, 0, -1):
    print(" "*(n-i) + " *"*i)
print()

print("6. Hollow Full Pyramid")
n = int(input("Nhập cạnh tam giác: "))
for i in range(1, n+1):
    if i == n or i == 1 or i == 2:
        print(" "*(n-i) + " *"*i)
    else:
        print(" "*(n-i) + " *" + " "*(2*i-3) + "*")
