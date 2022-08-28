import pandas as pd
import ast
import numpy as np

file_exam = pd.read_csv('additionalFolder/TimeTablingDataset/exam_another.csv')
file_exam.head()
file_exam = pd.DataFrame(file_exam)
file_exam = file_exam.values.tolist()

#DF1
MMH_1 = [] # Mã môn học
MLH_1 = [] # Mã lớp học
MSV_1 = [] # Mã sinh viên

#DF2
MLH_2 = []
MSV_2 = []
num_of_student_2 = []

#DF3
MMH_3 = []
MSV_3 = []
num_of_student_3 = []

#solve
for listSubClassCode in file_exam:
  classCodes = ast.literal_eval(listSubClassCode[1]) # MLHs
  MSV_3_temp = []
  for code in classCodes:
    df = pd.read_csv('additionalFolder/TimeTablingDataset/examinationTimetablingDataset/' + code + '.csv')
    MSVs = df['MSV'].tolist()
    MSV_3_temp.extend(MSVs)

    # 2
    MLH_2.append(code)
    MSV_2.append(MSVs)
    num_of_student_2.append(len(MSVs))
    # 1
    for msv in MSVs:
      MSV_1.append(msv)
      MMH_1.append(listSubClassCode[0])
      MLH_1.append(code)
    
  #3
  MMH_3.append(listSubClassCode[0])
  MSV_3_temp.sort()
  MSV_3.append(MSV_3_temp)
  #num_of_student_3.append(len(MSV_3_temp))



#out_csv
#df1
df1 = pd.DataFrame({'MSV': MSV_1, 'Ma_Lop_Hoc': MLH_1, 'Ma_Mon_Hoc': MMH_1})
df1 = df1.sort_values(by=['MSV','Ma_Lop_Hoc'],ignore_index= True)
df1.to_csv('additionalFolder/week06_assignment06_student06_NguyenNgocAnh_DataFrame_1.csv', index= False)

#df2
df2 = pd.DataFrame({'Ma_Lop_Hoc': MLH_2, 'list_MSV': MSV_2, 'So_Luong': num_of_student_2})
df2.to_csv('additionalFolder/week06_assignment06_student06_NguyenNgocAnh_DataFrame_2.csv', index= False)

#df3
MSV3_filt = []
for msvs in MSV_3:
  msv_temp = []
  for msv in msvs:
    if msv not in msv_temp:
      msv_temp.append(msv)
  MSV3_filt.append(msv_temp)
  num_of_student_3.append(len(msv_temp))


df3 = pd.DataFrame({'Ma_Mon_Hoc': MMH_3, 'list_MSV': MSV3_filt, 'So_Luong': num_of_student_3})
df3.to_csv('additionalFolder/week06_assignment06_student06_NguyenNgocAnh_DataFrame_3.csv', index= False)

#4
student = ''
MLH_4_temp = []
MMH_4_temp = []
MSV_4 = []
MLH_4 = []
MMH_4 = []
MSV4s = df1
MSV4s = MSV4s.values.tolist()
for msv in MSV4s:
    if msv[0] != student:
        student = msv[0]
        MSV_4.append(student)
        if student != '':
            MLH_4_temp = []
            MMH_4_temp = []
        MLH_4_temp.append(msv[1]) 
        MMH_4_temp.append(msv[2])
        MLH_4.append(MLH_4_temp)
        MMH_4.append(MMH_4_temp)
    else:
        MLH_4_temp.append(msv[1]) 
        MMH_4_temp.append(msv[2])
#df4
df4 = pd.DataFrame({'MSV': MSV_4, 'list_Ma_Lop_Hoc': MLH_4, 'list_Ma_Mon_Hoc': MMH_4})
df4.to_csv('additionalFolder/week06_assignment06_student06_NguyenNgocAnh_DataFrame_4.csv', index= False)

#df5

# thống kê:
df_stati = df4
df_stati = df_stati.values.tolist()

