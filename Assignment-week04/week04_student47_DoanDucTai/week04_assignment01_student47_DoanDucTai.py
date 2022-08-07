#bài 1. Viết một chương trình sắp xếp list này theo thứ tự tăng dẫn của 
# tổng các số trong mỗi list con.
b = type("")
A = [[1, 2], [3, 0, 4], [2], [4, 5, 'a'],["a", "b"]]
for i in range( len(A)):
    sumi = 0
    for h in A[i]:
        if (type(h) != b):
            sumi += float(h)

    for j in range(i + 1, len(A)):
        sumj = 0
        for k in A[j]:
            if (type(k) != b):
                sumj += float(k)
        if (sumi > sumj):
            B = A[i]
            A[i] = A[j]
            A[j] = B

print(A)
