"""
a) Vòng lặp do - while trong C khác với while trong Python là do - while sẽ thực hiện khối lệnh trong phần do trước rồi mới kiểm tra điều kiện, 
còn while thì kiểm tra điều kiện trước rồi mới thực hiện lệnh. Nghĩa là dù điều kiện sai thì khối lệnh trong do sẽ chạy ít nhất 1 lần
"""

#do - while trong python
while 1:
    userInput = input("Type exit to end program: ")
    if userInput == "exit":
        break
    else:
        continue
#Có thể thấy, vòng lặp trên luôn chạy ít nhất 1 lần