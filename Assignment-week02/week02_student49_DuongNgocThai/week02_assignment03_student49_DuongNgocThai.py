#Bài 3    
def fileName(name_student, week, stt_ex):
    return name_student + "_week" + str(week) + "_stt" + str(stt_ex) + ".py"

print(fileName("Thai", 2, 3)) # Thai_week2_stt3.py
print(fileName("Duc", 3, 21)) # Duc_week3_stt21.py
