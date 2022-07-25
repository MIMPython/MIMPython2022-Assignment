#Bài3
a = str(input("Tên học viên="))
b = int(input("Số thứ tự tuần học="))
c = int(input("Số thứ tự bài tập="))
def filename(a,b,c):
    print(f"week{b}_assignment{c}_{a}.py")
filename(a,b,c)