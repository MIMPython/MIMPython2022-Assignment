def file(full_name, week, assignment):
    file_name = week + "_" + assignment + "_" + full_name
    return file_name


week = "week02"
assignment = "assignment03"
full_name = "MaiVuHoangLam"
print(file(full_name, week, assignment))