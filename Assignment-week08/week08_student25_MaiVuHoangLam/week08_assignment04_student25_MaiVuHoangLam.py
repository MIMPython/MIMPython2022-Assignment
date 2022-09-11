from typing import Any

import pandas as pd

df1 = pd.DataFrame({
    'name': ['An', 'Binh', 'Chi', 'Dung', 'Giang'],
    'class': ['K64', 'K65', 'K65', 'K66', 'K67'],
    'score': [7.2, 7.3, 7.4, 7.5, 7.6]
})

k66 = pd.DataFrame({
    'name': [],
    'class': [],
    'score': []
})

k67 = pd.DataFrame({
    'name': [],
    'class': [],
    'score': []
})

k65 = pd.DataFrame({
    'name': [],
    'class': [],
    'score': []
})

k64 = pd.DataFrame({
    'name': [],
    'class': [],
    'score': []
})

count64 = 0
count65 = 0
count66 = 0
count67 = 0
for index in range(len(df1.index)):
    if df1['class'][index] == 'K64':
        k64.loc[count64] = df1.loc[index]
        count64 += 1
    elif df1['class'][index] == 'K65':
        k65.loc[count65] = df1.loc[index]
        count65 += 1
    elif df1['class'][index] == 'K66':
        k66.loc[count66] = df1.loc[index]
        count66 += 1
    elif df1['class'][index] == 'K67':
        k67.loc[count67] = df1.loc[index]
        count67 += 1

df2 = pd.DataFrame({
    'class': ['K64', 'K65', 'K66', 'K67'],
    'nStudents': [count64, count65, count66, count67],
    'meanScore': [sum(k64['score']) / count64, sum(k65['score']) / count65, sum(k66['score']) / count66,
                  sum(k67['score']) / count67]
})

print(df2)
# 0   K64          1       7.20
# 1   K65          2       7.35
# 2   K66          1       7.50
# 3   K67          1       7.60
