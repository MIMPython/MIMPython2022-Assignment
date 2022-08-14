print("Bài 9: Three Hands Of A Clock")

"""
Cho ba điểm A, B, C di động trên đường tròn tâm O có bán kính R = OA = OB = OC = 1
Với OA là kim giờ, OB là kim phút, OC là kim giây
Đặt M = AB + BC + CA
Tìm GTNN và GTLN của M

THUẬT TOÁN
a) Tìm GTNN của M = AB + BC + CA 
+ Có A, B, C là các điểm nằm trên đồng hồ => AB, BC, CA đều có giá trị không âm
+ Để M = AB + BC + CA đạt GTNN khi và chỉ khi AB = BC = CA = 0 => M = 0
hay có thể coi A, B, C là các điểm trùng nhau
=> Kim giờ OA, Kim phút OB, Kim giây OC trùng nhau


b) Tìm GTLN của M = AB + AC + CA
+ Có A, B, C là các điểm nằm trên đồng hồ => AB, BC, CA đều có giá trị không âm
+ Gọi AB = x, BC = y, CA = z
Để M = x + y + z đạt GTLN thì:
Áp dụng bất đẳng thức Bunhiacopski cho ba số thực không âm x, y, z có:
(a*x + b*y + c*z)**2 <= (a**2 + b**2 + c**2)*(x**2 + y**2 + z**2)
thay a = b = c = 1
<=> (1*x + 1*y + 1*z)**2 <= (1 + 1 + 1)*(x**2 + y**2 + z**2)
<=> (x + y + z)**2 <= 3*(x**2 + y**2 + z**2)
<=> x + y + z <= sqrt(3*(x**2 + y**2 + z**2))

Theo hệ quả bất đẳng thức Bunhiacopski ta được:
=> x = y = z <=> AB = BC = CA <=> Tam giác ABC là tam giác đều
gọi AB = BC = CA = e
Ta có OA = OB = OC = 1 = e*sqrt(3)/3 <=> e = sqrt(3)

Thay vào bất phương truinhf trên ta có:
x + y + z <= sqrt(3*(3+3+3)) = 3*sqrt(3)
<=> M <= 3*sqrt(3)
<=> Mmax = 3*sqrt(3)
=> Kim giờ OA, Kim phút OB, Kim giấy OC lần lượt lệch nhau góc 120 độ

"""

def gtnn(hour, minute, second):
    second -= 10
    for i in range(1, 12):
        hour += 1
        minute += 5
        second += 5
        print(f"Thời điểm thứ {i} để M đạt GTNN là {hour}:{minute:02d}:{second:02d}")

def gtln(hour, minute, second):
    second -= 10
    for i in range(12):
        minute += 20
        second = minute + 20
        if i == 0:
            print(f"Thời điểm giờ thứ {i} để M đạt GTLN là {hour}:{minute:02d}:{second:02d}")
            print(f"Thời điểm giờ thứ {i} để M đạt GTLN là {hour}:{second:02d}:{minute:02d}")
        else:
            hour += 1
            if minute >= 60: 
                minute -= 60
            if second >= 60:
                second -= 60
            print(f"Thời điểm giờ thứ {i} để M đạt GTLN là {hour}:{minute:02d}:{second:02d}")
            print(f"Thời điểm giờ thứ {i} để M đạt GTLN là {hour}:{second:02d}:{minute:02d}")

#Dữ liệu đầu vào
hour = 0
minute = 0
second = 10

print("Giá trị nhỏ nhất của M = AB + BC + CA là:")
gtnn(hour, minute, second)
print() 
gtln(hour, minute, second)
