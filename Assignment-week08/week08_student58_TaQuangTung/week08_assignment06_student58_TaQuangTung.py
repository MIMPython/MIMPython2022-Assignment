print("Longest Collatz Sequence")

"""
Chuỗi lặp sau được xác định cho tập hợp các số nguyên dương:
n → n/2 (n chẵn)
n → 3n + 1 (n lẻ)
"""
lst = []
for n in range(999999, 0, -1):
    ln = []
    for i in range(n):
        if n % 2 == 0:
            n /= 2
            ln.append(n)
        else:
            n = 3*n + 1
            ln.append(n)

        if n == 1:
            break 
    lst.append(len(ln))

gtln = max(lst)
ind = lst.index(gtln)
print(999999-ind)           # 837799
