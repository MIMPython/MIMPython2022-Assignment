import os
# Bài 5:



def get_files_folder(path):
    list_files_folder = os.listdir(path)
    for i in list_files_folder:
        if os.path.isfile(path + '\\' + i) == True:
            print(f"object {i}, type file.")
        elif os.path.isdir(path + '\\' + i) == True:
            print(f"object {i}, type folder.")
if __name__ == "__main__":
    path = "additionalFolder/folder_for_assignment05"
    get_files_folder(path)