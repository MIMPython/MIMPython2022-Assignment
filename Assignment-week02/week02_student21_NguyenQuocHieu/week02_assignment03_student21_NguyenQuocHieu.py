week = input("Nhap vao so thu tu cua tuan: ")
assignment = input("Nhap vao so thu tu bai tap: ")
name = input("Nhap vao ten cua ban: ")
if (int(week) < 10): weekOff = "0" + str(week)
if (int(assignment) < 10): assignmentOff = "0" + str(assignment)
string = "week_" + str(weekOff) + "assignment_" + str(assignmentOff) + "student21_" + str(name) + ".py"
print("Ten file bai tap cua ban hoc sinh la: ", string)
