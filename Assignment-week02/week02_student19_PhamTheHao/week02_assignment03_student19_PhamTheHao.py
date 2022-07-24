"""
Bài tập 3. Viết một hàm nhận vào tên học viên (kiểu string), số thứ tự tuần học 
(kiểu nguyên), số thứ tự bài tập (kiểu nguyên) và trả về tên file .py tương ứng.
"""
student_name = input("Student's name: ")
week = input("Week: ")
assignment = input("Assignment: ")
student_name_title = student_name.title().replace(' ','')
print(f"File's name: week{week}_assignment{assignment}_{student_name_title}")