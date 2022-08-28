
import os

path = 'C:\\Users\\PC\\Downloads'

list = os.listdir(path)

for i in list:
    p = os.path.join(path, i)

    if os.path.isdir(p):
        print ( i + ', type : folder')
    else:
        print ( i + ', type : file')
    