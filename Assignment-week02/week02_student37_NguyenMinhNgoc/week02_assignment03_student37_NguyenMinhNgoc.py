def file_of_student(student_name, week_number, assignment_number):
    file_name = ""
    if week_number < 10:
        file_name = "week0" + str(week_number) + "_assignment" + str(assignment_number) + "_" + student_name
    if assignment_number < 10:
        file_name = "week" + str(week_number) + "_assignment0" + str(assignment_number) + "_" + student_name
    if (week_number < 10) and (assignment_number < 10):
        file_name = "week0" + str(week_number) + "_assignment0" + str(assignment_number) + "_" + student_name
    return file_name
print(file_of_student("NguyenMinhNgoc", 2, 10))
print(file_of_student("NguyenMinhNgoc", 11, 3))
print(file_of_student("NguyenMinhNgoc", 2, 3))

"""
week02_assignment10_NguyenMinhNgoc
week11_assignment03_NguyenMinhNgoc
week02_assignment03_NguyenMinhNgoc
"""