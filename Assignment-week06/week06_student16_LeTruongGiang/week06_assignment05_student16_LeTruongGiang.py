import os

path = 'E:/foo'

print(f'Input: {path}')
print('Output:')
for file in os.listdir(path):
    isDir = os.path.isdir(f'E:/foo/{file}')
    if isDir == True:
        print(f'- object {file}, type folder')
    else:
        print(f'- object {file}, type file')
