#  Câu 3: Viết một hàm nhận vào tên học viên (kiểu string), số thứ tự tuần học (kiểu nguyên), số thứ tự bài tập (kiểu nguyên) và trả về tên file .py tương ứng.
import sys
# hàm thực hiện trả về tên file


def getFileName(nameStudent, week, assingment):
    week = int(week)
    assingment = int(assingment)
    nameStudent = nameStudent.replace(" ", "")
    return 'week' + f"{week:02d}" + '_assingment' + f"{assingment:02d}" + '_' + nameStudent + '.py'


# main
if __name__ == '__main__':
    print(getFileName(sys.argv[1], sys.argv[2], sys.argv[3]))
