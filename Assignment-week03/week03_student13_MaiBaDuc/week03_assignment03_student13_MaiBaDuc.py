'''
Bai 3:
Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names,
begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, 
multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, 
is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
'''
import string
A = list(string.ascii_uppercase)

s=''
with open('D://Project_1//Python//names.txt') as file_object:
    s = file_object.read()
    s = s.strip('"')
    s = s.rsplit('","')

s.sort() #sap xep theo thu tu bang chu cai

s_1 = [] #list chua gia tri cua tung ten

for i in s:
    res = 0 
    i = list(i)
    for i_1 in i:
        for k, v in enumerate(A, start=1):
            if(v==i_1):
                res += k
    s_1.append(res)

s_2 = [] #list chua gia tri de bai yeu cau

for k,v in enumerate(s, start=1):
    tmp = k*s_1[k-1]
    s_2.append(tmp)

print(s_2)
