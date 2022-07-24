def student_iformation():
    student_name = input("Enter student name: ") # Enter: Nguyen Van A
    student_name = student_name.replace(" ","") # remove spaces
    week_number = int(input("Enter week number: ")) # Enter: 4
    assignment_number = int(input("Enter assignment number: ")) # Enter: 2
    print (f"week{week_number}_assignment{assignment_number}_{student_name}.py") # Output: week4_assignment2_NguyenVanA.py

student_iformation()