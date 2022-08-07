A = []
lstong = []
tb = int(input(f"Nhập số phần tử trong A: \n"))
for i in range(1,tb+1):
    prompt = int(input(f"Nhập số phần tử của phần tử thứ {i} "))
    pt = []
    tong = 0
    for k in range(1,prompt+1):
        nh = int(input("Nhập phần tử: "))
        pt.append(nh)
        tong = tong + nh       
    lstong.append(tong)
    A.append(pt)
s = sorted(lstong)
B = []
for i in s:
    for j in range(0,len(lstong)):
        if lstong[j] == i:
            B.append(A[j])
print(B)