print("Bài 8: Banking Simulation")
print()

from tkinter import *
from tkinter.messagebox import showinfo

def kiemtra():
    a = str(Stringusername.get())
    name = str((Stringname).get())
    b = str(StringNew.get())
    c = str(StringAgain.get())
    if b == c:
        def luufile(path):
            file = open(path, 'w', encoding = 'utf-8')
            file.writelines(a + ";" + name + ";" + b)
            file.close()
        luufile("csdl.txt")
        
        #Thông báo ra màn hình
        showinfo("Đăng nhập thành công", "Số tiền trong tài khoản đã được cập nhật")
        exit()
        
    else:
        Stringusername.set("")
        StringNew.set("")
        StringAgain.set("")

root = Tk()

Stringusername = StringVar()
StringNew = StringVar()
StringAgain = StringVar()
Stringname = StringVar()

root.title("Banking Simulation")
root.minsize(height=100,width=350)

#Tiêu đề cho tkinter
Label(root, text = "Chào mừng bạn đến với Banking Simulation", fg = "Green", font = ("tohama", 15)).grid(row = 0, column = 1, columnspan=3)

#Giao diện Tkinter
Label(root,text="USERNAME:").grid(row=1,column=1,columnspan=2)
Entry(root,width=30,textvariable=Stringusername).grid(row=1,column=3)
Label(root, text="HỌ VÀ TÊN:").grid(row = 2,column = 1, columnspan=2)
Entry(root,width=30,textvariable=Stringname).grid(row=2,column=3)

Label(root,text="Enter Password:").grid(row=3,column=1,columnspan=2)
Entry(root,width=30,textvariable=StringNew).grid(row=3,column=3)
Label(root,text="Enter New Password Again:").grid(row=4,column=1,columnspan=2)
Entry(root,width=30,textvariable=StringAgain, show = "*").grid(row=4,column=3)

#Button xử lý
frameButton=Frame(root)
Button(frameButton,text=" OK ",command=kiemtra).pack()
frameButton.grid(row=5,column=1)

frameButton=Frame(root)
Button(frameButton,text="Cancel",command=root.quit).pack()
frameButton.grid(row=5,column=2)

root.mainloop()