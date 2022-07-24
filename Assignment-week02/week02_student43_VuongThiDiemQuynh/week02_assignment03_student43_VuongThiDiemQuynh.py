#Viết một hàm nhận vào tên học viên (kiểu string), số thứ tự tuần học (kiểu nguyên), số thứ tự bài tập (kiểu nguyên) và trả về tên file .py tương ứng.

def file_name():
    name = str(input('Enter your name\n'))
    week = int(input('Enter your study week\n'))
    assignment = int(input('Enter your number of assignment\n'))
    return('week',week,'_','assignment',assignment,'_',name,'.py')

file_name()