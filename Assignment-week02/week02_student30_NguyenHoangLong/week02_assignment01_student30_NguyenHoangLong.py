print("a) Các ký tự đặc biệt như @, $ ,%,... và khoảng trắng không được phép xuất hiện trong tên biến trong Python")
print("\nb) \nVí dụ về tên biến hợp lệ: Student_name\nVí dụ về tên biến không hợp lệ: Student_name@")
print("\nc) \nVí dụ về đặt tên biến tốt name_of_rubik_brands. \nTên biến này dùng trong tình huống ta muốn tìm hiểu về các hãng rubik mà các cuber sử dụng trong một cuộc thi của WCA.")
print("\nd)")
name = ["numberofcollegestudents", "NUMBEROFCOLLEGESTUDENTS", "numberOfCollegeStudents", "NumberOfCollegeStudents", "number_of_college_students"]
style = ["Lower Case", "Upper Case", "Camel Case", "Pascal Case", "Snake Case"]
for i in range(0,5):
	print(f"{name[i]} là phong cách {style[i]}")
	
print("\ne)")
print("Snake Case: sử dụng dấu gạch chân giữa các từ, tất cả các từ đều viết thường, ví dụ: nguyen_hoang_long")
print("camel Case: giống như cách viết của nó, từ đầu tiên viết thường, các từ tiếp theo viết hoa chữ cái đầu, ví dụ: nguyenHoangLong")
print("Pascal Case: viết hoa tất cả các chữ cái đầu, ví dụ: NguyenHoangLong")
print("\nf) \nEm chọn phong cách đặt tên biến là Snake Case")
