def file():
	name = str(input("Nhap ten cua ban: "))
	week_no = int(input("Nhap so thu tu tuan hoc: "))
	task_no = int(input("Nhap so thu tu bai tap: "))
	print("\nweek" + str(week_no) + ".assignment" + str(task_no) + "." + name.replace(" ", "") + ".py")

file()