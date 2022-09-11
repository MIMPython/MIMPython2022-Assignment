# bai tap 4
import pandas as pd

# create dataframe
dfStudent = pd.DataFrame({
    'name': ["Huy", "Trung", "Quang", "Hieu", "Tuan", "Hoang", "Duong", "Dung"],
    'class': ["K64A3", "K64A2", "K64A4", "K64A5", "K64A3", "K64A1", "K64A4", "K64A2"],
    'score': [9, 10, 8, 7, 6, 8, 9, 10]
})
# print(dfStudent)
# statictis
meanScore = dfStudent.groupby(['class']).mean()
newdf = dfStudent.groupby(['class']).count()
newdf.rename(columns={'name': 'nStudents', 'score': 'meanScore'}, inplace=True)
newdf['meanScore'] = meanScore['score']
print(newdf)
