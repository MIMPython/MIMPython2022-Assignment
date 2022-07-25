def hocvien(name, week, assignment, id):
    name = name.strip()
    n = name.split()
    name1 = ""
    for i in n:
        name1 += i
    if week <= 9:
        week = "0" + str(week)
    if assignment <= 9:
        assignment = "0" + str(assignment)
    print(week + str(week) + "_" + "assigment" + str(assignment) + "_" + "student" + id + "_" + name1 + ".py")    
    

if __name__ == '__main__':
    name = str(input("Input name: "))
    week = int(input("Input week of assignment: "))
    assignment = int(input("Input number of assignment: "))
    id = int(input("Input your ID: "))    
    hocvien(name, week, assignment, id)