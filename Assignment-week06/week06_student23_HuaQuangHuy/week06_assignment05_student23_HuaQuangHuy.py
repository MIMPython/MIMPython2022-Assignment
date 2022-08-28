#  bai tap 5: Iterator directory
import os
# path = 'E:\Mimpython_course\week06_student23_HuaQuangHuy'
# p = os.listdir(path)
# files = []
# dirs = []
# for file in p:
#     if os.path.isfile(os.path.join(path, file)):
#         files.append((file, 'file'))
#     if os.path.isdir(os.path.join(path, file)):
#         dirs.append((file, 'dir'))


# print(files)
# print(dirs)
files = []
dirs = []


def getFileorDir(path):
    element = os.listdir(path)
    for file in element:
        if os.path.isfile(os.path.join(path, file)):
            files.append((file, 'file'))
        if os.path.isdir(os.path.join(path, file)):
            dirs.append((file, 'dir'))
            getFileorDir(os.path.join(path, file))


if __name__ == '__main__':
    path = 'E:\Mimpython_course\week06_student23_HuaQuangHuy'
    getFileorDir(path)
    print(files)
    print(dirs)
