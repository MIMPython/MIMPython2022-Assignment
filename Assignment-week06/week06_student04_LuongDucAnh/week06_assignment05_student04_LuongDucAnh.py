import os

directory = input("Nhập đường dẫn: ")
 
for filename in os.listdir(directory): # iterate over files in that directory
    f = os.path.join(directory, filename)
    if os.path.isfile(f): # checking if it is a file
        print(f"object {filename}, type file")
    if os.path.isdir(f): # checking if it is a folder
        print(f"object {filename}, type folder")