
#a) Chương trình vô hạn sử dụng vào lặp while:
def ques_a():
    i = 0
    while i < 10:
        print("Hello, MIMer")
    
     
#b) Chương trình chạy vô hạn sử dụng vòng lặp for và không dùng vòng lặp while
def ques_b():
    a = list()
    a.append(0)
    for i in a:
        print(i)
        a.append(i+1)
        
# c)
def ques_c():
    for _ in iter (int, 1): 
        pass
