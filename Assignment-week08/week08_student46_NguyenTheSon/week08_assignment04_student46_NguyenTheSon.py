import pandas as pd

# Bài 4:
# a)
name_student = ['Son', 'An', 'Binh', 'Chi', 'Dung', 'Giang', 'Hoa', 'Kien', 'Linh', 'Mai', 'Ngoc', 'Oc', 'Quynh','Sam', 'Tien']
class_student = ['K64', 'K65', 'K63', 'K64', 'K66','K63', 'K64', 'K62', 'K66', 'K63', 'K64','K64', 'K63', 'K65', 'K66']
score_student = [8.8, 7.2, 9.2, 8.2, 5.6, 4.3, 9.2, 6.7, 7.6, 5.6, 7.8, 8.4, 7.3, 5.6, 6.9]

info_student = pd.DataFrame({'name': name_student, 'class': class_student, 'score': score_student})

# b)
# Tạo ra danh sách các lớp 
list_class = []
for i in class_student:
    if i not in list_class:
        list_class.append(i)

# Đếm số học sinh trong 1 lớp 

count_student = 0
list_student = []
for i in list_class:
    number_student = class_student.count(i)
    list_student.append(number_student)
    count_student += number_student
    if count_student == len(class_student):
        break

# Tính điểm trung bình

mean_score = []
for i in list_class:
    x = info_student[info_student['class'] == i]
    mean_score_student = round((x['score'].mean()), 1)
    mean_score.append(mean_score_student)


data_frame = pd.DataFrame({'class': list_class, 
                           'number of Student': list_student,
                           'mean score': mean_score}).sort_values('class')

print(data_frame)