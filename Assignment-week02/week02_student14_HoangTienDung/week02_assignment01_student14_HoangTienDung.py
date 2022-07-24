#a
Những kí tự không được phép xuất hiện trong tên biến trong Python: @, $, !, %,...
#b
Tên biến hợp lệ: man
Tên biến không hợp lệ: m@n
#c
Trong trường hợp chỉ sử dụng 1 biến index ta có thể đặt tên biến là "i". Mặt khác, nếu có thêm biến mới là integer thì ta nên đặt tên 2 biến rõ ràng hơn. Ví dụ là "index" và "int".
#d
"numberofcollegestudents" và "NUMBEROFCOLLEGESTUDENTS": 2 phong cách này gần như là tương đồng, đều là chữ viết thường hoặc chữ viết hoa cạnh nhau và điểm chung giữa chúng là khá khó đọc.
"numberOfCollegeStudents" và "NumberOfCollegeStudents": 2 phong cách này đã được viết hoa chữ cái đầu tiên của từ nên việc đọc biến sẽ dễ hơn.
"number_of_college_students": giữa các từ có dấu "_" nên việc đọc lại càng dễ hơn các phong cách trên.
#e
Camel Case: kết hợp các từ bằng cách viết hoa tất cả các từ sau từ đầu tiên và xóa không gian. ("numberOfCollegeStudents")
Pascal Case: kết hợp các từ bằng cách viết hoa tất cả các từ và xóa khoảng cách. ("NumberOfCollegeStudents")
Snake Case: kết hợp các từ bằng cách thay thế từng khoảng trắng bằng dấu "_" và, với kiểu tất cả đều viết hóa, tất cả các chữ cái được viết hoa. ("number_of_college_students")
#f
Em chọn phong cách đặt tên biến là "Snake Case" để mọi người có thể đọc code thuận tiện hơn. 