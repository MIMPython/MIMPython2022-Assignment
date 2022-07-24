""" 
a) Những kí tự không được phép xuất hiện trong tên biến Python: 
Những kí tự khác ngoài các chữ cái Latinh (A-z), chữ số (0-9) và _ ví dụ như: !, @,#,$,….
b) Tên biến hợp lệ: Test01, test01, _tuổi, 
   Tên biến không hợp lệ: 
      + 7up: Kí tự đầu tiên là giá trị số -> lỗi SyntaxError sẽ xuất hiện
      + from = "Việt Nam" : Sử dụng các từ khóa của python để đặt tên biến ->lỗi SyntaxError sẽ xuất hiện
c) Khi ta đặt tên một biến lưu trữ điểm số của Sinh viên
Cách đặt biến không tốt: a 
                         Num
Cách đặt biến tốt: score_of_student
              hay: student_score

d) Mô tả phong cách đặt tên:
   + numberofcollegestudents: lower case
   + NUMBEROFCOLLEGESTUDENTS: upper case
   + numberOfCollegeStudents: Camel Case
   + NumberOfCollegeStudents: PascalCase
   + number_of_college_students: snake_case, underscore
   
   Phân biệt các phong cách đặt tên biến Camel Case, Pascal Case và Snake Case:
   + Camel Case: Tên hàm và phương thức, Ví dụ: getUser, getCategory…
   + Pascal Case: Tên lớp, Ví dụ: UserClass, CategoryClass…
   + Snake Case: Với kiểu này, khi viết hoa, thường được sử dụng như một quy ước trong các hằng số.
     Với kiểu viết thường, nó thường được sử dụng trong việc khai báo tên trường cơ sở dữ liệu.
     Ví dụ: service_provided, PER_PAGE,...

e) Mình thường sử dụng Snake Case hoặc Camel Case làm phong cách đặt tên biến. Tuy nhiên vẫn sử dụng các phong cách
đặt tên khác để giúp phân biệt các biến đã đặt, giúp rõ nghĩa, tiết kiệm thời gian khi đọc code."""