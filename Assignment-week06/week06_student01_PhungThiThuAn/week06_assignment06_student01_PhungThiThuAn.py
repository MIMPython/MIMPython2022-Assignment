# chưa hoàn thành

import pandas as pd
import os

data = pd.read_csv('additionalFolder/exams.csv')
subjectCode = list(data.iloc[:,0])
temp = data.iloc[:,-1]
classCode = []
for i in temp:
    a = set(i.split('\'')[1:-1])
    if len(a) > 1:
        a.remove(', ')
    for j in a:
        classCode.append(j)

print(classCode)