#MSV| mã môn riêng | số lượng môn riêng | mã môn chung | số lượng lớp chung mã môn
stati_MSV = []
stati_list_Ma_Mon_Hoc = [] #list MMH không trùng nhau
stati_so_luong_mon = [] #số lượng môn không trùng nhau
stati_MMH_chung = [] #trùng lớp
stati_so_luong_lop_trung = [] #số lượng lớp bị trùng

for df_sta in df_stati:

  stati_MSV.append(df_sta[0])
  mmh_rieng = []
  mmh_chung = []

  for mmh in df_sta[2]:
    if mmh in mmh_rieng:
      if mmh not in mmh_chung:
        mmh_chung.append(mmh)
    else:
      mmh_rieng.append(mmh)

  stati_list_Ma_Mon_Hoc.append(mmh_rieng)
  stati_so_luong_mon.append(len(mmh_rieng))
  stati_MMH_chung.append(mmh_chung)
  stati_so_luong_lop_trung.append(len(df_sta[2]) - len(mmh_rieng))

stati_df = pd.DataFrame({'MSV': stati_MSV, 'Ma_Mon_Hoc_rieng': stati_list_Ma_Mon_Hoc, 'So_luong_mon_rieng': stati_so_luong_mon, 
'Ma_Mon_chung': stati_MMH_chung, 'So_luong_lop_trung': stati_so_luong_lop_trung})
stati_df.to_csv('additionalFolder/week06_assignment06_student06_NguyenNgocAnh_Statistics_1.csv', index= False)


# file
statistics_output_file = open('additionalFolder/week06_assignment06_student06_NguyenNgocAnh_Statistics.txt','w')
#Số sinh viên:
total_student = len(stati_df['MSV'])
statistics_output_file.write(f'Tong so sinh vien: {total_student}\n')
#Số lớp học:
total_class = len(df2['Ma_Lop_Hoc'])
statistics_output_file.write(f'Tong so lop hoc: {total_class}\n')
#Số môn học:
total_subject = len(df3['Ma_Mon_Hoc'])
statistics_output_file.write(f'Tong so mon hoc: {total_subject}\n')
#Số môn trung bình 1 sv đăng ký
mean_subject = np.mean(stati_df['So_luong_mon_rieng'])
statistics_output_file.write(f'So mon trung binh 1 sv dang ki: {mean_subject}\n')
#Môn học có nhiều (hoặc ít) sinh viên đăng ký nhất.
#min
subject_min_student = df3[df3['So_Luong']==df3['So_Luong'].min()]
subject_min_student.to_csv('additionalFolder/week06_assignment06_student06_NguyenNgocAnh_Statistics_subject_min_student.csv', index= False)
# max
subject_max_student = df3[df3['So_Luong']==df3['So_Luong'].max()]
subject_max_student.to_csv('additionalFolder/week06_assignment06_student06_NguyenNgocAnh_Statistics_subject_max_student.csv', index= False)
# Sinh viên đăng ký nhiều môn học nhất:
student_join_max_class = stati_df[stati_df['So_luong_mon_rieng']==stati_df['So_luong_mon_rieng'].max()]
student_join_max_class.to_csv('additionalFolder/week06_assignment06_student06_NguyenNgocAnh_Statistics_student_max_class.csv', index= False)
# Sinh viên đăng ký ít môn học nhất:
student_join_min_class = stati_df[stati_df['So_luong_mon_rieng']==stati_df['So_luong_mon_rieng'].min()]
student_join_min_class.to_csv('additionalFolder/week06_assignment06_student06_NguyenNgocAnh_Statistics_student_min_class.csv', index= False)

# Sinh viên đăng ký học 2 lớp chung 1 mã môn:
join_2_class_same_subject = stati_df[stati_df['So_luong_lop_trung'] > 0]
join_2_class_same_subject.to_csv('additionalFolder/week06_assignment06_student06_NguyenNgocAnh_Statistics_student_2_class_same_subject.csv', index= False)
