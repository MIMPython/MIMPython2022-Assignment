# Bài tập 1. Hãy trả lời những câu hỏi, thực hiện những yêu cầu sau đây

# (a) Những kí tự nào không được phép xuất hiện trong tên biến trong Python?
# (b) Cho ví dụ về tên biến hợp lệ và ví dụ về tên biến không hợp lệ.
# (c) Khi nói đến việc đặt tên biến, tác giả Robert C. Martin viết trong cuốn sách Clean Code: A Handbook of Agile Software Craftsmanship viết

# It is easy to say that names should reveal intent. What we want to impress upon you is that we are serious about this. Choosing good names takes time but saves more than it takes. So take care with your names and change them when you find better ones. Everyone who reads your code (including you) will be happier if you do.
# The name of a variable should answer all the big questions. It should tell you why it exists, what it does, and how it is used. If a name requires a com- ment, then the name does not reveal its intent.

# Hãy cho ví dụ về cách đặt tên biến tốt kèm theo tình huống sử dụng những biến này.

# (d) Cho danh sách những tên biến có cùng ý nghĩa thể hiện số sinh viên

# numberofcollegestudents
# NUMBEROFCOLLEGESTUDENTS
# numberOfCollegeStudents
# NumberOfCollegeStudents
# number_of_college_students
# Hãy mô tả các phong cách đặt những tên biến trên.
# (e) Phân biệt các phong cách đặt tên biến Camel Case, Pascal Case và Snake Case. Cho ví dụ.
# (f) Bạn chọn phong cách đặt tên biến nào?

# a) Những kí tự không được phép xuất hiện trong tên biến trong Python : "@" , "$" , "%"
# b) + ví dụ về tên biến hợp lệ : "sum" ; "num" ; "temp";...
#    + ví dụ về tên biến không hợp lệ :"7up" ; "from" ;...
# c) Có những từ mà bản thân nó hàm chứa ý nghĩa không rõ ràng; kiểu như “do”, “prepare”, “get” ..v.v. 
#     Giả sử bạn muốn tải một layout từ internet về để xử lí,
#     Nếu chúng ta đặt tên hàm kiểu như "prepareLayout()" hoặc "getLayout()" thì rất khó để truyền tải được ý nghĩa thật sự của nó là gì.
#     vì vậy để tốt hơn là chúng ta nên đặt tên kiểu như "downloadLayout()", nếu muốn xoá trắng layout trước khi xử lí thì cái tên 
#     "clearLayout()" sẽ hợp lí hơn nhiều.
# d) Mô tả các phong cách đặt những tên biến :   
#     +) numberofcollegestudents và NUMBEROFCOLLEGESTUDENTS : 2 phong cách đặt tên này sẽ khiến mọi người khó dịch tên đc biến từ đó không biết biến sử dụng với mục đích gì
#     +) numberOfCollegeStudents : kiểu này thường được sử dụng như một quy ước trong khai báo biến
#     +) NumberOfCollegeStudents : kiểu này thường sử dụng như một quy ước trong việc khai báo các lớp 
#     +) number_of_college_students : kiểu này nên dùng để khai báo tên trường cơ sở dữ liệu
# e)    
#     Camel Case: từ đầu tiên viết thường, các từ tiếp theo viết hoa chữ cái đầu
#     PascalCase: viết hoa tất cả các chữ cái đầu
#     Snake Case : ngăng cách giữa các chữ bằng dấu gạch dưới (_) 
# f) tùy từng tình huống khi code thì nên sử dụng các phong cách cho hợp lí tạo cho code của mình sạch đẹp và dễ hiểu ! 

