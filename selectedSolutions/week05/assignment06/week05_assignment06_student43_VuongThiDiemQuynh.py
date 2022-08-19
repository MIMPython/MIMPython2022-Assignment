'''
Bài tập 6. (command line arguments)
Thực hiện lại bài tập 3 của tuần 2 với việc thực thi chương trình kèm với đối số truyền qua dòng lệnh. Chú ý tên file nộp phải ghi đúng quy tắc (là bài tập 6 tuần 5).
'''

#Viết một hàm nhận vào tên học viên (kiểu string), số thứ tự tuần học (kiểu nguyên), số thứ tự bài tập (kiểu nguyên) và trả về tên file .py tương ứng.

import sys 

# usage: enter <Your Name>, <Number of week> and <Number of assignment> respectively.

name = None
numberOfWeek = 0
numberOfAssignment = 0

if len(sys.argv) < 2:
    print('Needs at least one argument')
    exit()

name = sys.argv[1]
numberOfWeek = sys.argv[2]
numberOfAssignment = sys.argv[3]

if __name__ == "__main__":
    print('week0',numberOfWeek,'_','assignment0',numberOfAssignment,'_',name,'.py')
# Command line: /usr/bin/python3 "/Users/macbook/Desktop/MIM Python/week05_student43_VuongThiDiemQuynh/test.py" VuongThiDiemQuynh 5 6  
# Output: week0 5 _ assignment0 6 _ VuongThiDiemQuynh .py