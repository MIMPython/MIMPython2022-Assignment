"""
Bài tập 1:
a) Những ký tự nào không được phép xuất hiện trong tên biến trong Python?
    TL: Tất cả các ký tự không phải là chữ cái, số và dấu gạch dưới.
b) Cho ví dụ về tên biến hợp lệ và ví dụ về tên biến không hợp lệ.
    TL: Tên hợp lệ: variable_names
    Tên không hợp lệ:  variable names
c) Hãy cho ví dụ về cách đặt tên biến tốt kèm theo tình huống sử dụng những biến này.
    TL: Ta cần một biến để lưu trữ họ và tên một người, thay vì chỉ đặt tên biến là 
    'name' thì ta đặt là 'full_name' để mô tả rõ ràng, đầy đủ hơn.
"""
first_name = 'Hao'
last_name = 'Pham'
full_name = f"{first_name} {last_name}"
print(full_name)

"""
d) Cho danh sách những tên biến có cùng ý nghĩa thể hiện số sinh viên, Hãy mô tả 
các phong cách đặt những tên biến sau
    - numberofcollegestudents: tất cả viết thường liền nhau -> Khó phân biệt giữa 
    các từ, gây khó hiểu.
    - NUMBEROFCOLLEGESTUDENTS: tất cả viết hoa liền nhau -> Khó phân biệt giữa các
    từ, gây khó hiểu.
    - numberOfCollegeStudents: chữ cái đầu tiên của từng từ được viết hoa (trừ từ
    đầu tiên) giúp ta phân biệt được giữa các từ -> Dễ hiểu.
    - NumberOfCollegeStudents: chữ cái đầu tiên của từng từ được viết hoa giúp ta 
    phân biệt được giữa các từ -> Dễ hiểu.
    - number_of_college_students: các từ được phân biệt với nhau bởi dấu gạch dưới
    -> dễ đọc, dễ hiểu.
e) Phân biệt các phong cách đặt tên biến Camel Case, Pascal Case và Snake Case. 
Cho ví dụ.
    - Camel Case: tất cả các từ viết liền nhau và viết hoa chữ cái đầu tiên (trừ từ 
    đầu tiên). Ví dụ: variableNames.
    - Pascal Case: tất cả các từ viết liền nhau và viết hoa chữ cái đầu tiên.
    Ví dụ: VariableNames.
    - Snake Case: tất cả các chữ cái viết thường, giữa hai từ liên tiếp là dấu gạch 
    dưới. Ví dụ: variable_names.
f) Bạn chọn phong cách đặt tên biến nào?
    TL: phong cách Snake Case.

"""

