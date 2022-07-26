# Viết một hàm nhận vào tên học viên (kiểu string), số thứ tự tuần học (kiểu nguyên), số thứ tự bài tập (kiểu nguyên) và trả về tên file .py tương ứng.
from asyncore import file_dispatcher


def student(name, id_week, id_exercise):
    file_name = 'week' + "%02d" % id_week + "_" + 'exercise' + '%02d' %id_exercise + "_" + name + '.py'
    return file_name
