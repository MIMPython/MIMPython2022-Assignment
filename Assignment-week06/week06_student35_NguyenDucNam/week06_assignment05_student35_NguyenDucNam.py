import os
input = '/Users/namyh/Desktop/week05_student35_NguyenDucNam'
files = os.listdir(input)
fullpaths = map(lambda name: os.path.join(input, name), files)
def checkType(link):
    if os.path.isdir(link): 
        return('object ' + os.path.basename(item) + ', ' + "type folder")
    if os.path.isfile(link): 
        return('object ' + os.path.basename(item) + ', ' + "type file")

if __name__ == '__main__':
    for item in fullpaths:  
        print(checkType(item))
        










