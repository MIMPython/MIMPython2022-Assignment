import os

for f in os.listdir(r"D:\Project_1\Python\Nghịch"):
    if f.__contains__("."):
        file = f[:f.index('.')]
        type =  f[f.index('.')+1:]
        print('object '+ file +', type ' + type)
    else: 
        print('object '+ f + ', type folder')



