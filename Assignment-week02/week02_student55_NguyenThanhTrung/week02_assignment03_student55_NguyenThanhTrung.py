
def findCorrespondingFile(name, weekNum, assignmentNum, studentNum) :
    fileName = "week{weekNum}_assignment{assignmentNum}_student{studentNum}_{name}.py"
    return fileName.format(weekNum = weekNum, assignmentNum = assignmentNum, studentNum = studentNum, name = name)

if __name__ == '__main__' :
    print(findCorrespondingFile("NguyenThanhTrung", 2, 3, 55 ))