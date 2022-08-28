import os
# dirname = '.\Desktop'
# files = os.listdir(dirname)
# for name in files:
#     print(name)

def iterating_a_directory(folderPath):
    files = os.listdir(folderPath)
    for nameFile in files:
        print(nameFile)

if __name__=='__main__':
    iterating_a_directory('.\Desktop')

