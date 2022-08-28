import pandas as pd
import os
#create file path

pathToFile = 'D:\\VisualCode\\Python\\MIM2022Python\\exams.csv'
pathToFolder = 'D:\\VisualCode\\Python\\MIM2022Python\\examinationTimetablingDataset'

#read each file in folder examinationTimetablingDataset
listFile = os.listdir(pathToFolder)
fullPath = map(lambda name : os.path.join(pathToFolder, name), listFile)
readerList = []
classCodeList = []
for filePath in fullPath:
    reader = pd.read_csv(filePath)
    readerList.append(reader)
    classCodeList.append(os.path.basename(filePath).rstrip(".csv"))
# print(len(readerList[0]))
    
#read file exams.csv
dataOfSubject = pd.read_csv(pathToFile)

#get student code and sort them with ascending order
temporaryListStudentCode = []
for element in readerList:
    for index in range(0, len(element)):
        studentCode = element.at[index, "MSV"]
        temporaryListStudentCode.append(studentCode)
setStudentCode = set(temporaryListStudentCode)
listStudentCode = list(setStudentCode)
listStudentCode.sort()

#create a dataframe of students
firstDataframe = pd.DataFrame({
    "MSV":[],
    "ClassCode":[],
    "Subject code":[]})

for studentCode in listStudentCode:
    for index in range(0, len(readerList)):
        for number in range(0, len(readerList[index])):
            if readerList[index].at[number, "MSV"] == studentCode:
                            list1 = [studentCode, classCodeList[index]]
                            stringList = list1[1].split(" ")
                            list1.append(stringList[0])
                            firstDataframe.loc[len(firstDataframe)] = list1
print(firstDataframe)
firstDataframe.to_csv("firstDataframe.csv", index = False)

# create second dataframe:
secondDataFrame = pd.DataFrame({
    "ClassCode":[],
    "Student code":[],
    "Number of student":[]
})

for index in range(0, len(readerList)):
    studentCodeList = []
    for number in range(0, len(readerList[index])):
        studentCodeList.append((readerList[index]).at[number, "MSV"])
    listOfEachData = [classCodeList[index], studentCodeList, len(readerList[index])]
    secondDataFrame.loc[len(secondDataFrame)] = listOfEachData
print(secondDataFrame)
secondDataFrame.to_csv("secondDataframe.csv", index = False)
#create third dataframe
thirdDataframe = pd.DataFrame({
    "Subject code" : [],
    "Student code" : [],
    "Student number" : []
})
for index in range(0, len(dataOfSubject)):
    listClassCodeBefore = (dataOfSubject.at[index, "classCode"]).split("'")
    setClassCode = set(listClassCodeBefore)
    listClassCode = list(setClassCode)
    if len(listClassCode) > 3:
        listClassCode.remove("[")
        listClassCode.remove(", ")
        listClassCode.remove("]")
    elif len(listClassCode) == 3:
        listClassCode.remove("[")
        listClassCode.remove("]")
    else:
        listClassCode.remove("[]")
    studentCodeList2 = []
    
    for classCode in listClassCode:
        for number in range(0, len(classCodeList)):
            if str(classCode) == str(classCodeList[number]):
                for i in range(0, len(readerList[number])):
                    studentCodeList2.append(readerList[number].at[i, "MSV"])
    list2 = [dataOfSubject.at[index, "subjectCode"], studentCodeList2, len(studentCodeList2)]
    thirdDataframe.loc[len(thirdDataframe)] = list2

 
#create fourth dataframe
fourthDataFrame = pd.DataFrame({
    "MSV":[],
    "Class":[],
    "Subject":[]
})
for number in range(0, len(listStudentCode)):
    listClassCode = []
    listSubjectCode = []
    for i in range(0, len(readerList)):
        for index in range(0, len(readerList[i])):
            if listStudentCode[number] == (readerList[i]).at[index, "MSV"]:

                listClassCode.append(classCodeList[i])
                listClassCode.sort()

                subjectCode = classCodeList[i].split(" ")
                listSubjectCode.append(subjectCode[0])
                listSubjectCode.sort()

    listStudent = [listStudentCode[number], listClassCode, list(set(listSubjectCode))]
    fourthDataFrame.loc[len(fourthDataFrame)] = listStudent

fourthDataFrame.to_csv("studentsData.csv", index = False)

#create fifth dataframe from third dataframe:

fifthDataFrame = pd.DataFrame({
    "Subject 1": [],
    "Subject 2": [],
    "Students that study both subject": [],
    "Number of students":[]
})
#create subject code list
listOfSubjects = []
for i in range(0, len(thirdDataframe)):   
    subject = [(thirdDataframe.at[i, "Subject code"])] 
    listOfSubjects.append(subject)

for index1 in range(0, len(thirdDataframe)):
    for index2 in range(index1 + 1, len(thirdDataframe)):        
        set1 = set(thirdDataframe.at[index1, "Student code"])
        set2 = set(thirdDataframe.at[index2, "Student code"])
        listOfTwoSet = list(set1 & set2)
        listTwoSubjectHaveTheSameStudents = [listOfSubjects[index1], listOfSubjects[index2], listOfTwoSet, len(listOfTwoSet)]
        fifthDataFrame.loc[len(fifthDataFrame)] = listTwoSubjectHaveTheSameStudents

print(fifthDataFrame)
fifthDataFrame.to_csv("fifthDataframe.csv", index=False)
subjectData = pd.read_csv("subjectData.csv")
studentsData = pd.read_csv("studentsData.csv")
eachSubjectThatStudentStudy = pd.read_csv("eachSubjectThatStudentStudy.csv")
classData = pd.read_csv("classData.csv")
twoSubjectsHaveTheSameStudents = pd.read_csv("twoSubjectsHaveTheSameStudents.csv")

