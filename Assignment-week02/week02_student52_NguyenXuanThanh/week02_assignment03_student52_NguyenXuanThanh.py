def Exercise(name, week, assignment):
    if (week < 10):
        week_i = 0
    else: 
        week_i =""    

    if (assignment< 10):
        assignment_j = 0
    else: 
        assignment_j = ""

    print("week",week_i,week,"_assignment",assignment_j,assignment,"_",name,".py",sep = "")

Exercise("NguyenXuanThanh",11,2) #week11_assignment02_NguyenXuanThanh.py
Exercise("TranThanhTung",11,99) #week11_assignment99_TranThanhTung.py
Exercise("NguyenVanQuan",1,2) #week01_assignment02_NguyenVanQuan.py

