from time import perf_counter

print("Bài 5: Filling Missing Digits")

"""
Các số nguyên từ 1 --> 9 vào A, B, C, D, E, F, G, H, I đồng thời khác nhau
--> A + B/C + D + E/F = G + H/I
"""

start1 = perf_counter()

lst = []
for a in range(1, 10):
    for b in range(1, 10):
        for c in range(1, 10):
            for d in range(1, 10):
                for e in range(1, 10):
                    for f in range(1, 10):
                        for g in range(1, 10):
                            for h in range(1, 10):
                                for i in range(1, 10):
                                    if a + b/c + d + e/f == g + h/i:
                                        ln = [a, b, c, d, e, f, g, h, i]
                                        lst.append(ln)

for ele in lst:
    d = set(ele)
    if len(ele) == len(d):
        print(ele)
end1 = perf_counter()

print(end1 - start1)

# Time: 192.5976671000244
"""
[1, 2, 3, 7, 5, 6, 9, 4, 8]
[1, 2, 4, 7, 3, 9, 8, 5, 6]
[1, 2, 4, 8, 7, 6, 9, 5, 3]
[1, 2, 8, 5, 9, 6, 7, 3, 4]
[1, 2, 8, 7, 5, 4, 9, 3, 6]
[1, 2, 8, 7, 6, 3, 9, 5, 4]
[1, 3, 2, 5, 9, 6, 7, 8, 4]
[1, 3, 2, 7, 6, 8, 9, 5, 4]
[1, 3, 4, 7, 6, 8, 5, 9, 2]
[1, 3, 6, 7, 5, 2, 9, 8, 4]
[1, 3, 9, 7, 2, 4, 8, 5, 6]
[1, 3, 9, 7, 4, 6, 5, 8, 2]
[1, 4, 2, 5, 3, 9, 7, 8, 6]
[1, 4, 2, 5, 7, 3, 9, 8, 6]
[1, 4, 6, 7, 3, 9, 5, 8, 2]
[1, 4, 8, 5, 9, 3, 6, 7, 2]
[1, 4, 8, 6, 5, 2, 7, 9, 3]
[1, 4, 8, 7, 5, 2, 9, 6, 3]
[1, 5, 2, 3, 8, 4, 7, 9, 6]
[1, 5, 2, 4, 8, 3, 9, 7, 6]
[1, 5, 2, 6, 4, 8, 7, 9, 3]
[1, 5, 2, 7, 3, 6, 9, 8, 4]
[1, 5, 2, 7, 4, 8, 9, 6, 3]
[1, 5, 4, 7, 2, 8, 9, 3, 6]
[1, 5, 6, 4, 9, 2, 8, 7, 3]
[1, 5, 6, 7, 2, 3, 9, 4, 8]
[1, 6, 3, 7, 2, 8, 9, 5, 4]
[1, 6, 4, 5, 7, 2, 8, 9, 3]
[1, 6, 8, 2, 9, 3, 5, 7, 4]
[1, 6, 8, 7, 3, 2, 9, 5, 4]
[1, 6, 8, 7, 3, 4, 5, 9, 2]
[1, 7, 2, 4, 3, 9, 8, 5, 6]
[1, 7, 2, 5, 6, 4, 8, 9, 3]
[1, 7, 3, 5, 4, 2, 9, 8, 6]
[1, 8, 3, 4, 5, 2, 9, 7, 6]
[1, 8, 4, 3, 5, 2, 7, 9, 6]
[1, 9, 2, 4, 5, 6, 8, 7, 3]
[1, 9, 3, 2, 6, 8, 5, 7, 4]
[1, 9, 3, 5, 4, 8, 6, 7, 2]
[1, 9, 6, 5, 2, 8, 7, 3, 4]
[1, 9, 6, 5, 3, 2, 7, 8, 4]
[2, 1, 3, 7, 4, 8, 9, 5, 6]
[2, 1, 6, 5, 7, 3, 9, 4, 8]
[2, 3, 1, 5, 6, 8, 9, 7, 4]
[2, 3, 6, 9, 4, 8, 5, 7, 1]
[2, 3, 6, 9, 4, 8, 7, 5, 1]
[2, 4, 8, 7, 1, 3, 9, 5, 6]
[2, 4, 8, 9, 3, 6, 5, 7, 1]
[2, 4, 8, 9, 3, 6, 7, 5, 1]
[2, 5, 1, 3, 6, 8, 9, 7, 4]
[2, 6, 8, 1, 9, 3, 5, 7, 4]
[2, 6, 8, 3, 5, 1, 9, 7, 4]
[2, 6, 8, 5, 3, 1, 9, 7, 4]
[2, 6, 8, 5, 9, 4, 3, 7, 1]
[2, 6, 8, 5, 9, 4, 7, 3, 1]
[2, 6, 9, 8, 4, 3, 5, 7, 1]
[2, 6, 9, 8, 4, 3, 7, 5, 1]
[2, 7, 3, 5, 1, 6, 9, 4, 8]
[2, 9, 3, 1, 6, 8, 5, 7, 4]
[2, 9, 4, 5, 6, 8, 3, 7, 1]
[2, 9, 4, 5, 6, 8, 7, 3, 1]
[3, 1, 2, 5, 6, 8, 7, 9, 4]
[3, 1, 4, 5, 2, 8, 7, 9, 6]
[3, 2, 1, 5, 6, 8, 9, 7, 4]
[3, 2, 8, 5, 1, 4, 7, 9, 6]
[3, 4, 8, 5, 9, 2, 6, 7, 1]
[3, 4, 8, 5, 9, 2, 7, 6, 1]
[3, 5, 1, 2, 6, 8, 9, 7, 4]
[3, 5, 2, 1, 8, 4, 7, 9, 6]
[3, 6, 8, 2, 5, 1, 9, 7, 4]
[3, 6, 8, 5, 1, 2, 7, 9, 4]
[3, 6, 8, 5, 2, 1, 9, 7, 4]
[3, 8, 4, 1, 5, 2, 7, 9, 6]
[3, 9, 2, 5, 4, 8, 6, 7, 1]
[3, 9, 2, 5, 4, 8, 7, 6, 1]
[4, 5, 2, 1, 8, 3, 9, 7, 6]
[4, 6, 2, 5, 9, 3, 7, 8, 1]
[4, 6, 2, 5, 9, 3, 8, 7, 1]
[4, 7, 2, 1, 3, 9, 8, 5, 6]
[4, 8, 3, 1, 5, 2, 9, 7, 6]
[4, 8, 3, 7, 2, 6, 5, 9, 1]
[4, 8, 3, 7, 2, 6, 9, 5, 1]
[4, 9, 2, 1, 5, 6, 8, 7, 3]
[4, 9, 3, 5, 6, 2, 7, 8, 1]
[4, 9, 3, 5, 6, 2, 8, 7, 1]
[5, 1, 2, 3, 6, 8, 7, 9, 4]
[5, 1, 4, 3, 2, 8, 7, 9, 6]
[5, 1, 6, 2, 3, 9, 7, 4, 8]
[5, 1, 6, 2, 7, 3, 9, 4, 8]
[5, 2, 1, 3, 6, 8, 9, 7, 4]
[5, 2, 4, 9, 3, 6, 7, 8, 1]
[5, 2, 4, 9, 3, 6, 8, 7, 1]
[5, 2, 8, 1, 9, 6, 7, 3, 4]
[5, 2, 8, 3, 1, 4, 7, 9, 6]
[5, 3, 1, 2, 6, 8, 9, 7, 4]
[5, 3, 2, 1, 9, 6, 7, 8, 4]
[5, 3, 2, 8, 6, 4, 7, 9, 1]
[5, 3, 2, 8, 6, 4, 9, 7, 1]
[5, 3, 6, 9, 2, 4, 7, 8, 1]
[5, 3, 6, 9, 2, 4, 8, 7, 1]
[5, 3, 9, 2, 1, 6, 7, 4, 8]
[5, 4, 2, 1, 3, 9, 7, 8, 6]
[5, 4, 2, 1, 7, 3, 9, 8, 6]
[5, 4, 8, 1, 9, 3, 6, 7, 2]
[5, 4, 8, 3, 9, 2, 6, 7, 1]
[5, 4, 8, 3, 9, 2, 7, 6, 1]
[5, 6, 2, 4, 9, 3, 7, 8, 1]
[5, 6, 2, 4, 9, 3, 8, 7, 1]
[5, 6, 4, 1, 7, 2, 8, 9, 3]
[5, 6, 4, 8, 3, 2, 7, 9, 1]
[5, 6, 4, 8, 3, 2, 9, 7, 1]
[5, 6, 8, 2, 3, 1, 9, 7, 4]
[5, 6, 8, 2, 9, 4, 3, 7, 1]
[5, 6, 8, 2, 9, 4, 7, 3, 1]
[5, 6, 8, 3, 1, 2, 7, 9, 4]
[5, 6, 8, 3, 2, 1, 9, 7, 4]
[5, 7, 2, 1, 6, 4, 8, 9, 3]
[5, 7, 3, 1, 4, 2, 9, 8, 6]
[5, 7, 3, 2, 1, 6, 9, 4, 8]
[5, 9, 2, 3, 4, 8, 6, 7, 1]
[5, 9, 2, 3, 4, 8, 7, 6, 1]
[5, 9, 3, 1, 4, 8, 6, 7, 2]
[5, 9, 3, 4, 6, 2, 7, 8, 1]
[5, 9, 3, 4, 6, 2, 8, 7, 1]
[5, 9, 4, 2, 6, 8, 3, 7, 1]
[5, 9, 4, 2, 6, 8, 7, 3, 1]
[5, 9, 6, 1, 2, 8, 7, 3, 4]
[5, 9, 6, 1, 3, 2, 7, 8, 4]
[6, 2, 8, 7, 3, 4, 5, 9, 1]
[6, 2, 8, 7, 3, 4, 9, 5, 1]
[6, 3, 4, 7, 2, 8, 5, 9, 1]
[6, 3, 4, 7, 2, 8, 9, 5, 1]
[6, 4, 8, 1, 5, 2, 7, 9, 3]
[6, 5, 2, 1, 4, 8, 7, 9, 3]
[7, 2, 4, 1, 3, 9, 8, 5, 6]
[7, 2, 8, 1, 5, 4, 9, 3, 6]
[7, 2, 8, 1, 6, 3, 9, 5, 4]
[7, 2, 8, 6, 3, 4, 5, 9, 1]
[7, 2, 8, 6, 3, 4, 9, 5, 1]
[7, 3, 2, 1, 6, 8, 9, 5, 4]
[7, 3, 4, 1, 6, 8, 5, 9, 2]
[7, 3, 4, 6, 2, 8, 5, 9, 1]
[7, 3, 4, 6, 2, 8, 9, 5, 1]
[7, 3, 6, 1, 5, 2, 9, 8, 4]
[7, 4, 8, 1, 5, 2, 9, 6, 3]
[7, 4, 8, 2, 1, 3, 9, 5, 6]
[7, 5, 2, 1, 3, 6, 9, 8, 4]
[7, 5, 2, 1, 4, 8, 9, 6, 3]
[7, 5, 3, 1, 8, 6, 9, 4, 2]
[7, 5, 4, 1, 2, 8, 9, 3, 6]
[7, 6, 3, 1, 2, 8, 9, 5, 4]
[7, 6, 8, 1, 3, 2, 9, 5, 4]
[7, 6, 8, 1, 3, 4, 5, 9, 2]
[7, 8, 3, 4, 2, 6, 5, 9, 1]
[7, 8, 3, 4, 2, 6, 9, 5, 1]
[7, 8, 6, 1, 5, 3, 9, 4, 2]
[8, 2, 4, 1, 7, 6, 9, 5, 3]
[8, 3, 2, 5, 6, 4, 7, 9, 1]
[8, 3, 2, 5, 6, 4, 9, 7, 1]
[8, 4, 3, 1, 7, 6, 9, 5, 2]
[8, 4, 3, 2, 6, 9, 5, 7, 1]
[8, 4, 3, 2, 6, 9, 7, 5, 1]
[8, 6, 4, 5, 3, 2, 7, 9, 1]
[8, 6, 4, 5, 3, 2, 9, 7, 1]
[8, 6, 9, 2, 4, 3, 5, 7, 1]
[8, 6, 9, 2, 4, 3, 7, 5, 1]
[8, 7, 6, 1, 2, 4, 9, 5, 3]
[8, 7, 6, 1, 4, 3, 9, 5, 2]
[9, 2, 4, 5, 3, 6, 7, 8, 1]
[9, 2, 4, 5, 3, 6, 8, 7, 1]
[9, 2, 6, 4, 5, 3, 7, 8, 1]
[9, 2, 6, 4, 5, 3, 8, 7, 1]
[9, 3, 6, 2, 4, 8, 5, 7, 1]
[9, 3, 6, 2, 4, 8, 7, 5, 1]
[9, 3, 6, 5, 2, 4, 7, 8, 1]
[9, 3, 6, 5, 2, 4, 8, 7, 1]
[9, 4, 8, 2, 3, 6, 5, 7, 1]
[9, 4, 8, 2, 3, 6, 7, 5, 1]
[9, 5, 3, 4, 2, 6, 7, 8, 1]
[9, 5, 3, 4, 2, 6, 8, 7, 1]
"""
