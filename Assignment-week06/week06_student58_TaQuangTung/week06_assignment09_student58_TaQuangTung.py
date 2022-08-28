print("Bài 9: Clock")

#Nhập xuất các thư viện cần thiết
from tkinter import *           
from datetime import datetime       
import time               
import math             


#Nhập độ lớn của đồng hồ và màu sắc đồng hồ
WINwidth = 500                          #Độ lớn của đồng hồ
WINcolor = '#7FFFD4'                    #Màu sắc của đồng hồ (xanh)


#Độ lớn của các dây kim
WINheight = WINwidth                    #Chiều rộng của cửa sổ Tkinter
S_length = WINwidth / 2 * 0.75          #Độ dài kim giây
M_length = S_length * 0.95              #Độ dài kim phút
H_length = S_length * 0.8               #Độ dài kim giờ

H_LINEwidth = 8  #Độ to của kim giờ
M_LINEwidth = H_LINEwidth / 2  #Độ to của kim phút 
S_LINEwidth = 1  #Đồ to của kim giây

#Thân chương trình chính
root = Tk()
root.title("CLOCK")

w = Canvas(root, width = WINwidth, height = WINheight, background = WINcolor)
w.pack()

w.create_oval(WINwidth / 2 - 5, WINheight / 2 - 5, WINwidth / 2 + 5, WINheight / 2 + 5, fill="black")       #Tạo điểm tâm của đồng hồ
w.create_oval(5, 5, WINwidth-5, WINheight-5, width = 2)             #Tạo vòng tròn bên ngoài đồng hồ


FontSize = int(WINwidth / 14)       #Size của cỡ chữ 
Fx = 0                              #Sửa vị trí của chữ hiển thị giờ
Fy = FontSize / 10
R = S_length + FontSize * 0.9       #Bán kính của chữ hiển thị giờ
A = 0                               #Độ lớn của góc tạo với chữ hiển thị giờ

#Hiển thị chữ số
for i in range(1,13):               
    A = A + 30
    Tx = R * math.cos(A / 180 * math.pi)            #Tọa độ của chữ số để hiển thị giờ trên đồng hồ
    Ty = R * math.sin(A / 180 * math.pi)
    w.create_text(WINwidth / 2 + Ty - Fx, WINheight / 2 - Tx + Fy, text = i, font = ("", FontSize))

try:
    #Vòng lặp để tính giờ
    while True:
        now = datetime.now()  
        if now.hour > 12:  
            nowhour = now.hour - 12
        else:
            nowhour = now.hour


        nowhour = nowhour + now.minute / 60 + now.second / 3600         #Thay đổi định dạng thời gian sang giờ
        nowminute = now.minute + now.second / 60                        #Thay đổi định dạng thời gian sang phút

        #Tính toán giữa các góc
        H_A = nowhour / 12 * 360 * math.pi /180             #Góc tạo với kim giờ
        M_A = nowminute / 60 * 360 * math.pi / 180          #Góc tạo với kim phút
        S_A = now.second / 60 * 360 * math.pi / 180         #Góc tạo với kim giây


        #Độ dài của kim so với trung tâm đồng hồ
        H_x = math.cos(H_A) * H_length  
        H_y = math.sin(H_A) * H_length
        M_x = math.cos(M_A) * M_length
        M_y = math.sin(M_A) * M_length
        S_x = math.cos(S_A) * S_length
        S_y = math.sin(S_A) * S_length


        #Khởi tạo thêm đồng hồ số phia bên dưới (hiển thị vị trí của chữ trên đồng hồ số)
        w.create_text(WINwidth / 2 , WINheight / 2 + WINwidth / 8, text = datetime.now().strftime('%Y/%m/%d %H:%M:%S'), font = ("", int(FontSize / 1.5)), tag="Y")  #Hiển thị dữ liệu trên đồng hồ số


        #Hiển thị đồng hồ kim chạy
        w.create_line(WINwidth / 2, WINheight / 2, WINwidth / 2 + H_y, WINheight / 2 - H_x, width = H_LINEwidth, tag="H") #Kim giờ
        w.create_line(WINwidth / 2, WINheight / 2, WINwidth / 2 + M_y, WINheight / 2 - M_x, width = M_LINEwidth, tag="M") #Kim phút
        w.create_line(WINwidth / 2, WINheight / 2, WINwidth / 2 + S_y, WINheight / 2 - S_x, width = S_LINEwidth, tag="S") #Kim giây
        """
        Tạo đường thẳng cần có hai điểm (x1,y1) và (x2,y2)    
        """

        w.update()  #Update thời gian mới

        #Xóa thời gian cũ
        w.delete("H")  
        w.delete("M")
        w.delete("S")
        w.delete("Y")

        time.sleep(0.01)  #Tạo khoảng thời gian nghỉ
except:
    pass

root.mainloop()
