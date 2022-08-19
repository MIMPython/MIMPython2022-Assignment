import sys

def convert(number):
            str_num = str(number)
            if number < 10:
                str_num = '0' + str_num
            return str_num

def print_filename(name, student_id, week_id, assignment_id):
    # Both week_id and assignment_id are 1 or 2-digit numbers
    limit = range(1, 100)
    if student_id in limit and week_id in limit and assignment_id in limit:
        w_id = convert(week_id)
        a_id = convert(assignment_id)
        s_id = convert(student_id)   

        print(f'week{w_id}_assignment{a_id}_student{s_id}_{name}.py')
    else:
        print('student id or week id or assignment id is out of range.')
        print(name, student_id, week_id, assignment_id)

if __name__ == "__main__":
    print_filename('PhungThiThuAn', 1, 5, 6) # week05_assignment06_student01_PhungThiThuAn.py
    print_filename(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]))
    
    # Nhập vào Terminal dòng lệnh dưới và đc kết quả:s
# python week05_assignment06_student01_PhungThiThuAn.py PhungThiThuAn 1 3 4
# week03_assignment04_student01_PhungThiThuAn.py