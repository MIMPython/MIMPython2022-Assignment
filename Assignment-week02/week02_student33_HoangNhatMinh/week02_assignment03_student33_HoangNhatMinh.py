def namingAssignments(studentName: str, week: int, assignment: int) :
    # kết quả gồm 3 thành phần s w a ta chuyển hết về str để thuận tiện cho việc ghép nối
    s = studentName.upper()
    s = studentName.strip()
    s = studentName.title().replace(' ', '')
    w = ''
    a = ''
    
    if ( 0 < week < 10 ) : w = 'week0' + str(week)
    elif week >= 10 : w = 'week1' + str(week)
    else : return "error"

    if ( 0 < assignment < 10 ) : a = 'assignment0' + str(assignment)
    elif assignment >= 10 : a = 'assignment1' + str(assignment)
    else : return "error"

    return w + '_' + a + '_' + s

print(namingAssignments('hoang nhat minh', 1, 1)) #week01_assignment01_HoangNhatMinh
print(namingAssignments(' trAn tUan   vu ', 10, 100)) #week10_assignment100_TranTuanVu
print(namingAssignments('hoAng Hai aNh ', 10, 20)) #week10_assignment100_HoangHaiAnh
print(namingAssignments('hoAng Hai aNh ', 10, -20)) #error