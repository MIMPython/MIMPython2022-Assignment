print("Bài 5: Iterating A Directory")
txt = """
MIMpy Composition/
    filePython.py
week01_student58_TaQuangTung/
    week01_assignment02_student58_TaQuangTung.py
    week01_assignment03_student58_TaQuangTung.py
    week01_assignment01_student58_TaQuangTung.py
week02_student58_TaQuangTung/
    week02_assignment06_student58_TaQuangTung.py
    week02_assignment07_student58_TaQuangTung.py
week03_student58_TaQuangTung/
    additionalFolder/
    week03_assignment08_student58_TaQuangTung.py
    week03_assignment09_student58_TaQuangTung.py
    week03_assignment10_student58_TaQuangTung.py
week04_student58_TaQuangTung/
    additionalFolder/
        X/
        file.txt   
week05_student58_TaQuangTung/
week06_student58_TaQuangTung/
csdl.txt
HelloPython.py
Kiemtra.py
names.txt
Testfile.py
week01_student58_TaQuangTung.zip
week02_student58_TaQuangTung.zip
week03_student58_TaQuangTung.zip
week04_student58_TaQuangTung.zip
week05_student58_TaQuangTung.zip
"""

import os

def iteratingDic(directory, included_extensions):
    for filename in os.listdir(directory):
        if filename[-4:] in included_extensions or filename[-3:] in included_extensions:
            print(f"object {filename}, type file")
        else:
            print(f"object {filename}, type folder")

#Gọi đường dẫn tới
directory = "D:\MIM Python"
included_extensions = ['.txt', '.py', '.zip']            
        
iteratingDic(directory, included_extensions)
#Kết quả:
"""
object csdl.txt, type file
object HelloPython.py, type file
object Kiemtra.py, type file
object MIMpy Composition, type folder
object names.txt, type file
object Testfile.py, type file
object week01_student58_TaQuangTung, type folder
object week01_student58_TaQuangTung.zip, type file
object week02_student58_TaQuangTung, type folder
object week02_student58_TaQuangTung.zip, type file
object week03_student58_TaQuangTung, type folder
object week03_student58_TaQuangTung.zip, type file
object week04_student58_TaQuangTung, type folder
object week04_student58_TaQuangTung.zip, type file
object week05_student58_TaQuangTung, type folder
object week05_student58_TaQuangTung.zip, type file
object week06_student58_TaQuangTung, type folder
"""
