import os
dirPath = 'D:\\VisualCode\\Python\\MIM2022Python'
dirFiles = os.listdir(dirPath)

#get path of each file or folder in folder
fullpaths = map(lambda name: os.path.join(dirPath, name), dirFiles)

# add file name to list
folders = []
files = []
for file in fullpaths:
    if os.path.isdir(file): folders.append(os.path.basename(file)) #get name of folder
    if os.path.isfile(file): files.append(os.path.basename(file)) #get name of file
    
# print    
for file in folders:
    print("object " + str(file) + " ," + " type folder")
for file in files:
    print("object " + str(file) + " ," + "type file")