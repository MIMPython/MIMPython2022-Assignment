print("Tro choi keo - bua - bao")
print("Moi nguoi choi A chon (1-3):")
print("1.Keo")
print("2.Bua")
print("3.Bao")
a = int (input())
while (a<1 or a>3):
    print("So da chon chua hop le. Moi ban chon lai (1-3): ")
    a = int (input())

print("Moi nguoi choi B chon (1-3):")
print("1.Keo")
print("2.Bua")
print("3.Bao")
b = int (input())
while (b<1 or b>3):
    print("So da chon chua hop le. Moi ban chon lai (1-3): ")
    b = int (input())
    
if (a==b):
    print("Hai ban hoa nhau")
elif (a==1):
    if (b==2):
        print("Nguoi B thang")
    else:
        print("Nguoi A thang")
elif (a==2):
    if (b==1):
        print("Nguoi A thang")
    else:
        print("Nguoi B thang")
elif (a==3):
    if (b==1):
        print("Nguoi B thang")
    else:
        print("Nguoi A thang")





