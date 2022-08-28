# import required module
import os

# assign directory
directory = './'

# iterate over files in
# that directory
	
def classifyObject(path):
    if path.find('.') == -1:
        return 'folder'
    else:
        return 'file'

for filename in os.scandir(directory):
    fd, fn = filename.path.split('/')
    type = classifyObject(fn)
    print(f'Object {fn}, type {type}.')

'''
Object additionalFolder, type folder.
Object week06_assignment01_student01_PhungThiThuAn.py, type file.
Object week06_assignment02_student01_PhungThiThuAn.py, type file.
Object week06_assignment03_student01_PhungThiThuAn.py, type file.
Object week06_assignment04_student01_PhungThiThuAn.py, type file.
Object week06_assignment05_student01_PhungThiThuAn.py, type file.
Object week06_assignment06_student01_PhungThiThuAn.py, type file.
Object week06_assignment07_student01_PhungThiThuAn.py, type file.

'''
