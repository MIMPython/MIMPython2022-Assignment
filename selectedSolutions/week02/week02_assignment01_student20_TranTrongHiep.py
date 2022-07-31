"""
Bài 1.
a. Những kí tự nào không được phép xuất hiện trong tên biến trong Python
    Không sử dụng các kí tự đặc biệt như: @, $, %,... trừ dấu "_".
	Không thể sử dụng các từ khóa của Python như: class, bool, print,...
	Không thể sử dụng các giá trị số (0 đến 9) cho ký tự đầu tiên.

b. Ví dụ
    Hợp lệ: HoTen, Nam_Sinh, num2,...
    Không hợp lệ: 2k, sum%, class,...

c. Ví dụ về cách đặt tên biến tốt
    #Tính tổng hai số nguyên
	a = 2
	b = 6
	sum = a + b;	#sum: tổng

	print(sum)	#8

d. Mô tả các phong cách đặt tên biến.
    numberofcollegestudents: tất cả các chữ cái đều viết in thường.
    NUMBEROFCOLLEGESTUDENTS: tất cả các chữ cái đều viết in hoa.
	    => Hai phong cách đặt tên biến trên đều khó có thể phân biệt được cái từ, dễ rối, nhầm lẫn.
    numberOfCollegeStudents: chữ cái đầu tiên của tất cả các từ đều viết in hoa, trừ chữ cái đầu của từ đầu tiên thì viết in thường.
    NumberOfCollegeStudents: chữ cái đầu tiên của tất cả các từ đều viết in hoa.
    number_of_college_students: các từ được ngăn cách với nhau bởi dấu "_" và tất cả các chữ cái đều viết in thường.
	    => Ba phong cách đặt tên biến này đều có dấu hiệu ngăn cách giữa các từ nên dễ dàng nhận biết.

e. Phân biệt các phong cách đặt tên biến:
	Camel Case: chữ cái đầu tiên của tất cả các từ đều viết in hoa, trừ chữ cái đầu của từ đầu tiên thì viết in thường.
		VD: camelCase, hoVaTen, namSinh,...
	Pascal Case: chữ cái đầu tiên của tất cả các từ đều viết in hoa.
		VD: PascalCase, HoVaTen, NamSinh,...
	Snake Case: các từ được ngăn cách với nhau bởi dấu "_" và tất cả các chữ cái đều viết in thường (hoặc có thể tất cả in hoa).
		VD: snake_case, ho_va_ten, NAM_SINH,...

f. Mình chọn phong cách đặt tên biến Pascal Case.
"""