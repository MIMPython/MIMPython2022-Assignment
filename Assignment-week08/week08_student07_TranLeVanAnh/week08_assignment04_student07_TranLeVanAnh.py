#Bài 4
import pandas as pd
name = ['An','Binh','Chi','Dung','Giang']
classk = ['K64','K65','K65','K66','K67']
score = [7.2, 7.3, 7.4, 7.5, 7.6]
table = pd.DataFrame({'name': name, 'class': classk, 'score': score })
print(table)
