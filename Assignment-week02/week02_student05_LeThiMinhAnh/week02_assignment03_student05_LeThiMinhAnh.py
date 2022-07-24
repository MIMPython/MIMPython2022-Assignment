def fileName(studentName, week, assignment):
    if week < 10:
        week = "0"+str(week)
    if assignment < 10:
        assignment = "0"+str(assignment)
    return f"week{week}_assignment{assignment}_{studentName}.py"


print(fileName("LeThiMinhAnh", 2, 3))  # week02_assignment03_LeThiMinhAnh.py
print(fileName("LeThiMinhAnh", 10, 3))  # week10_assignment03_LeThiMinhAnh.py
print(fileName("LeThiMinhAnh", 5, 12))  # week05_assignment12_LeThiMinhAnh.py
print(fileName("LeThiMinhAnh", 10, 15))  # week10_assignment15_LeThiMinhAnh.py
