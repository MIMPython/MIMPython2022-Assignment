import pandas as pd
import itertools

exams = pd.read_csv("D:/python/exams.csv")

data1 = pd.DataFrame(columns = ["MSV", "classCode", "subjectCode"])
data2 = pd.DataFrame(columns = ["classCode", "MSV", "numberOfStudents"])
data3 = pd.DataFrame(columns = ["subjectCode", "MSV", "numberOfStudents"])
data4 = pd.DataFrame(columns = ["MSV", "classCode", "subjectCode"])
data5 = pd.DataFrame(columns = ["subjectCode1", "subjectCode2", "MSV", "numberOfStudents"])

for i in exams.index:
    subjectCode = exams["subjectCode"][i]
    classCode = exams["classCode"][i]
    classCode = classCode[1:-1].replace("'", "").split(", ")
    listStudents3 = []
    for code in classCode:
        if len(code) == 0:
            continue
        path = f"D:/python/examinationTimetablingDataset/{code}.csv"
        temp = pd.read_csv(path)
        for MSV in temp["MSV"]:
            data1.loc[len(data1.index)] = [MSV, code, subjectCode]
            
        listStudents2 = sorted(temp["MSV"].tolist())
        data2.loc[len(data2.index)] = [code, listStudents2, len(listStudents2)]
        
        listStudents3 += temp["MSV"].tolist()
    listStudents3.sort()
    data3.loc[len(data3.index)] = [subjectCode, listStudents3, len(listStudents3)]

data1 = data1.sort_values(by="MSV")

data1.to_csv('./additionalFolder/data1.csv', index=False)
data2.to_csv('./additionalFolder/data2.csv', index=False)
data3.to_csv('./additionalFolder/data3.csv', index=False)

listMSV = list(set(data1["MSV"].tolist()))
listMSV.sort()
for MSV in listMSV:
    data4.loc[len(data4.index)] = [MSV,
                                   list(set(data1.loc[data1["MSV"] == MSV]["classCode"].tolist())),
                                   list(set(data1.loc[data1["MSV"] == MSV]["subjectCode"].tolist()))]
data4.to_csv('./additionalFolder/data4.csv', index=False)

listSubject = list(set(data1["subjectCode"].tolist()))
combinationSubject = itertools.combinations(listSubject, 2)
for element in combinationSubject:
    listStudentSub1 = data1.loc[data1["subjectCode"] == element[0]]["MSV"].tolist()
    listStudentSub2 = data1.loc[data1["subjectCode"] == element[1]]["MSV"].tolist()
    listStudents5 = list(set(listStudentSub1).intersection(listStudentSub2))
    data5.loc[len(data5.index)] = [element[0], element[1], listStudents5, len(listStudents5)]
    
data5.to_csv('./additionalFolder/data5.csv', index=False)

"""
    Do bài này mình làm thời gian chạy hơi lâu (2-3 phút) nên mình
    rất khó để vừa làm vừa test các ý sau
"""