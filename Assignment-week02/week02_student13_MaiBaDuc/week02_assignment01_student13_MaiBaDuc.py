'''
Bài tập 1. Hãy trả lời những câu hỏi, thực hiện những yêu cầu sau đây
(a) Những kí tự nào không được phép xuất hiện trong tên biến trong Python?

    False   class   finally is  return
    None    continue    for lambda  try 
    True    def from    nonlocal    while
    and del global  not with    
    as  elif    if  or  yield   
    assert  else    import  pass
    break   except  in  raise

(b) Cho ví dụ về tên biến hợp lệ và ví dụ về tên biến không hợp lệ.

    Biến hợp lệ: var_1
    Biến không hợp lệ: 1_var

(c) Khi nói đến việc đặt tên biến, tác giả Robert C. Martin viết trong cuốn sách Clean Code: A Handbook of Agile Software Craftsmanship viết
It is easy to say that names should reveal intent. What we want to impress upon you is that we are serious about this. Choosing good names takes time but saves more than it takes. So take care with your names and change them when you find better ones. Everyone who reads your code (including you) will be happier if you do.
The name of a variable should answer all the big questions. It should tell you why it exists, what it does, and how it is used. If a name requires a com- ment, then the name does not reveal its intent.
Hãy cho ví dụ về cách đặt tên biến tốt kèm theo tình huống sử dụng những biến này.
 
lst_name = ['tom', 'john', 'kerry']
lst_class = ['TK22', 'TK21', 'HK22']
stu_1 = f"{lst_name[0].title()}-{lst_class[0]}"

(d) Cho danh sách những tên biến có cùng ý nghĩa thể hiện số sinh viên
•	numberofcollegestudents
•	NUMBEROFCOLLEGESTUDENTS
•	numberOfCollegeStudents
•	NumberOfCollegeStudents
•	number_of_college_students
Hãy mô tả các phong cách đặt những tên biến trên.

numberofcollegestudents             Lower case
NUMBEROFCOLLEGESTUDENTS             Up case  
numberOfCollegeStudents             Camel Case 
NumberOfCollegeStudents             Pascal case
number_of_college_students          Snake case

(e) Phân biệt các phong cách đặt tên biến Camel Case, Pascal Case và Snake Case. Cho ví dụ.

    Camel case: chữ cái đầu tiên của từ được in hoa (trừ từ đầu tiên trong tên biến). Ví dụ: numberOfCollegeStudents
    Pascal case: chữ cái đầu tiên được in hoa trong mỗi từ. Ví dụ: NumberOfCollegeStudents
    Snake case: dùng dấu gạch dưới '_' phân cách giữa các từ. Ví dụ: number_of_college_students
    
(f) Bạn chọn phong cách đặt tên biến nào?
    Em chọn Snake case vì thấy tiện và đẹp.
'''