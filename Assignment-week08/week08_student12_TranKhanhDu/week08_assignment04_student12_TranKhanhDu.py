import time
import random
import pandas as pd
import numpy
studentData = pd.DataFrame({
    'name':[], 'class':[], 'score':[]
})
with open('D:\\VisualCode\\Python\\MIM2022Python\\week08_student12_TranKhanhDu\\additionalFolder\\Players.txt') as fileObject:
    reader = fileObject.readlines()
    listOfName = []
    for line in reader:
        listOfName.append(line.rstrip('\n'))
startTime = time.time()
listOfClass = ['K64', 'K65', 'K66', 'K67']
for i in range(0, len(listOfName)):
    student = [listOfName[i], listOfClass[random.randint(0,3)], round(random.uniform(0,10), 1)]
    studentData.loc[len(studentData)] = student

print(studentData)

classData = pd.DataFrame({
    'class':[], 'studentNumber':[], 'meanScore':[]
})

numberOfK64Students = 0
sumOfK64StudentsScore = 0
for index in range(0, len(studentData)):
    if studentData.at[index, 'class'] == 'K64':
        numberOfK64Students += 1
        sumOfK64StudentsScore += studentData.at[index, 'score']
meanK64StudentsScore = round(sumOfK64StudentsScore / numberOfK64Students, 2)
classData.loc[len(classData)] = ['K64', numberOfK64Students, meanK64StudentsScore]

numberOfK65Students = 0
sumOfK65StudentsScore = 0
for index in range(0, len(studentData)):
    if studentData.at[index, 'class'] == 'K65':
        numberOfK65Students += 1
        sumOfK65StudentsScore += studentData.at[index, 'score']
meanK65StudentsScore = round(sumOfK65StudentsScore / numberOfK65Students, 2)
classData.loc[len(classData)] = ['K65', numberOfK65Students, meanK65StudentsScore]

numberOfK66Students = 0
sumOfK66StudentsScore = 0
for index in range(0, len(studentData)):
    if studentData.at[index, 'class'] == 'K66':
        numberOfK66Students += 1
        sumOfK66StudentsScore += studentData.at[index, 'score']
meanK66StudentsScore = round(sumOfK66StudentsScore / numberOfK66Students, 2)
classData.loc[len(classData)] = ['K66', numberOfK66Students, meanK66StudentsScore]

numberOfK67Students = 0
sumOfK67StudentsScore = 0
for index in range(0, len(studentData)):
    if studentData.at[index, 'class'] == 'K67':
        numberOfK67Students += 1
        sumOfK67StudentsScore += studentData.at[index, 'score']
meanK67StudentsScore = round(sumOfK67StudentsScore / numberOfK67Students, 2)
classData.loc[len(classData)] = ['K67', numberOfK67Students, meanK67StudentsScore]
endTime = time.time()
processingTime = endTime - startTime
print(classData)
print('processing time: ' + str(processingTime))



