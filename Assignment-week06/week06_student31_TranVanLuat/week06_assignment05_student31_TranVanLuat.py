import os
def foo(folder):
    list = os.listdir(folder)
    for index in list:
        if os.path.isdir(f"{folder}/{index}"):
            print(f"- Object {index}, type folder")
        else:
            print(f"- Object {index}, type file")

if __name__=='__main__':
    foo("D:/MIM Python/week06_student31_TranVanLuat/additionalFolder/temp")