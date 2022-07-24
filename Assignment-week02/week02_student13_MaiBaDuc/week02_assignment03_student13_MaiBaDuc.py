'''
Bài tập 3. Viết một hàm nhận vào tên học viên (kiểu string), 
số thứ tự tuần học (kiểu nguyên), số thứ tự bài tập (kiểu nguyên) và trả về tên file .py tương ứng.
'''
def func_1():
    name = input("Name: ")
    week = int(input("Week: "))
    assignment = int(input("Assignment: "))
    result = f"week{week}_assignment{assignment}_{name}.py"
    print(result)
func_1()
