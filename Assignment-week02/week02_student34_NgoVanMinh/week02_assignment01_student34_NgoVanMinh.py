# %%
"""Bài tập 1. Hãy trả lời những câu hỏi, thực hiện những yêu cầu sau đây

(a) Những kí tự nào không được phép xuất hiện trong tên biến trong Python?
(b) Cho ví dụ về tên biến hợp lệ và ví dụ về tên biến không hợp lệ.
(c) Khi nói đến việc đặt tên biến, tác giả Robert C. Martin viết trong cuốn sách Clean Code: A Handbook of Agile Software Craftsmanship viết
"""

"""It is easy to say that names should reveal intent. What we want to impress upon you is that we are serious about this. Choosing good names takes time but saves more than it takes. So take care with your names and change them when you find better ones. Everyone who reads your code (including you) will be happier if you do.
The name of a variable should answer all the big questions. It should tell you why it exists, what it does, and how it is used. If a name requires a com- ment, then the name does not reveal its intent"""

"""Hãy cho ví dụ về cách đặt tên biến tốt kèm theo tình huống sử dụng những biến này.

(d) Cho danh sách những tên biến có cùng ý nghĩa thể hiện số sinh viên

numberofcollegestudents
NUMBEROFCOLLEGESTUDENTS
numberOfCollegeStudents
NumberOfCollegeStudents
number_of_college_students
Hãy mô tả các phong cách đặt những tên biến trên.
(e) Phân biệt các phong cách đặt tên biến Camel Case, Pascal Case và Snake Case. Cho ví dụ.
(f) Bạn chọn phong cách đặt tên biến nào?"""

# %%
"""
a) Python không chấp nhận đặt tên biến bằng các kí hiệu đặc biệt ví dụ @, $, % và không đặt các chữ số ở đầu tiên và không đặt tên
trùng với các key words ví dụ như class, False, True,...
b)
Wrong answer 
    76trombones = 'big parade'
    more@ = 1000000
Correct answer
    numberOfStudent = 3
c)
    numberOfStudent = 40    #Số học sinh trong lớp
d)
numberofcollegestudents : Camelcase
NUMBEROFCOLLEGESTUDENTS : Camelcase viết hoa
number_of_college_students : Snakecase
NumberOfCollegeStudents : Pascalcase
f) Mình chọn Pascalcase
"""


