""" (do-while conversion)
a) So sánh vòng lặp do-while trong C++ với vòng lặp while trong Python.
   + Do-while trong C++: Chương trình thực thi khối lệnh trong phần do, sau đó kiểm 
   tra điều kiện ở phần while. Nếu điều kiện xảy ra thì chương trình quay trở lại  
   điểm xuất phát vòng lặp, nếu điều kiện không xảy ra thì chương trình thoát khỏi vòng lặp.           
    
    + Do-while trong Python: Trong vòng lặp while, điều_kiện_kiểm_tra sẽ được kiểm tra đầu tiên. 
    Khối lệnh của vòng lặp chỉ được nạp vào nếu điều_kiện_kiểm_tra là True. Sau một lần lặp,  
    điều kiện kiểm tra sẽ được kiểm tra lại. Quá trình này sẽ tiếp tục cho đến khi điều kiện 
    kiểm tra là False. Trong Python mọi giá trị khác 0 đều là True, None và 0 được hiểu là False. 
     
    Khuyết điểm: Đặc điểm này của while có thể dẫn đến trường hợp là while có thể không chạy vì  
    ngay lần lặp đầu tiên điều_kiện_kiểm_tra đã False. Khi đó, khối lệnh của while sẽ bị bỏ qua  
    và phần code ngay sau đó sẽ được thực thi.

b) Có thể biến đổi tương đương đoạn code sử dụng do-while trong C++ sang đoạn code sử dụng while trong Python hay không? 
VD: Nhập vào một số nguyên dương từ bàn phím và in ra số đó. Nếu nhập sai, bắt nhập lại.
+) C++ 
int main(){
    int number;
    do{
        printf("\nNhap number = ");
        scanf("%d", &number);
    }while(number < 1);
    printf("\nnumber = %d", number);
}
 
+) Python
n = int(input("Nhap number = "))
while (n < 0):
    n = int(input("Nhap number = "))
"""