#get student number, class number and subject number
studentNumber = len(studentsData)
print("student number is " + str(studentNumber))
classNumber = len(classData)
print("class number is " + str(classNumber))
subjectNumber = len(subjectData)
print("subject number is " + str(subjectNumber))

#because the data in csv file is string, so we have to split it into list
def getLengthOfElementInCsvFile(string):
    listOfString = list(set(string.split("'")))
    if len(listOfString) > 3:
        listOfString.remove("[")
        listOfString.remove(", ")
        listOfString.remove("]")
    elif len(listOfString) == 3:
        listOfString.remove("[")
        listOfString.remove("]")
    else:
        listOfString.remove("[]")
    return listOfString

#get the mean number of subject that each student enrolled in
numberOfSubjectOfAllStudents = 0
for index in range(0, len(studentsData)):
    numberOfSubjectOfAllStudents += len(getLengthOfElementInCsvFile(studentsData.at[index, "Subject"]))
meanNumber = numberOfSubjectOfAllStudents/len(studentsData)
print("subject that is enrolled in mean is " +str(meanNumber))

#get the student that enrolled in the highest or lowest number of subject 
maxValue = 0
for index in range(0, len(studentsData)):
    numberOfSubject = len(getLengthOfElementInCsvFile(studentsData.at[index, "Subject"]))
    if numberOfSubject >= maxValue:
        maxValue = numberOfSubject

listStudentEnrolledMax = []
for index in range(0, len(studentsData)):
    if maxValue == len(getLengthOfElementInCsvFile(studentsData.at[index, "Subject"])):
        listStudentEnrolledMax.append(studentsData.at[index, "MSV"])
print("the students that enrolled in max subjects is: ")
print(listStudentEnrolledMax)

minValue = len(getLengthOfElementInCsvFile(studentsData.at[0, "Subject"]))
for index in range(0, len(studentsData)):
    numberOfSubject = len(getLengthOfElementInCsvFile(studentsData.at[index, "Subject"]))
    if numberOfSubject <= minValue:
        minValue = numberOfSubject

listStudentEnrolledMin = []
for index in range(0, len(studentsData)):
    if minValue == len(getLengthOfElementInCsvFile(studentsData.at[index, "Subject"])):
        listStudentEnrolledMin.append(studentsData.at[index, "MSV"])
print("the students that enrolled in min subjects is: ")
print(listStudentEnrolledMin)

#get the subject that most student enrolled in
maxSubject = subjectData.at[0, "Student number"]
for index in range(0, len(subjectData)):
    if subjectData.at[index, "Student number"] >= maxSubject:
        maxSubject = subjectData.at[index, "Student number"]

listSubjectBeEnrolledMax = []
for index in range(0, len(subjectData)):
    if subjectData.at[index, "Student number"] == maxSubject:
        listSubjectBeEnrolledMax.append(subjectData.at[index, "Subject code"])
print("Subjects that are enrolled in max are: ")
print(listSubjectBeEnrolledMax)

#get the subject that least student enrolled in
minSubject = subjectData.at[0, "Student number"]
for index in range(0, len(subjectData)):
    if subjectData.at[index, "Student number"] <= minSubject:
        minSubject = subjectData.at[index, "Student number"]

listSubjectBeEnrolledMin = []
for index in range(0, len(subjectData)):
    if subjectData.at[index, "Student number"] == minSubject:
        listSubjectBeEnrolledMin.append(subjectData.at[index, "Subject code"])
print("Subjects that are enrolled in min are: ")
print(listSubjectBeEnrolledMin)

#get the students that study in 2 class of a subject(đăng ký non thế :v)
listStudentsStudy2Class = []
for index in range(0, len(studentsData)):
    listOfString = list(set(studentsData.at[index, "Class"].split("'")))

    if len(listOfString) > 3:
        listOfString.remove("[")
        listOfString.remove(", ")
        listOfString.remove("]")
    elif len(listOfString) == 3:
        listOfString.remove("[")
        listOfString.remove("]")
    else:
        listOfString.remove("[]")
    listOfSubjectInClass = []

    for element in listOfString:
        variable = element.split()
        listOfSubjectInClass.append(variable[0])

    for number1 in range(0, len(listOfSubjectInClass)):
        for number2 in range(number1 + 1, len(listOfSubjectInClass)):
            if listOfSubjectInClass[number1] == listOfSubjectInClass[number2]:
                listStudentsStudy2Class.append(studentsData.at[index, "MSV"])
listStudentsStudy2Class = list(set(listStudentsStudy2Class))
listStudentsStudy2Class.sort()
    
print("Students that study in 2 class of 1 subject are: ")
print(listStudentsStudy2Class)

#get two subject that have the highest number of student:
maxStudentInTwoSubject = 0
for index in range(0, len( twoSubjectsHaveTheSameStudents)):
    if maxStudentInTwoSubject <= twoSubjectsHaveTheSameStudents.at[index, "Number of students"]:
        maxStudentInTwoSubject = twoSubjectsHaveTheSameStudents.at[index, "Number of students"]

listMaxTwoSubject = []
for index in range(0, len(twoSubjectsHaveTheSameStudents)):
    if twoSubjectsHaveTheSameStudents.at[index, "Number of students"] == maxStudentInTwoSubject:
        string = twoSubjectsHaveTheSameStudents.at[index, "Subject 1"] + twoSubjectsHaveTheSameStudents.at[index, "Subject 2"]
        listMaxTwoSubject.append(string)

print("two subjects that have the highest number of student study are: ")
for ele in listMaxTwoSubject:
    print(ele)

#DRAW HISTOGRAM



