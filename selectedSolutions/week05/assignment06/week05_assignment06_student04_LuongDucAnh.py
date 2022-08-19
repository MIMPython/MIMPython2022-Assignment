import sys
def checkNum(num):
    num = int(num)
    if int(num) < 10:
        return f"0{num}"
    else:
        return f"{num}"
        
def getName(*args):
    name = args[0].lower().title().replace(" ", "")
    studentIndex = checkNum(args[1])
    weekIndex = checkNum(args[2])
    assignmentIndex = checkNum(args[3])
    return f"week{weekIndex}_assignment{assignmentIndex}_student{studentIndex}_{name}.py"

print(getName(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]))

#python week05_assignment06_student04_LuongDucAnh.py "Luong     duc   anh" 4 5 6
#week05_assignment06_student04_LuongDucAnh.py