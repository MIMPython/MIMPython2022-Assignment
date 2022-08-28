print("Bài 6: Examination Timetabling Analysis")
"""
+ File exams.csv chứa danh sách mã môn học (subjectCode) và các mã lớp học (classCode)
+ File nén examinationTimetablingDataset.zip chứa các file csv
với mỗi file có tên là một mã lớp học, nội dung mỗi file là danh sách mã sinh viên
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os

#Mã môn học và mã lớp
dataFrame = pd.read_csv(r'D:\MIM Python\week06_student58_TaQuangTung\additionalFolder\exams.csv')
print(dataFrame)
mamon = dataFrame["subjectCode"]        #Mã môn học
malop = dataFrame["classCode"]          #Mã lớp học



# Các mã sinh viên ứng với các môn học
pathtoFolder = r"D:\MIM Python\week06_student58_TaQuangTung\additionalFolder\examinationTimetablingDataset"

listFile = os.listdir(pathtoFolder)
fullPath = map(lambda name : os.path.join(pathtoFolder, name), listFile)
readerList = []             #Mỗi mã lớp có những sinh viên
classCodeList = []          #Các mã lớp học

for filePath in fullPath:
    reader = pd.read_csv(filePath)
    readerList.append(reader)
    classCodeList.append(os.path.basename(filePath).rstrip(".csv"))


#TẠO dataFrame1
studentMSV = ((readerList[0]).iloc[0])["MSV"]       #Chọn 1 sinh viên bất kỳ
MaLop = []
MaMon = []

for i in range(len(readerList)):        #Tìm kiếm mã lớp ứng với sinh viên trên
    dem = (readerList[i]).count()
    gt = dem['MSV']
    d = readerList[i]
    for j in range(gt):
        if (d.iloc[j])["MSV"] == studentMSV:
            MaLop.append(classCodeList[i])

lengthLop = len(MaLop)
for i in range(lengthLop):                  #Tìm kiếm mã môn ứng với mã lớp
    for j in range(malop.count()):
        if MaLop[i] in malop[j]:
            MaMon.append(mamon[j])

dataFrame1 = pd.DataFrame({"Mã sinh viên" : [studentMSV]*lengthLop,
                            "Mã lớp học" : MaLop,
                            "Mã môn học" : MaMon}) 
print("DataFrame1")
print(dataFrame1)  
print()       


#TẠO dataFrame2
MaLopHoc = classCodeList[0]     #Một mã lớp môn học bất kỳ
SinhVien = readerList[0]        #Số sinh viên trong mã lớp đó
MaMonHoc = []
leng = ((readerList[0]).count())["MSV"]
dataFrame2 = pd.DataFrame({"Mã lớp học" : [MaLopHoc]*leng})
dataFrame2["Mã sinh viên"] = SinhVien                   #Thêm cột MSV
dataFrame2["Số sinh viên"] = (SinhVien.count())['MSV']      #Thêm cột Số sinh viên
print("DataFrame2")
print(dataFrame2)
print()


#TẠO dataFrame3
Mon3 = mamon[2]             #Một mã môn học bất kỳ
SinhVien3 = []

MaLop3 = malop[2]
sum = 0                     #Số lượng sinh viên đăng ký môn học này
for i in range(len(classCodeList)):
    if classCodeList[i] in MaLop3:
        SinhVien3.append(readerList[i])
        sum += (readerList[i].count())["MSV"]

Student3 = pd.concat(SinhVien3, ignore_index=True)            #Kết hợp các sinh viên từ các mã lớp học
dataFrame3 = pd.DataFrame([Mon3]*sum)
dataFrame3["Mã sinh viên"] = Student3
dataFrame3["Số sinh viên"] = sum
print("DataFrame3")
print(dataFrame3)
print()


#TẠO dataFrame4
SinhVien4 = ((readerList[0]).iloc[1])["MSV"]       #Chọn 1 sinh viên bất kỳ
Lop4 = []
Mon4 = []
for i in range(len(readerList)):        #Tìm kiếm mã lớp ứng với sinh viên trên
    dem = (readerList[i]).count()
    gt = dem['MSV']
    d = readerList[i]
    for j in range(gt):
        if (d.iloc[j])["MSV"] == SinhVien4:
            Lop4.append(classCodeList[i])

for i in range(len(Lop4)):                  #Tìm kiếm Môn học ứng với mã lớp
    for j in range(malop.count()):
        if Lop4[i] in malop[j]:
            Mon4.append(mamon[j])

print(Lop4)
print(Mon4)
if len(Lop4) == len(Mon4):
    dataFrame4 = pd.DataFrame({"Mã sinh viên" : [SinhVien4]*len(Lop4),
                                "Mã lớp học" : Lop4,
                                "Môn học" : Mon4}) 
else:
    dataFrame4 = pd.DataFrame({"Mã sinh viên" : [SinhVien4]*len(Lop4),
                                "Mã lớp học" : Lop4,
                                "Môn học" : "ERROR"})
print("DataFrame4")
print(dataFrame4)  
print() 


#TẠO dataFrame5
mon1 = mamon[4]         #Cột 1
mon2 = mamon[8]         #Cột 2

ma1 = mamon[4]
ma2 = mamon[8]
SV = []


for i in range(len(classCodeList)):
    if ma1 in classCodeList[i] or ma2 in classCodeList[i]:
        SV.append(readerList[i])
        
Student5 = pd.concat(SV, ignore_index=True)            #Kết hợp các sinh viên từ các mã lớp học
d = (Student5.count())["MSV"]
Student5["Môn 1"] = mon1
Student5["Môn 2"] = mon2
Student5["Số lượng"] = d

print("DataFrame5")
print(Student5)
print()


# Thống kê dữ liệu 
subjectID = dataFrame['subjectCode']
classID = dataFrame['classCode']
print(subjectID.describe())
print()
print(classID.describe())

#Vẽ đồ thị
plt.hist(subjectID)
plt.hist(classID)
plt.show()

