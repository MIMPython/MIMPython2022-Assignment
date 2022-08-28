import glob
import pandas as pd
globl = glob.glob("additionalFolder/TimeTablingDataset/examinationTimetablingDataset/*")
MMH = []
MLH = []
mmh = ''
mlh_temp = []
for g in globl:
    g = g.strip('.csv').split('\\')[-1]
    classCode = g
    g = g.split(' ')
    if len(g) > 1:
        index = g[1]
    else:
        index = ''


    if len(index) < 3:
        g = g[0]
    else:
        g = g[0] + ' '
        for char in index:
            if '0' > char or '9' < char:
                g += char

    if g != mmh:
        mmh = g
        MMH.append(mmh)
        if mmh != '':
            mlh_temp = []
        mlh_temp.append(classCode) 
        MLH.append(mlh_temp)
    else:
        mlh_temp.append(classCode) 

exam_another = pd.DataFrame({'subjectCode': MMH, 'classCode': MLH})
exam_another.to_csv('additionalFolder\TimeTablingDataset\exam_another.csv', index=0)
        