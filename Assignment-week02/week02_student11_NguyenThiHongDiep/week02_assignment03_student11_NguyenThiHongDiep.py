name = str(input('Ten hoc vien: '))
week = int(input('So thu tu tuan hoc: '))
assignment = int(input('So thu tu bai tap: '))

name = name.title()
str_week = str(week)
str_assignment = str(assignment) 

if week < 10:
    str_week = '0' + str_week
if assignment < 10:
    str_assignment = '0' + str_assignment

fileName = 'week' + str_week + '_assignment' + str_assignment + '_' + name + '.py'
print('File .py tuong ung la:', fileName.replace(" ", ""))

# Ten hoc vien: nGUYEn tHI HOnG dieP
# So thu tu tuan hoc: 23
# So thu tu bai tap: 6
# File .py tuong ung la: week23_assignment06_NguyenThiHongDiep.py

# Ten hoc vien: nguyEn ThI bao phuC
# So thu tu tuan hoc: 15
# So thu tu bai tap: 11
# File .py tuong ung la: week15_assignment11_NguyenThiBaoPhuc.py

# Ten hoc vien: Nguyen thi bAo LOC
# So thu tu tuan hoc: 6
# So thu tu bai tap: 2
# File .py tuong ung la: week06_assignment02_NguyenThiBaoLoc.py