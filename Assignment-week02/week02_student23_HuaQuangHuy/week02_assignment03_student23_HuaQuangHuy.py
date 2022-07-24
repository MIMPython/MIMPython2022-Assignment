#  Câu 3: Viết một hàm nhận vào tên học viên (kiểu string), số thứ tự tuần học (kiểu nguyên), số thứ tự bài tập (kiểu nguyên) và trả về tên file .py tương ứng.

# hàm thực hiện trả về tên file
def getFileName(nameStudent, week, assingment):
    if type(nameStudent) is str and type(week) is int and type(assingment) is int:
        if week < 10:
            week = '0' + str(week)
        if assingment < 10:
            assingment = '0' + str(assingment)
        nameStudent = nameStudent.replace(" ", "")

        return 'week' + str(week) + '_assingment' + str(assingment) + '_' + nameStudent + '.py'
    else:
        print('Chưa nhập đúng kiểu dữ liệu')


# main
if __name__ == '__main__':
    # week03_assingment04_HuaQuangHuy.py
    print(getFileName(' Hua Quang Huy ', 3, 4))
    # week10_assingment11_HuaQuangHuy.py
    print(getFileName(' Hua Quang Huy ', 10, 11))
    # Chưa nhập đúng kiểu dữ liệu
    print(getFileName(' Hua Quang Huy ', 3.5, 4))
