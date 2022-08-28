import os

path = 'additionalFolder/foo'
print(os.listdir(path))
for file in os.listdir(path):
    if os.path.isdir(path + '/' + file):
        print('- object ' + file + ', type folder')
    else:
        print('- object ' + file + ', type file')

