'''
Bài tập 4. (DataFrame groupby tricks)
a) Tạo ngẫu nhiên một DataFrame chứa dữ liệu về điểm trung bình của sinh viên. Dữ liệu cần có tối thiểu ba trường thông tin name, class, score.
b) Thống kê điểm sinh viên theo từng lớp, trình bày thống kê trong một DataFrame với ít nhất ba cột class, nStudents, meanScore.

Dưới đây là một mẫu dữ liệu (được ghi bởi định dạng JSON).

# (a)
{"name":"An","class":"K64","score":7.2}
{"name":"Binh","class":"K65","score":7.3}
{"name":"Chi","class":"K65","score":7.4}
{"name":"Dung","class":"K66","score":7.5}
{"name":"Giang","class":"K67","score":7.6}

# (b)
{"class":"K64","nStudents":1,"meanScore":7.2}
{"class":"K65","nStudents":2,"meanScore":7.35}
{"class":"K66","nStudents":1,"meanScore":7.5}
{"class":"K67","nStudents":1,"meanScore":7.6}
'''

import pandas as pd
import json

data = {'Name': ['An', 'Binh', 'Chi', 'Dung', 'Giang'],
'Class': ['K64', 'K65', 'K65', 'K66', 'K67'], 
'Score': [7.2, 7.3, 7.4, 7.5, 7.6]}


df = pd.DataFrame(data)
print(df)
'''
    Name Class  Score
0     An   K64    7.2
1   Binh   K65    7.3
2    Chi   K65    7.4
3   Dung   K66    7.5
4  Giang   K67    7.6
'''

nStudents = df['Class'].value_counts()
print(nStudents)


meanScore = df.groupby('Class').mean()['Score']
print(meanScore)


new_df = pd.DataFrame(nStudents, columns=['Class', 'nStudents'])
new_df['meanScore'] = meanScore


print(new_df)

'''
     Class nStudents  meanScore
K65      2       NaN       7.35
K64      1       NaN       7.20
K66      1       NaN       7.50
K67      1       NaN       7.60
'''
