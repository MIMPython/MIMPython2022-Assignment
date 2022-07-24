print("Bài 3: Viết hàm nhập vào tên học viên, STT tuần học, STT bài tập")
def hocvien(ten, tuan, baitap):
    ten = ten.strip()
    t = ten.split()
    tene = ""
    for i in t:
        tene += i
    if tuan <= 9:
        tuan = "0" + str(tuan)
    if baitap <= 9:
        baitap = "0" + str(baitap)
    print("week" + str(tuan) + "_" + "assignment" + str(baitap) + "_" + tene + ".py")
ten = input("Tên học viên: ")
tuan = int(input("STT tuần: "))
baitap = int(input("STT bài tập: "))
hocvien(ten, tuan, baitap)

#hocvien(Quang Tung, 2, 13) = week02_assignment13_QuangTung.py
