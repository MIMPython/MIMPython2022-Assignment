def getFileName(student_name, week_number, assignment_number):
    fileName = "week{0:0>2}_assignment{1:0>2}_{2}".format(week_number, assignment_number, student_name)
    return fileName

if __name__ == '__main__':
    print(getFileName("LeTuanDat", 2, 7))  #week02_assignment07_LeTuanDat
    print(getFileName("LeTuanDat", 2, 8))  #week02_assignment08_LeTuanDat
    print(getFileName("LeTuanDat", 2, 9))  #week02_assignment09_LeTuanDat