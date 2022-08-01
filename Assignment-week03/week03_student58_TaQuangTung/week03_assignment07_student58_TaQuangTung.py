print("Bài 7: Largest Prime Factor")
# PHÂN TÍCH MỘT SỐ THÀNH TÍCH CÁC SỐ NGUYÊN TỐ
n = int(input("n = "))
lst = []        #Mảng gồm các thừa số nguyên tố
i = 2
while n > 1:
    while (n % i == 0):
        lst.append(i)
        n //= i
    i += 1
print("Mảng gồm tích các số nguyên tố là:",lst)
print("Thừa số nguyên tố lớn nhất là:", max(lst))