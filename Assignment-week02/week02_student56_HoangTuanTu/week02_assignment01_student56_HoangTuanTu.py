"""
a) Những kí tự nào không được phép xuất hiện trong tên biến trong Python?
-> Trả lời: 
+ Các ký tự đặc biệt (nằm ngoài khoảng hợp giữa các đoạn [48-57]; [65-89] và [97-121] trong bảng mã ASCII)
không phải ký tự chữ số hay chữ cái) ví dụ: ',', '.', '%',... 
+ Trường hợp đặc biệt ký tự gạch dưới '_' được xuất hiện trong tên biến
+ Trùng tên với các từ được bao lưu có sẵn trong python (print, def, class,...)
+ Ngoài ra các kỹ tự chữ số (từ 48 đến 57 trong bảng mã ACIII) cũng không được đặt ở đầu biến


b) Cho ví dụ về tên biến hợp lệ và ví dụ về tên biến không hợp lệ.
-> Trả lời:
+ Biến hợp lệ: a = 3; b = []; c = (1,2); d = "23456"; a_ =10;...
+ Biến không hợp lệ: %a = 3; a& = 3; a b = 3; c@ = []; 3a = 3;..c.



"""

"""C) Hãy cho ví dụ về cách đặt tên biến tốt kèm theo tình huống sử dụng những biến này.
-> Trả lời: 
"""

student = {1:"Hoang Tuan Tu",2 : "Tran Van Luat",3:"Nguyen Thi Ha Phuong"}

def search(id):
    return student[id]

print("Input ID of student you want to search:", end =" ")
id = int(input())
if id<0 or id> 3:
    print(
        "Invalid ID")
print("Student have ID {} have name: {}".format(id,search(id)))

date = 26
month = 10
year = 2003

print("My birth is: {}/{}/{}".format(date,month,year))

"""
d) Hãy mô tả các phong cách đặt những tên biến trên.
-> Trả lời:
+ numberofcollegestudents: Phong cách đặt tên biến: Lowercase - Là tên mà tất cả các chữ cái trong 
một từ được viết mà không Viết Hoa

+ NUMBEROFCOLLEGESTUDENTS: Phong cách đặt tên biến: Uppercase - Là tên trong đó tất cả các chữ cái
trong một từ được viết bằng chữ HOA

+ numberOfCollegeStudents: Phong cách đặt tên biến: camelCase - Từ đầu tiên viết thường, các từ tiếp theo 
viết hoa chữ cái đầu và giữa các từ không có dấu nối

+ NumberOfCollegeStudents: Phong cách đặt tên biến: PascalCase - Viết hoa tất cả các chữ cái đầu và
giữa các từ không có dấu nối

+ number_of_college_students: phong cách đặt tên biến: Underscore -  Sử dụng dấu gạch chân giữa các từ,
tất cả các từ đều viết thường #Có thể được gọi bằng cái tên khác (Snake case/ Kecab case)

e) Phân biệt các phong cách đặt tên biến Camel Case, Pascal Case và Snake Case. Cho ví dụ.
-> Trả lời: 
*Phân biệt:
+ Camel case: Từ đầu tiên viết thường, các từ tiếp theo viết hoa chữ cái đầu và giữa các từ không có dấu nối
+ PascalCase - Viết hoa tất cả các chữ cái đầu và giữa các từ không có dấu nối
+ Snake case/ Kecab case/ Underscore: Sử dụng dấu gạch chân giữa các từ, tất cả các từ đều viết thường 

*Ví dụ: 
+ Camel case: numberOfCollegeStudents
+ Pascal case: NumberOfCollegeStudents
+ Snake case/ Kecab case/ Underscore: number_of_college_students

f) Bạn chọn phong cách đặt tên biến nào?
-> Trả lời: Phong cách đặt tên Camel case tạo cảm giác vô cùng thuận mắt và đã khi học các ngôn ngữ khác
nên em chọn phong cách đặt tên biến là camel case
"""
