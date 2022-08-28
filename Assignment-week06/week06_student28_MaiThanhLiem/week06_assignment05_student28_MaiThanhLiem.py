import os


directory = "C:\\Users\\Yo\\OneDrive\\Documents\\Python_Practice\\MIMPython\\Week06\\week06_student28_MaiThanhLiem"
for (root, dirs, files) in os.walk(directory):
    for dirname in dirs:
        print(f"- object {dirname}, type folder")
    for filename in files:
        print(f"- object {filename}, type file")
