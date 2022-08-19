import sys

def namingAssignments(studentName: str, week: int, assignment: int):
    # kết quả gồm 3 thành phần s w a ta chuyển hết về str để thuận tiện cho việc ghép nối
    s = studentName.upper()
    s = studentName.title().replace(' ', '')
    w = ''
    a = ''

    if (0 < week < 10):
        w = 'week0' + str(week)
    elif week >= 10:
        w = 'week1' + str(week)
    else:
        return "error"

    if (0 < assignment < 10):
        a = 'assignment0' + str(assignment)
    elif assignment >= 10:
        a = 'assignment1' + str(assignment)
    else:
        return "error"

    return w + '_' + a + '_' + s + '.py'

if __name__ == '__main__':
    s = sys.argv[1]
    w = int(sys.argv[2])
    a = int(sys.argv[3])
    print(namingAssignments(s,w,a))