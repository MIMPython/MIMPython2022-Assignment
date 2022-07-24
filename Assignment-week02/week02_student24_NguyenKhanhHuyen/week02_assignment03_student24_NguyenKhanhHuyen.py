def filename():
    print("Nhập tên học viên:")
    name= str(input())
    name1=name.replace(' ','')
    print("Nhập số thứ tự tuần học:")
    week_num= str(input())
    print("Nhập số thứ tự bài tập:")
    assign_num = str(input())
    file= "week" + week_num + "_" + "assignment" + assign_num + "_" + name1 + ".py"
    return file

print(filename())