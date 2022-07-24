print("a) \nKhoảng trắng và những ký tự đặc biệt như @, %,... không được phép xuất hiện trong tên biến trong Python")
print("b) \nTên biến hợp lệ: week02_assignment01\nTên biến không hợp lệ: week02!_assignment01")
print("c) \nTên biến tốt: Name_of_Smartphone\nTình huống sử dụng: tìm hiểu về các dòng điện thoại đang được sử dụng phổ biến")
print("d) ")
name = ["numberofcollegestudents", "NUMBEROFCOLLEGESTUDENTS", "numberOfCollegeStudents", "NumberOfCollegeStudents", "number_of_college_students"]
style = ["Lower Case", "Upper Case", "Camel Case", "Pascal Case", "Snake Case"]
for i in range(0,5):
    print(f"{name[i]} là phong cách {style[i]}")
print("e) ")
print("Snake Case: Tất cả các từ đều viết thường, sử dụng dấu gạch chân giữa các từ\nVí dụ: week02_assignment01")
print("Camel Case: Từ đầu tiên viết thường, các từ tiếp theo viết hoa chữ cái đầu điên\nVí dụ: week02Assignment01")
print("Pascal Case: Viết hoa tất cả các chữ cái đầu tiên của các từ\nVí dụ: Week02Assignment01")
print("f) \nPhong cách đặt tên lựa chọn: Snake Case")