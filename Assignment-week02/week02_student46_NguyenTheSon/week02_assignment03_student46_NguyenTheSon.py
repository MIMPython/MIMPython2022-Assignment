#Bài 3:
def name_file(name, week, assignment):
    if week < 10 and assignment < 10:
        a = 'week0' + str(week) + '_assignment0' +  str(assignment) + '_' + name.title() + '.py'
    elif week < 10:
        a = 'week0' + str(week) + '_assignment' +  str(assignment) + '_' + name.title() + '.py'
    elif assignment < 10:
        a = 'week' + str(week) + '_assignment0' +  str(assignment) + '_' + name.title() + '.py'
    else: 
        a = 'week' + str(week) + '_assignment' +  str(assignment) + '_' + name.title() + '.py'
    return a
if __name__ == '__main__':
    print(name_file('nguyentheson', 2, 3)) #week02_assignment03_Nguyentheson.py
    print(name_file('nguyentheson', 14, 5)) #week14_assignment05_Nguyentheson.py
    print(name_file('nguyentheson', 6, 11)) #week06_assignment11_Nguyentheson.py

