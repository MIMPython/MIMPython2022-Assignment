"""
(a) Những kí tự nào không được phép xuất hiện trong tên biến trong Python?
>>>>Các ký tự đặc biệt (trừ dấu _).
    Chữ số đứng ở đầu tên biến.
    Khoảng trắng.
    Các từ khóa của Python và tên các hàm có sẵn.

(b) Cho ví dụ về tên biến hợp lệ và ví dụ về tên biến không hợp lệ.
>>>>Tên biến hợp lệ
        example1 = "Ví dụ một"
        usd = "Đô la Mỹ"
        tenhople = "Tên hợp lệ"
        final = "Cuối cùng"
    Tên biến không hợp lệ
        1example = "Một ví dụ"
        $usd = "Đô la Mỹ"
        ten khong hop le = "Tên không hợp lệ"
        finally = "Cuối cùng"

(c) Khi nói đến việc đặt tên biến, tác giả Robert C. Martin viết trong cuốn sách Clean Code: A Handbook of Agile Software Craftsmanship viết

It is easy to say that names should reveal intent. What we want to impress upon you is that we are serious about this. Choosing good names takes time but saves more than it takes. So take care with your names and change them when you find better ones. Everyone who reads your code (including you) will be happier if you do.
The name of a variable should answer all the big questions. It should tell you why it exists, what it does, and how it is used. If a name requires a com- ment, then the name does not reveal its intent.

Hãy cho ví dụ về cách đặt tên biến tốt kèm theo tình huống sử dụng những biến này.
>>>>first_name = "Mai"
    last_name = "Thanh Liêm"
    full_name = f"{first_name} {last_name}"
    print(full_name)

(d) Cho danh sách những tên biến có cùng ý nghĩa thể hiện số sinh viên

numberofcollegestudents
    >>>flat case
NUMBEROFCOLLEGESTUDENTS
    >>>upper case
numberOfCollegeStudents
    >>>camel case
NumberOfCollegeStudents
    >>>Pascal case
number_of_college_students
    >>>snake case
Hãy mô tả các phong cách đặt những tên biến trên.
    flat case: tên biến viết thường tất cả, liền nhau không phân biệt các từ trong tên;
    upper case: tên biến viết hoa tất cả, liền nhau không phân biệt các từ trong tên;
    camel case: tên biến viết liền không phân biệt các từ trong tên, viết hoa ở những chữ cái đầu của các từ chính thể hiện ý nghĩa của tên;
    Pascal case: tên biến viết liền không biệt các từ trong tên, viết hoa ở tất cả những chữ cái đầu của các từ trong tên;
    snake case: tên biến viết thường tất cả, phân biệt các từ trong tên bởi dấu _.

(e) Phân biệt các phong cách đặt tên biến Camel Case, Pascal Case và Snake Case. Cho ví dụ.
    camel case: tên biến viết liền không phân biệt các từ trong tên, viết hoa ở những chữ cái đầu của các từ chính thể hiện ý nghĩa của tên;
        Ví dụ: nameofStudent;
    Pascal case: tên biến viết liền không biệt các từ trong tên, viết hoa ở tất cả những chữ cái đầu của các từ trong tên;
        Ví dụ: NameOfStudent;
    snake case: tên biến viết thường tất cả, phân biệt các từ trong tên bởi dấu _.
        Ví dụ: name_of_student;

(f) Bạn chọn phong cách đặt tên biến nào?
>>>>Snake case.
"""
