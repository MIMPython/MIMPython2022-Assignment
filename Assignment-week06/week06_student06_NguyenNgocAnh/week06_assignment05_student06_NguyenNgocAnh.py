import glob, os
import pandas as pd
type_fold = []
obj = []
def recurPath(path, num):
    file_name = path.split('\\')[-1]
    obj.append(file_name)
    type_fold.append('folder')
    #print(num * '\t' + file_name + '/')
    dir = os.path.join(path, "*")
    globl = glob.glob(dir)
    #print(globl)
    for p in globl:
        flag = os.path.isfile(p)
        if (flag == True):
            p = p.split('\\')[-1]
            obj.append(p)
            type_fold.append('file')
            #print((num + 1) * '\t'+ p)
        else:
            recurPath(p, num + 1)
    
recurPath('D:\Python\week06_student06_NguyenNgocAnh', 0)
data = pd.DataFrame({'FILE' : obj, 'TYPE' : type_fold})
pd.DataFrame.to_csv(data,'additionalFolder/week06_assignment05_student06_NguyenNgocAnh/week06_assignment05_student06_NguyenNgocAnh_files.csv')

