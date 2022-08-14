def toString(number):
    str_num = str(number)
    if (number < 10):
        str_num = '0' + str_num
    return str_num

def fileName(week, assignment, id, name):
    str_week = toString(week)
    str_assignment = toString(assignment)
    str_id = toString(id)
    name = name.title()
    file = f'week{str_week}_assignment{str_assignment}_student{str_id}_{name}.py'
    return file.replace(" ", "")

if __name__ == "__main__":
    print(fileName(2, 3, 19, 'nGuyen Thi hONG dIep')) # week02_assignment03_student19_NguyenThiHongDiep.py
