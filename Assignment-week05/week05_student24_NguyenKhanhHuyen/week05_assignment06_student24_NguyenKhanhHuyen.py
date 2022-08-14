import sys

def fileName(stuName, stuID, weekID, assignmentIndex):
    if stuID < 10:
        stuID = '0' + str(stuID)

    if weekID < 10:
        weekID = '0' + str(weekID)

    if assignmentIndex < 10:
        assignmentIndex = '0' + str(assignmentIndex)

    print(f"week{weekID}_assignment{assignmentIndex}_student{stuID}_{stuName}.py") 
name = sys.argv[1]
stuID = (int) (sys.argv[2])
weekID = (int) (sys.argv[3])
assignmentIndex = (int) (sys.argv[4])
fileName(name, stuID, weekID, assignmentIndex)
#python .\week05_assignment06_student24_NguyenKhanhHuyen.py NguyenKhanhHuyen 2 2 2: week02_assignment02_student02_NguyenKhanhHuyen.py
#python .\week05_assignment06_student24_NguyenKhanhHuyen.py NguyenKhanhHuyen 25 6 3: week06_assignment03_student25_NguyenKhanhHuyen.py